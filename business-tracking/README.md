# VEGINSHAPE™ — Business Tracking

**Objectif** : conserver une trace horodatée du business généré pour justifier la rémunération due sur la période d'activité, en prévision du départ d'Elio (préavis au 22 novembre 2026).

---

## Contexte

- **Date de snapshot** : 2026-11-07
- **Date préavis Elio** : 2026-11-22
- **Risque** : retrait progressif des accès (agenda, CRM, Calendly, etc.)
- **Action** : capturer un maximum de données avant perte d'accès

---

## Fichiers

### `agenda-calls-2026-11-07.csv`

Export de l'agenda au 7 novembre 2026, couvrant la période **30 oct. 2026 → 10 janv. 2027**.

**Colonnes** :
- `date`, `jour`, `heure_debut`, `heure_fin`
- `type` : `R1-Consultation`, `R2` (follow-up), `R3`, `Call-Groupe`, `Relance`
- `code_setter` : code setter/closer figurant dans le nom de l'event (I, V, H, GO, W, S)
- `prospect_client` : nom
- `date_lead` : date d'origine du lead (pour les R2/Relances)
- `statut` : note de présence (ex. "Présence reconfirmée")
- `notes`

**Événements perso exclus** : anniversaire Jadore (31 oct.), Bowling La Brume (2 nov.), Déchèterie (7 nov.), "Go voir Anton'" (9 nov.), "Pas dispo" (2 nov.), "Call Saj" (12 nov. — à reclasser si business).

---

## Récapitulatif chiffré (snapshot 2026-11-07)

| Type | Nombre |
|---|---|
| R1-Consultation (premier call) | 29 |
| R2 (follow-up / closing) | 13 |
| R3 | 1 |
| Relance | 1 |
| Call groupe VEGINSHAPE™ | 11 |
| **Total actions business** | **55** |

### Répartition par code setter (R1-Consultations uniquement)

| Code | Nombre |
|---|---|
| V | 19 |
| I | 5 |
| H | 2 |
| GO | 1 |
| W | 1 |
| S | 1 |

> Les codes setter (I, V, H, GO, W, S) correspondent probablement aux initiales des setters/closers ayant booké le call. À confirmer et documenter pour justifier les commissions.

---

## Prochaines étapes recommandées

1. **Captures d'écran agenda** — faire des screenshots de Calendly / Google Calendar pour chaque semaine, à archiver dans `business-tracking/screenshots/`.
2. **Export Calendly brut** — télécharger l'export CSV natif Calendly (plus de détails : source, UTM, email prospect) tant que l'accès est ouvert.
3. **Export CRM** — récupérer la liste complète des leads/deals avec statut, montant, propriétaire (code setter).
4. **Historique emails** — archiver les confirmations de booking et les emails de closing dans un dossier séparé.
5. **Statistiques Meta Ads** — screenshots des campagnes et attribution (source du trafic).
6. **Deals clôturés (signés)** — faire un fichier `deals-closed.csv` séparé avec montants, pour calcul de commission.
7. **Commit Git** — une fois validé, committer ce dossier sur la branche `claude/quirky-feynman-dgGs0` pour avoir la trace horodatée Git (immutable).

---

## Notes de parsing

- "CONSULTATION VEGINSHAPE™ (X)" → typé `R1-Consultation`, lettre entre parenthèses → `code_setter`
- "R2 [Nom] Lead [date]" → typé `R2`, date du lead extraite
- "R3 avec [Nom]" → typé `R3`
- "Relancer [Nom] Lead [date]" → typé `Relance`
- Un conflit horaire noté sur Florian Despont 31 oct. (13:00) — reporté le 12 nov. (10:00)
- Deux occurrences pour Florian Despont (31 oct. + 12 nov.) et Aurélie Nguyen (7 nov. R1 + 16 nov. R2)

---

*Snapshot généré le 2026-11-07 à partir d'un copier-coller manuel de l'agenda. Pour une source de vérité fiable, compléter par des exports natifs (Calendly / CRM) dès que possible.*
