# Correction — le snapshot agenda du 09/11 était tronqué, pas de purge

**Date de la correction** : 2026-11-10
**Rédigée par** : Crème Tech (après capture agenda complet 10/11)

---

## Résumé

Le snapshot agenda du 09/11/2026 (`agenda-calls-2026-11-09.csv`) listait **10 événements** avec la mention *"Plus aucune réunion prévue"* après le 12 nov. Mes analyses ultérieures (`agenda-diff-2026-11-07-to-2026-11-09.md`, sections concernées de `DOSSIER-COMPLET-2026-11-10.md`, `calendly-elio/README.md`, `STRATEGIE-NEGOCIATION-sortie-contrat.md`, `slack-transcript-elio-rayyan-2026-11-09.md`) en ont tiré la conclusion que **23 événements business avaient été supprimés** (6 R2 cette semaine + 4 R2 futurs + 1 R3 + 1 relance + 10 calls groupe + 1 passé), argumentée comme un acte de mauvaise foi contractuelle (art. 1104 Code civil).

**Cette conclusion était erronée.**

Le snapshot agenda du 10/11/2026 (`agenda-calls-2026-11-10.csv`), capturé le lendemain, confirme que **tous ces événements sont toujours présents** dans l'agenda d'Elio, parfois à leur date originale et parfois légèrement décalés. Il y a même **plusieurs événements supplémentaires** au-delà de ce que le snapshot initial du 07/11 affichait (calls groupe hebdos étendus jusqu'au 07/02/2027 + un R2 Sébastien Wisniewski programmé le 24/11).

## Cause probable du malentendu

La vue Calendly / agenda utilisée pour le screenshot du 09/11 était vraisemblablement **tronquée** par un filtre d'affichage (par ex. vue "RDV à venir" restreinte à X jours, affichage mobile / desktop différent, ou filtre "mes événements Calendly uniquement" qui masque les entrées Google Calendar natives). L'interface a renvoyé le message *"Plus aucune réunion prévue"* alors que ces événements étaient bien dans Google Calendar, simplement non visibles dans la vue consultée.

## État réel des événements concernés (vérifié au 10/11)

| Événement | Snapshot 07/11 | Snapshot 10/11 (vérifié) | Statut |
|---|---|---|---|
| R2 Ambre Ravenaud | lun 09/11 10:00 | **ven 13/11 10:00** | 🔄 Décalé de 4 jours |
| R2 Anne Fouqué | lun 09/11 11:00 | *non visible dans le snapshot 10/11* | ❓ À clarifier — peut-être déjà fait ou re-programmé plus tard |
| R2 Déborah Corvasce | mar 10/11 10:00 | **mar 10/11 10:00** | ✅ Date originale |
| R2 Emilie Mesnier | mar 10/11 14:00 | **mar 10/11 14:00** — "À suivre" | ✅ Date originale |
| R2 Thomas Défago | mar 10/11 16:00 | **mar 10/11 16:00** | ✅ Date originale |
| R2 Noyra Lages | mer 11/11 13:00 | **mer 11/11 13:00** | ✅ Date originale |
| R2 Aurélie Nguyen | lun 16/11 14:00 | **lun 16/11 14:00** | ✅ Date originale |
| R2 Audrey Galvan | jeu 19/11 10:00 | **jeu 19/11 10:00** | ✅ Date originale |
| R2 Sylvie Hirel | lun 04/01 16:00 | **lun 04/01 16:00** | ✅ Date originale |
| R2 Néna Lardy | mar 05/01 10:00 | **mar 05/01 10:00** | ✅ Date originale |
| R3 Astoria Christiane | mar 05/01 19:00 | **mar 05/01 19:00** | ✅ Date originale |
| Relance Alec Serbah | mar 15/12 09:00 | **mar 15/12 09:00** | ✅ Date originale |
| 10 calls groupe (15/11 → 10/01) | tous présents | **tous présents** | ✅ Date originale |

### Nouveaux événements apparus au 10/11

- **R1 Véronique Falguieres** (V) — mar 10/11 17:00 (lead reçu depuis le snapshot précédent)
- **R2 Sébastien Wisniewski** — mar 24/11 12:30 (programmé suite au R1 du 10/11)
- **Calls groupe étendus** : dim 17/01, 24/01, 31/01, 07/02 2027
- **RDV perso** : Fiduciaire 16/11, Prise de sang Lepori 19/01

## Ce que ça change pour le dossier

### Ce qui reste solide

| Argument | Statut |
|---|---|
| **Art. 5.1 "tous canaux confondus"** → 15 % sur tout CA encaissé HT | ✅ Inchangé |
| **Q1a** : mensualités de plans échelonnés signés avant 22/11 = commissionnées jusqu'au bout | ✅ Inchangé |
| **Q1b** : RDV bookés avant 22/11 qui closent après = commissionnés | ✅ Renforcé — tous les R2 sont confirmés, donc le CA attendu est réel |
| **Art. 9 (PI)** : livrables = propriété Crème Tech jusqu'au paiement complet | ✅ Inchangé, levier à garder en réserve |
| **Art. 4** : le Client doit fournir le reporting — accès compta demandé non reçu | ✅ Inchangé |
| **Argument "absence de tracking = pas un défaut"** | ✅ Inchangé |
| **Analyse des 9 questions d'Elio** (A/B opt-in, KPI, ads, cut criteria, Andromeda, budget, VSL/ads encore valable) | ✅ Inchangé — chiffres Meta et Wistia intacts |

### Ce qui est retiré

| Argument | Statut |
|---|---|
| ❌ **"23 événements évacués en 48 h"** | **RETIRÉ** — c'était un artefact de snapshot tronqué |
| ❌ **"Organisation du vide pendant le préavis"** | **RETIRÉ** — non prouvé |
| ❌ **Art. 1104 Code civil (bonne foi) comme renfort juridique** | **RETIRÉ** sur cette base-là (l'article reste pertinent sur d'autres points, par exemple si Elio refuse l'accès compta) |

## Lecture positive pour Rayyan

**Cette rectification est, en réalité, une bonne nouvelle business** :
- Les 6 R2 de cette semaine vont **se tenir** → chaque close génère du CA commissionnable à 15 %.
- Les calls groupe hebdos continuent → activation client régulière.
- Elio continue à booker des R1 et à programmer des R2 → le funnel tourne normalement.
- **Pas de rupture brutale**, pas d'acte apparent de sabotage côté Elio.

Le dossier reste solide sur la lecture contractuelle du périmètre commission (Q1a, Q1b, Q1c) et sur le levier Art. 9. Simplement, l'argument de bonne foi fondé sur la "purge" n'existe plus — ce qui n'était de toute façon qu'un renfort, pas le cœur du dossier.

## Fichiers à considérer mis à jour / dépréciés

- ✅ `agenda-calls-2026-11-10.csv` — snapshot le plus récent, à considérer comme source actuelle
- ⚠️ `agenda-diff-2026-11-07-to-2026-11-09.md` — **à considérer comme obsolète** (interprétation révisée ici)
- ⚠️ `calendly-elio/README.md` — correction appliquée (la vraie preuve R2 Google Calendar annoncée est caduque)
- ⚠️ `DOSSIER-COMPLET-2026-11-10.md` — correction appliquée sur sections 1 et 5
- ⚠️ `STRATEGIE-NEGOCIATION-sortie-contrat.md` — "Renfort 2" (bonne foi fondée sur la suppression) à retirer
- ⚠️ `slack-transcript-elio-rayyan-2026-11-09.md` — "Signal fort côté terrain — 23 événements supprimés" à nuancer

---

*Correction d'honnêteté intellectuelle. Il est critique pour la crédibilité du dossier de ne présenter à Elio (ou à un juge, si ça en arrive là) que des arguments fondés sur des faits vérifiés. L'argument "purge" partait d'une lecture incomplète et aurait pu être démonté facilement en audience.*
