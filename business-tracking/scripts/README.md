# Scripts — Snapshots horodatés

## Pourquoi

Figer l'état du pipeline VEGINSHAPE à des dates clés (notamment **le 22/11/2026 à 23:59 CET**, fin du préavis) pour documenter la base de calcul des commissions. Chaque snapshot est commit avec horodatage GitHub immutable : preuve à produire en cas de litige.

## snapshot-systemeio.py

Télécharge en une passe **tous les contacts Systeme.io** (avec tags), consolide en CSV, extrait les sous-ensembles critiques (Client, RDV booké, Prospects iClosed), écrit un résumé stats, et commit + push automatiquement.

### Prérequis

1. **Clé API Systeme.io** dans une variable d'environnement (jamais dans le repo) :
   ```bash
   export SIO_API_KEY="be75lmef9ody5jpxu40tu8bi0hqt2eqqpykt6iru49oxo26cvekyqaqd3a1vtcv5"
   ```
2. **Git configuré** pour pousser sur la branche en cours.
3. **Python 3.9+** (utilise la stdlib uniquement, aucune dépendance externe).

### Usage

```bash
# Snapshot standard (horodatage = aujourd'hui UTC), avec commit+push
python3 business-tracking/scripts/snapshot-systemeio.py

# Forcer une date précise (utile pour le gel au 22/11)
python3 business-tracking/scripts/snapshot-systemeio.py --date 2026-11-22

# Produire les fichiers sans committer
python3 business-tracking/scripts/snapshot-systemeio.py --no-commit

# Commit local sans push
python3 business-tracking/scripts/snapshot-systemeio.py --no-push
```

### Fichiers produits

| Fichier | Statut Git |
|---|---|
| `systemeio-raw/snapshot-YYYY-MM-DD/contacts-pageNNN.json` | gitignored (lourd, ~5 MB) |
| `systemeio-contacts-YYYY-MM-DD.csv` | **commit** |
| `systemeio-tag-CLIENT-YYYY-MM-DD.csv` | **commit** |
| `systemeio-tag-RDV-booke-YYYY-MM-DD.csv` | **commit** |
| `systemeio-tag-Prospects-iClosed-YYYY-MM-DD.csv` | **commit** |
| `systemeio-stats-YYYY-MM-DD.md` | **commit** |

### Durée

~2 à 3 minutes pour ~12 500 contacts (126 pages de 100).

### Plan opérationnel pour le 22/11/2026

**Phase 1 — Juste avant minuit CET du 22/11 (ex. 23:50)** :

```bash
cd /chemin/vers/veginshape
git pull origin claude/quirky-feynman-dgGs0
export SIO_API_KEY="..."  # La clé actuelle
python3 business-tracking/scripts/snapshot-systemeio.py --date 2026-11-22
```

**Phase 2 — Snapshot manuel à compléter le même soir** :

Le script Systeme.io est automatisable, mais ces éléments doivent être capturés **à la main** (accès propriétaire) :

- [ ] **Capture Calendly** de la liste des RDV futurs (export CSV si dispo, sinon screenshots). Compte Elio `eliovegancoach`.
- [ ] **Capture facturation** (Stripe / Qonto Elio / Dougs Elio) de toutes les factures émises jusqu'au 22/11 inclus.
- [ ] **Capture du pipeline iClosed** (ou outil de closing équivalent) si accessible.
- [ ] **Capture Meta Ads Manager** : campagnes actives au 22/11, dépenses, performances par ad.
- [ ] **Capture Wistia** : stats VSL `l67oat8gve` à J+0.
- [ ] **Capture Slack** : toute conversation Elio → Rayyan récente, en particulier confirmation/refus de la lecture commission.

Ces captures vont dans `business-tracking/screenshots/2026-11-22/`.

**Phase 3 — Rédaction du relevé de commission** :

Une fois les snapshots pris, produire un `COMMISSION-A-FACTURER-2026-11-22.md` qui liste :

- Pour chaque plan échelonné signé avant le 22/11 : échéancier des mensualités à venir avec commission 15 %.
- Pour chaque lead taggé "RDV booké" ou "Prospects iClosed" au 22/11 : identifiant + email + date d'entrée dans le pipe.
- Pour chaque close déjà encaissé non commissionné : ligne de rattrapage.

Puis commit + push.

## Ce qu'il manque pour automatiser davantage

Si demain tu ajoutes les clés API suivantes aux variables d'environnement, on peut écrire les scripts équivalents :

- **STRIPE_SECRET_KEY** → snapshot des factures + plans échelonnés en cours
- **QONTO_ORGANIZATION_SLUG + QONTO_API_TOKEN** (côté Veginshape si accessible) → snapshot des encaissements
- **DOUGS_API_TOKEN** (côté Veginshape) → snapshot comptable
- **CALENDLY_PERSONAL_TOKEN** (compte Elio) → snapshot complet des events (actifs + annulés)
- **META_ADS_ACCESS_TOKEN** → snapshot des campagnes + perfs
- **WISTIA_API_TOKEN** → snapshot des stats VSL

Chaque clé supplémentaire = un fichier `.py` similaire à côté. Dire quelle API tu veux prioriser.
