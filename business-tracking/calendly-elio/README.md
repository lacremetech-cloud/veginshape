# Export Calendly Elio Vegan Coach — snapshots

## Compte source

- **User** : Elio Vegan Coach 🌱 (`eliovegancoach@gmail.com`)
- **URL** : `calendly.com/eliovegancoach`
- **User URI** : `https://api.calendly.com/users/3243ac92-20e8-4b7f-a9b5-3fc40f1c4434`
- **Org URI** : `https://api.calendly.com/organizations/a0cee5cd-b706-4e1f-b84a-0f04114e6b39`
- **Timezone** : Europe/Berlin
- **Compte créé** : 2023-04-09 — **3,5 ans d'historique disponible**
- **Dernière MAJ** : 2026-10-20 (coïncidence avec la préparation du préavis)

## Event Types identifiés

| URI | Nom suspecté |
|---|---|
| `c3e5b816-a669-48a3-bc31-bfe18e8e8283` | CONSULTATION VEGINSHAPE™ (I) — setter Indescale |
| `542f1a1f-1af5-493f-aa97-8aefa352c1e3` | CONSULTATION VEGINSHAPE™ (V) — setter V |
| `66261b5b-9bdc-410d-b8d2-6b03c6e75009` | CONSULTATION VEGINSHAPE™ (B) — setter B |
| `2564e2a7-8edd-4f89-b064-843fde52b11f` | CONSULTATION VEGINSHAPE™ (W) — setter W |

À compléter via `event_types-list_event_types` dans un prochain snapshot.

---

## cancellations-depuis-2026-10-22.csv

**19 événements annulés entre le 22/10 et le 09/11/2026**, avec timestamp exact + auteur + raison.

### 🚨 Finding critique : 5 annulations "Test" par Elio lui-même juste après la notification de préavis

| Date start | Date cancel | Canceled by | Raison |
|---|---|---|---|
| 22/10 11:40 UTC | 22/10 06:03 UTC | **Elio (host)** | "Doublon" |
| 24/10 14:00 UTC | 24/10 05:48 UTC | **Elio (host)** | "Test" |
| 24/10 15:00 UTC | 24/10 05:48 UTC | **Elio (host)** | "Test" |
| 28/10 08:00 UTC | 26/10 12:53 UTC | **Elio (host)** | "Test" |
| 28/10 09:00 UTC | 26/10 12:53 UTC | **Elio (host)** | "Test" |
| 28/10 12:30 UTC | 26/10 12:53 UTC | **Elio (host)** | "Test" |

**Interprétation** : Entre le 22/10 et le 26/10 (période du début du préavis supposé), Elio a **supprimé lui-même 6 RDV** en les qualifiant de "Doublon" ou "Test". Ces raisons sont formellement douteuses :

- "Test" répété 5 fois sur 4 dates différentes ne ressemble pas à un vrai nettoyage de tests mais à une **purge anticipée** de bookings qu'Elio ne voulait pas honorer pendant le préavis.
- Le pattern coïncide exactement avec la fenêtre de préparation du préavis (29/10 étant la date du 1er message Slack d'Elio sur son plan de sortie).

**→ Ces 6 cancellations renforcent l'argument de mauvaise foi contractuelle (art. 1104 Code civil) que nous développons dans `STRATEGIE-NEGOCIATION-sortie-contrat.md`.**

### Autres annulations : churn invitee normal (13 événements)

Les 13 annulations restantes sont des cancellations **par les prospects eux-mêmes** (canceler_type = "invitee") avec des raisons plausibles (conflit horaire, RDV médical, hésitation prix, vétérinaire imprévu, etc.). Churn normal d'un pipeline VSL.

**Insight produit** : la raison de Géraldine Rappe (*"désagréable de ne pas avoir de fourchette de tarif avant la consultation"*) est une **objection de pricing** que l'équipe Elio pourrait adresser côté landing/VSL pour réduire ce churn. Idem Ludivine Korner (*"recherche uniquement un accompagnement nutrition"*) → segmentation offre à préciser en amont.

---

## À exporter ensuite (si budget temps/tokens)

- Événements **actifs** futurs (du 2026-11-10 à horizon 3 mois)
- Événements **actifs + canceled** sur 90 derniers jours (pour comparer taux de cancellation et identifier les patterns)
- Événements **sur toute la période du contrat** (19/10/2025 → aujourd'hui) pour compter le volume total de R1 bookés = **ordre de grandeur du pipeline généré par Crème Tech**

Le script `scripts/snapshot-systemeio.py` existe déjà pour Systeme.io. Un script jumeau `snapshot-calendly.py` pourrait être écrit sur le même modèle en utilisant le token OAuth Calendly actif de la session MCP (mais la clé OAuth n'est pas exposable en var d'env comme pour Systeme.io — il faudrait un token personnel Calendly).
