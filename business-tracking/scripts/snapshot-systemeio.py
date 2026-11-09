#!/usr/bin/env python3
"""
Snapshot Systeme.io — à exécuter au moment du gel du périmètre
(ex. 22/11/2026 à 23:59 CET pour le préavis).

Objet
-----
Télécharge en une passe tous les contacts Systeme.io (avec leurs tags),
consolide en CSV horodaté, extrait les sous-ensembles critiques pour
le calcul de commission, et commit + push sur la branche en cours.

Prérequis
---------
- Variable d'environnement SIO_API_KEY contenant la clé API Systeme.io.
  (Cette clé N'EST PAS stockée dans le repo pour raisons de sécurité.)
- Les outils: python3, curl ou requests, git configurés pour push.

Usage
-----
    export SIO_API_KEY="be75lmef9ody5jpxu40tu8bi0hqt2eqqpykt6iru49oxo26cvekyqaqd3a1vtcv5"
    python3 business-tracking/scripts/snapshot-systemeio.py

Options
-------
    --no-push       : commit local uniquement, ne push pas.
    --no-commit     : produit les fichiers mais ne commit pas.
    --date YYYY-MM-DD : force la date d'horodatage (default: aujourd'hui en UTC).

Sortie
------
    business-tracking/systemeio-raw/snapshot-YYYY-MM-DD/contacts-pageNNN.json  (gitignored)
    business-tracking/systemeio-contacts-YYYY-MM-DD.csv                        (commit)
    business-tracking/systemeio-tag-CLIENT-YYYY-MM-DD.csv                      (commit)
    business-tracking/systemeio-tag-RDV-booke-YYYY-MM-DD.csv                   (commit)
    business-tracking/systemeio-tag-Prospects-iClosed-YYYY-MM-DD.csv           (commit)
    business-tracking/systemeio-stats-YYYY-MM-DD.md                            (commit)
"""

import argparse
import csv
import json
import os
import shutil
import subprocess
import sys
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


API_URL = "https://api.systeme.io/api/contacts"
REPO_ROOT = Path(__file__).resolve().parents[2]
BT_DIR = REPO_ROOT / "business-tracking"
RAW_DIR_PARENT = BT_DIR / "systemeio-raw"

# Les tags qu'on extrait dans leur propre CSV pour accès rapide
TAGS_TO_EXTRACT = [
    ("Client", "CLIENT"),
    ("RDV booké", "RDV-booke"),
    ("Prospects iClosed", "Prospects-iClosed"),
]


def api_get(path_and_query, api_key):
    req = urllib.request.Request(
        f"{API_URL}{path_and_query}",
        headers={"X-API-Key": api_key, "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def paginate_all_contacts(api_key, raw_dir):
    raw_dir.mkdir(parents=True, exist_ok=True)
    page = 1
    last_id = None
    total = 0
    while True:
        qs = "?limit=100" + (f"&startingAfter={last_id}" if last_id else "")
        try:
            data = api_get(qs, api_key)
        except Exception as e:
            print(f"ERREUR page {page}: {e}", file=sys.stderr)
            raise
        items = data.get("items", [])
        has_more = data.get("hasMore", False)
        out = raw_dir / f"contacts-page{page:03d}.json"
        out.write_text(json.dumps(data, ensure_ascii=False))
        total += len(items)
        if page % 10 == 0 or not has_more:
            print(f"  page {page:>3}: {len(items)} items, total={total}, hasMore={has_more}")
        if not has_more or not items:
            break
        last_id = items[-1]["id"]
        page += 1
        if page > 500:
            print("ARRÊT DE SÉCURITÉ: plus de 500 pages", file=sys.stderr)
            break
    return total, page


def consolidate_csv(raw_dir, out_csv):
    rows = []
    for page_file in sorted(raw_dir.glob("contacts-page*.json")):
        data = json.loads(page_file.read_text())
        for item in data.get("items", []):
            rows.append({
                "sio_id": item.get("id", ""),
                "email": item.get("email", ""),
                "registeredAt": item.get("registeredAt", ""),
                "locale": item.get("locale", ""),
                "unsubscribed": item.get("unsubscribed", False),
                "bounced": item.get("bounced", False),
                "sourceURL": item.get("sourceURL", "") or "",
                "tags": "|".join(t.get("name", "") for t in (item.get("tags") or [])),
            })
    rows.sort(key=lambda r: r["sio_id"], reverse=True)
    with out_csv.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["sio_id", "email", "registeredAt", "locale",
                                         "unsubscribed", "bounced", "sourceURL", "tags"])
        w.writeheader()
        w.writerows(rows)
    return rows


def write_tag_subset(rows, tag_name, out_csv):
    sub = [r for r in rows if tag_name in (r["tags"] or "").split("|")]
    with out_csv.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["sio_id", "email", "registeredAt", "locale",
                                         "unsubscribed", "bounced", "sourceURL", "tags"])
        w.writeheader()
        w.writerows(sub)
    return len(sub)


