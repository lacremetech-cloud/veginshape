# VEGINSHAPE™ — Business Tracking

**Objectif** : conserver une trace horodatée du business généré pour justifier la rémunération due sur la période d'activité, en prévision du départ d'Elio (préavis au 22 novembre 2026).

---

## Contexte

- **Dernier snapshot** : 2026-11-08
- **Date préavis Elio** : 2026-11-22
- **Risque** : retrait progressif des accès (agenda, CRM, Calendly, facturation, etc.)
- **Action** : capturer un maximum de données avant perte d'accès

---

## Fichiers

### `agenda-calls-2026-11-07.csv`

Export de l'agenda au 7 novembre 2026, couvrant la période **30 oct. 2026 → 10 janv. 2027** (55 actions business : 29 R1, 13 R2, 1 R3, 1 relance, 11 calls groupe).

### `transactions-2026-11-08.csv`

Export des factures/remboursements au 8 novembre 2026, couvrant la période **9 sept. 2026 → 7 nov. 2026** (50 transactions : 48 factures, 2 remboursements).

**Colonnes** :
- `transaction_id` (F### ou R##)
- `type` (Facture / Remboursement)
- `date`, `heure`
- `client`, `email`, `nouveau_client`
- `montant` (signé), `devise` (EUR/CHF)
- `offre` (libellé facture)
- `contrat_total_estime` (valeur totale du contrat, pas juste la mensualité)
- `plan_echelonnement` (3x, 5x, 10x, 12x, one-shot)

---

## 📊 Récapitulatif chiffré

### Agenda (snapshot 2026-11-07)

| Type | Nombre |
|---|---|
| R1 Consultations | 29 |
| R2 (follow-up / closing) | 13 |
| R3 | 1 |
| Relance | 1 |
| Call groupe VEGINSHAPE™ | 11 |
| **Total actions business** | **55** |

**Répartition code setter (R1 uniquement)** : V=19, I=5, H=2, GO=1, W=1, S=1

### Transactions (snapshot 2026-11-08 — période 9 sept → 7 nov 2026)

| Indicateur | Valeur |
|---|---|
| Factures émises | 48 |
| Remboursements | 2 |
| Clients distincts | 33 |
| Nouveaux clients (tag "Nouveau") | 3 (Emir Belkahia, Severine Bassahon, Sara Enggist) |

**Cash-in encaissé sur la période :**

| Devise | Encaissé | Remboursé | **Net** |
|---|---:|---:|---:|
| EUR | +14 858,00 € | −360,00 € | **+14 498,00 €** |
| CHF | +932,00 CHF | −360,00 CHF | **+572,00 CHF** |

**Contrat total (valeur contractuelle signée, hors doublons mensualités) :**

| Devise | Contrat total |
|---|---:|
| EUR | **67 413,00 €** |
| CHF | **7 313,00 CHF** |

> ⚠️ **Base de commission à clarifier** : la commission se calcule-t-elle sur l'encaissement mensuel ou sur la valeur contractuelle totale ? La différence est **majeure** (x4-x5 selon les contrats 10-12x). À confirmer avant toute réclamation.

---

## 🚨 Prochaines étapes urgentes avant perte d'accès

1. **Export Calendly natif** — l'accès est ouvert (compte Rayyan Indescale, timezone Europe/Berlin). À lancer via l'API pour récupérer tous les events avec emails prospects + source + UTM.
2. **Historique complet des factures** — remonter avant F518 (sept. 2026) pour couvrir toute la période d'activité.
3. **Deals/leads non signés** — exporter le pipeline CRM (prospects en cours, NRP, à relancer).
4. **Screenshots horodatés** — Calendly, facturation, CRM — chaque page à archiver dans `screenshots/YYYY-MM-DD/`.
5. **Attribution source** — pour chaque client, identifier la source (ads Meta, bouche-à-oreille, Insta, YouTube, etc.) pour justifier l'apport.
6. **Historique Gmail** — confirmations de booking + emails de closing (preuves de closing côté agence).
7. **Contrat / accord commission** — récupérer et archiver l'écrit (email, DocuSign, chat) qui formalise la rémunération due.

---

## Notes de parsing

- Les montants mensuels (ex. 290€ pour un contrat 3490€ en 11x) apparaissent chaque mois ; la colonne `contrat_total_estime` donne la valeur totale.
- Récurrences détectées : Olivier Barbosa (2x), Nathan Bruyneel (2x), Kétura Baptiste (2x), Sebastien Ceraulo (2x), Thao Mucci (2x), Marie-hélène Quemon (2x), Jeanne Ysnel (2x), Géraldine Lollier (2x), Ophélie Chretien (2x), Lili Dufour (2x), Estelle Parisi (2x), Sandie Tichané (2x), Christelle Pernette (2x), Laura Delcourt (2x), Ke Thien Nguyen (2x) — ce sont les mensualités des contrats échelonnés, pas des doublons.
- Remboursement R10 (Martine Steininger) : même jour/heure que la facture F548 → facture annulée immédiatement (test ou erreur).
- Remboursement R9 (Catherine Donabedian) : même jour/heure que F523 → idem.

---

*Snapshots générés à partir de copier-collers manuels. Pour une source de vérité fiable, compléter par des exports natifs (Calendly / Stripe / Dougs / Qonto) dès que possible.*