def write_stats(rows, out_md, snap_date, nb_pages, subsets_counts):
    tag_counter = Counter()
    nb_with_tag = 0
    for r in rows:
        tags = [t for t in (r["tags"] or "").split("|") if t]
        if tags:
            nb_with_tag += 1
        for t in tags:
            tag_counter[t] += 1
    oldest = min((r["registeredAt"] for r in rows if r["registeredAt"]), default="N/A")
    newest = max((r["registeredAt"] for r in rows if r["registeredAt"]), default="N/A")
    nb = len(rows)
    with out_md.open("w") as f:
        f.write(f"# Snapshot Systeme.io — {snap_date}\n\n")
        f.write(f"**Total contacts** : {nb}\n\n")
        f.write(f"**Pages API paginées** : {nb_pages}\n\n")
        f.write(f"**Contacts avec au moins un tag** : {nb_with_tag} ({100*nb_with_tag//max(nb,1)} %)\n\n")
        f.write(f"**Fenêtre d'inscription** : {oldest} → {newest}\n\n")
        f.write("## Répartition par tag\n\n")
        f.write("| Tag | Nombre |\n|---|---:|\n")
        for tag, n in tag_counter.most_common():
            f.write(f"| {tag} | {n} |\n")
        f.write("\n## Extractions dédiées\n\n")
        f.write("| Fichier | Lignes |\n|---|---:|\n")
        for tag_name, slug in TAGS_TO_EXTRACT:
            f.write(f"| systemeio-tag-{slug}-{snap_date}.csv | {subsets_counts.get(tag_name, 0)} |\n")


def run_git(args, check=True):
    return subprocess.run(["git"] + args, cwd=str(REPO_ROOT), check=check,
                          capture_output=True, text=True)


def git_commit_and_push(snap_date, total, subsets_counts, do_commit, do_push):
    files_to_add = [
        f"business-tracking/systemeio-contacts-{snap_date}.csv",
        f"business-tracking/systemeio-stats-{snap_date}.md",
    ]
    for _, slug in TAGS_TO_EXTRACT:
        files_to_add.append(f"business-tracking/systemeio-tag-{slug}-{snap_date}.csv")
    if not do_commit:
        print("\n--no-commit: fichiers produits mais pas committés.")
        return
    run_git(["add"] + files_to_add)
    tag_stats_line = ", ".join(
        f"{subsets_counts.get(name, 0)} {name}" for name, _ in TAGS_TO_EXTRACT
    )
    msg_lines = [
        f"Snapshot Systeme.io — {snap_date} ({total} contacts)",
        "",
        f"Timestamped freeze of the full Systeme.io contact base",
        f"({total} contacts) used as the contractual baseline for",
        f"commission computation. Extracts: {tag_stats_line}.",
        "",
        "Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>",
        "Claude-Session: https://claude.ai/code/session_01KwWQEVa676Q5JfHBMGa16z",
    ]
    msg = "\n".join(msg_lines)
    r = run_git(["commit", "-m", msg], check=False)
    if r.returncode != 0:
        print("Commit non effectué (peut-être rien à committer) :")
        print(r.stdout)
        print(r.stderr)
    else:
        print("Commit OK.")
    if not do_push:
        print("--no-push: pas de push.")
        return
    branch_r = run_git(["branch", "--show-current"])
    branch = branch_r.stdout.strip()
    print(f"Push vers origin/{branch} ...")
    pr = run_git(["push", "origin", branch], check=False)
    print(pr.stdout)
    if pr.returncode != 0:
        print("ATTENTION: push a échoué:", pr.stderr, file=sys.stderr)
    else:
        print("Push OK.")


def main():
    ap = argparse.ArgumentParser(description="Snapshot Systeme.io horodaté + commit")
    ap.add_argument("--no-push", action="store_true", help="Ne pas pusher après commit")
    ap.add_argument("--no-commit", action="store_true", help="Ne pas committer après produire les fichiers")
    ap.add_argument("--date", help="Date d'horodatage YYYY-MM-DD (défaut: aujourd'hui UTC)")
    args = ap.parse_args()

    api_key = os.environ.get("SIO_API_KEY")
    if not api_key:
        print("ERREUR: variable d'environnement SIO_API_KEY manquante.", file=sys.stderr)
        print("Avant de lancer:  export SIO_API_KEY=\"...\"", file=sys.stderr)
        sys.exit(2)

    snap_date = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"=== Snapshot Systeme.io — date d'horodatage : {snap_date} ===\n")

    raw_dir = RAW_DIR_PARENT / f"snapshot-{snap_date}"
    if raw_dir.exists():
        print(f"(Le dossier raw existe déjà, on repart à zéro : {raw_dir})")
        shutil.rmtree(raw_dir)

    print("Pagination de toute la base contacts ...")
    total, nb_pages = paginate_all_contacts(api_key, raw_dir)
    print(f"→ {total} contacts téléchargés en {nb_pages} pages.\n")

    print("Consolidation CSV ...")
    out_csv = BT_DIR / f"systemeio-contacts-{snap_date}.csv"
    rows = consolidate_csv(raw_dir, out_csv)
    print(f"→ {out_csv.name} : {len(rows)} lignes.\n")

    print("Extractions par tag ...")
    subsets = {}
    for tag_name, slug in TAGS_TO_EXTRACT:
        out = BT_DIR / f"systemeio-tag-{slug}-{snap_date}.csv"
        n = write_tag_subset(rows, tag_name, out)
        subsets[tag_name] = n
        print(f"  {tag_name:<22} → {n} contacts  ({out.name})")
    print()

    print("Stats ...")
    out_md = BT_DIR / f"systemeio-stats-{snap_date}.md"
    write_stats(rows, out_md, snap_date, nb_pages, subsets)
    print(f"→ {out_md.name}")
    print()

    git_commit_and_push(snap_date, total, subsets,
                        do_commit=not args.no_commit,
                        do_push=not args.no_push)

    print("\n=== Terminé. ===")


if __name__ == "__main__":
    main()
