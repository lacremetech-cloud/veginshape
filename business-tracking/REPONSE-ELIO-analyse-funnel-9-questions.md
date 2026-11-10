# Analyse complète funnel VEGINSHAPE — réponses aux 9 questions

> **Document préparé pour le call de la semaine 10/11/2026**
> Prestataire : Crème Tech EI (Rayyân Djeridi) · Client : VEG IN SHAPE COACHING FZCO (Elio Morier)
> Référence contrat : signé le 19/10/2025, art. 5.1 (commission 15 % CA encaissé HT, tous canaux confondus)
> Version du : 2026-11-10

---

## Préambule — sur quoi s'appuie cette analyse

Toutes les réponses ci-dessous s'appuient sur la data réelle que nous avons capturée sur le dispositif VEGINSHAPE :

- **12 594 contacts** Systeme.io exportés (3+ ans d'historique, 9 tags actifs)
- **Compte Meta Ads VEG IN SHAPE** (act_444571528114901, CHF, Europe/Zurich) :
  - Lifetime : **100 856 CHF** dépensés, **11 232 leads** générés (CPL moyen 8,98 CHF)
  - 30 derniers jours : **6 103,91 CHF** / **1 131 leads** / **CPL 5,40 CHF**
- **Wistia VSL "ELIO VSL FINAL V2"** (l67oat8gve) : ~4 000 plays, 57 % play rate, 35 % avg engagement
- **A/B test opt-in actif depuis mai 2026** : 25 384 vues par variante, taux 14,1 % (A) vs 14,5 % (B)
- **50 factures** sur 9 sept → 7 nov 2026 (snapshot facturation)

---

## 1. Opt-in A vs B — qui gagne et pourquoi ?

### Chiffres au 09/11/2026 (test lancé le 19/05/2026)

| Variante | Vues | Conversions | **Taux** |
|---|---:|---:|---:|
| **A** — Page originale | 25 384 | 3 578 | **14,10 %** |
| **B** — Variante | 25 384 | 3 673 | **14,47 %** |

### Verdict statistique

Uplift observé **+0,37 point** (soit **+2,6 %** en relatif).

Avec n = 25 384 par variante et taux de base ~14 %, le **minimum detectable effect à 95 % de confiance** est ~0,6-0,7 point. Le +0,37 point actuel tombe **sous le seuil de significativité** : B est très légèrement devant, mais **ça n'est statistiquement pas prouvé**.

### Pourquoi (hypothèses à valider)

Sans le détail des deux pages, les leviers qui déplacent 1-3 points sur un opt-in VSL sont, par ordre d'impact :
1. **Promesse du titre** (clarté + chiffre + délai > créativité)
2. **Longueur du formulaire** (moins = plus de conversion)
3. **Preuve sociale above the fold** (logo, nombre d'inscrits, mini-témoignages)
4. **Angle émotionnel vs rationnel** (selon la source trafic)
5. **Vitesse mobile** (chaque seconde de chargement = -5 % de conversion)

### Recommandation

- **Ne pas arrêter B comme gagnant maintenant** = parier sur du bruit statistique.
- **Deux options rationnelles** :
  - (a) Laisser tourner → ~2-3 mois pour atteindre la significativité au rythme actuel.
  - (b) Terminer à match nul et **lancer une variante C audacieuse** (changement majeur, pas micro-tweak).
- Pour l'optimisation sérieuse : **option (b)**.

---

## 2. KPI à viser sur ce type de funnel

### Référentiel par étape (coaching VEG panier 3 000-3 500 CHF, FR/CH)

| Étape | KPI | Seuil acceptable | Bon | Excellent | **Actuel VEGINSHAPE** |
|---|---|---:|---:|---:|---:|
| Ad Meta | CTR link | ≥ 1,0 % | 1,8 % | > 2,5 % | **3,18 %** ✅ excellent |
| | CPM | < 25 CHF | < 20 | < 15 | **10,84 CHF** ✅ excellent |
| | CPC link | < 1,50 CHF | < 1,00 | < 0,70 | **0,34 CHF** ✅ excellent |
| Landing | Cost per LPV | < 2 CHF | < 1 | < 0,50 | **0,78 CHF** ✅ excellent |
| | Click → LPV | > 70 % | > 85 % | > 95 % | **44 %** ⚠️ **fuite** |
| | LPV → Lead | 10-15 % | 15-20 % | > 20 % | **14 %** (14,1 - 14,5 A/B) — acceptable, marge |
| VSL | Play rate | 40-50 % | 55-65 % | > 70 % | **57 %** ✅ bon |
| | Avg engagement | 25-30 % | 35-40 % | > 45 % | **35 %** ✅ bon |
| | Rétention à 100 % | 10-15 % | 15-20 % | > 20 % | **~15 %** ✅ bon (601/4000) |
| | CPL pixel | < 12 CHF | < 8 | < 5 | **5,40 CHF** ✅ excellent |
| Pipeline | Opt-in → RDV booké | 10-15 % | 20-25 % | > 30 % | *à mesurer via Systeme.io* |
| | Show rate R1 | 60 % | 70-75 % | > 80 % | *à mesurer* |
| | R1 → vente | 10-15 % | 20-30 % | > 35 % | *à mesurer* |
| Business | CPA (coût par vente) | < 25 % panier | < 20 % | < 15 % | *à mesurer* |
| | **ROAS D28** | ≥ 2 | ≥ 3,5 | ≥ 6 | *à mesurer — pixel ne tracke pas purchase* |

### Les 3 KPI prioritaires à piloter chaque semaine

1. **CPL hebdo** — on est à 5,40 CHF (30j) mais **6,43 CHF sur les 7 derniers jours** = **dégradation en cours**.
2. **CAC** = spend Meta de la semaine / nb de nouveaux clients signés.
3. **ROAS D28** — nécessite setup CAPI Purchase (voir Q3).

### Diagnostic VEGINSHAPE en un paragraphe

**Le haut de funnel est excellent** (CTR 3,18 %, CPM 10,84 CHF, CPC 0,34 CHF, CPL 5,40 CHF — tous dans la bande "excellent"). **Deux fuites à mi-funnel** : (a) 56 % des clicks ne deviennent pas une LPV (bounce / speed / mobile), (b) la LPV ne convertit qu'à ~14 % en lead. **Ce sont les deux points où il reste le plus de potentiel**, pas en ajoutant du budget mais en corrigeant ces deux leaks.

---

## 3. Analyse des pubs Meta actuelles — ground truth

### Compte VEG IN SHAPE (act_444571528114901) — 30 derniers jours

**2 campagnes actives** :

| Campagne | Spend | Leads | **CPL** | Verdict |
|---|---:|---:|---:|---|
| **VSL OCTOBRE 2026 - NEW TUNNEL** | 5 200 CHF | 1 131 | **4,60 CHF** | 💰 Cash cow : tout vient d'ici |
| **PACK 4 - ADS TO FOLLOW - ADS 4 (3 HOOKS)** | 904 CHF | **0** | **N/A** | 🚨 **Morte — 900 CHF gaspillés** |

### 9 ads actives — classement par performance

| Rang | Ad | AdSet | Spend | Leads | **CPL** | CTR link | **LPV→Lead** |
|---|---|---|---:|---:|---:|---:|---:|
| 🥇 | **BATCH 3 [10-13]** | BATCH 3 | **287** | 100 | **2,87** | 2,8 % | **14,5 %** |
| 🥈 | **BATCH 1 [14-17]** | BATCH 4 | 1 191 | **344** | 3,46 | 4,0 % | 11,8 % |
| 🥉 | BATCH 1 [2-5] | BATCH 1 | 1 126 | 260 | 4,33 | 2,7 % | 12,4 % |
| 4 | BATCH 1 [18-20] | BATCH 5 | 289 | 59 | 4,90 | 3,5 % | 9,3 % |
| 5 | BATCH 1 [6-9] | BATCH 2 | 1 124 | 212 | 5,30 | 2,9 % | 11,9 % |
| 6 | BATCH SUISSE | SUISSE | 1 182 | 156 | **7,57** ⚠️ | 3,1 % | 11,4 % |
| ❌ | ADS 4 HOOK 1 | PACK 4 | **836** | **0** | — | 3,1 % | **0 %** |
| ❌ | ADS 4 HOOK 3 | PACK 4 | 43 | 0 | — | 4,3 % | 0 % |
| ❌ | ADS 4 HOOK 2 | PACK 4 | 25 | 0 | — | 3,5 % | 0 % |

### Les 3 top performers — pourquoi ils marchent

1. **BATCH 3 [10-13]** — CPL **2,87 CHF** + taux LPV→Lead **14,5 %** (le meilleur du compte). C'est le **meilleur match hook ↔ offre** actuel. Signal clair qu'il y a dans cette créa un angle qui résonne mieux que les autres. **À copier** dans les prochaines variantes.
2. **BATCH 1 [14-17]** — meilleur **volume** (344 leads) et meilleur CTR link (4 %). C'est le workhorse.
3. **BATCH 1 [2-5]** — solide fiabilité, bon taux LPV→Lead (12,4 %).

### Les 3 pires — pourquoi elles ne marchent pas

- **PACK 4 "ADS TO FOLLOW"** (toutes les 3) — nom qui suggère du **retargeting**. CTR link correct (3-4 %) mais **taux LPV→Lead = 0 %**. Diagnostic : la landing ne convertit pas ce trafic retargeté. Soit la landing affiche une offre différente de celle de l'ad, soit le retargeting touche les mauvais segments (cold vs warm non filtré), soit l'offre affichée n'est pas celle attendue par qui revoit l'ad.
- **ADS 4 HOOK 1 seule** a brûlé **836 CHF en 30j pour 0 lead**, et continue à tourner à **~200 CHF/semaine** aujourd'hui. **À couper dans l'heure.**

### BATCH SUISSE — cas particulier

CPL **7,57 CHF** sur 30j, **11,95 CHF** sur 7j = en dégradation rapide. Marché Suisse = CPM structurellement plus cher, mais la dégradation récente dépasse ça. À auditer :
- Ciblage trop large ?
- Créa pas assez "locale" (pas de francs suisses visibles, pas de référence locale) ?
- Pricing exprimé correctement pour une audience CH ?

### KPI VEGINSHAPE vs benchmarks (récap)

✅ **Excellent** : CTR link, CPM, CPC, Cost per LPV, CPL
⚠️ **À améliorer** : Click → LPV (44 % seulement) et LPV → Lead (14 % seulement)

**Deux fast wins** : (1) audit vitesse + mobile de la landing (gain potentiel +20 % de leads sur même budget), (2) nouvelle variante C d'opt-in (changement majeur, pas micro-tweak).

---

## 4. Quelles stats viser sur les ads

Référentiel Meta pour ce funnel VEGINSHAPE (France/Suisse, panier 3 000-3 500 CHF) :

| Métrique | Seuil minimum (survie) | Objectif (scale) | Signal top performer | **VEG IN SHAPE actuel** |
|---|---:|---:|---:|---:|
| Thumbstop | 25 % | 40 % | > 50 % | *data video à puller séparément* |
| CTR link | 1,0 % | 1,8 % | > 2,5 % | **3,18 %** ✅ |
| CPC link | < 1,50 CHF | < 1,00 | < 0,70 | **0,34 CHF** ✅ |
| CPM | < 25 CHF | < 20 | < 15 | **10,84 CHF** ✅ |
| CPL opt-in | < 20 CHF | < 12 | < 8 | **5,40 CHF** ✅ |
| Taux lead / LPV | > 10 % | > 15 % | > 20 % | **~14 %** ⚠️ |
| Coût par RDV | < 60 CHF | < 40 | < 25 | *à chiffrer avec data Systeme.io* |
| **Coût par vente** | < 500 CHF | < 350 | < 250 | *pixel ne track pas purchase* |
| **ROAS D7** | > 1,5 | > 2,5 | > 4 | *à chiffrer* |
| **ROAS D28** | > 2,0 | > 3,5 | > 6 | *à chiffrer* |

**Ces seuils s'appliquent par ad, pas globalement**. Le compte peut avoir un bon CPL global tout en contenant des ads winners et des ads à zéro conversion (voir PACK 4 ci-dessus).

---

## 5. Winner / loser : à quel moment cut ?

### Framework de décision

Base : CAC cible ≈ 25 % du panier moyen. Pour VEGINSHAPE (panier ~3 000 CHF), **CAC cible ≈ 750 CHF**.

| Seuil de dépense atteint | Décision |
|---|---|
| **< 1× CAC cible** (< 750 CHF) | Laisser tourner — pas assez de signal statistique |
| **1× à 2× CAC** (750-1 500 CHF) | Checker amont : si thumbstop < 25 % OU CTR link < 0,8 % → **cut**. Sinon, continuer. |
| **2× à 3× CAC** (1 500-2 250 CHF) | Checker CPL : si CPL > 2× seuil → **cut**. Sinon, continuer. |
| **3× CAC** (≥ 2 250 CHF) | **Décision finale** : 0 vente ET CPL > seuil → **cut sans appel**. 1 vente et ROAS D7 > 1,5 → **garder et scale**. |
| **5× CAC** (≥ 3 750 CHF) | 0 vente à ce stade = **cut absolu**, peu importe les métriques amont. |

### Signaux de kill immédiat (avant 1× CAC)

- Thumbstop < 15 % sur 1 000 impressions = hook cassé.
- Freq ≥ 3 avec CPM +30 % vs lancement = fatigue d'audience.
- CTR link divisé par 2 vs 48 h après lancement = saturation ou saison hostile.

### Signaux de scale (sur 7 jours de stabilité)

- CPL < 60 % du seuil, consistant 5+ jours.
- ROAS D7 > 3 sur budget quotidien stable.
- Freq < 2, CPM stable.
- **→ Dupliquer** (pas augmenter budget — ça casse l'algo), en gardant la créa et en variant audience / placement.

### Exemple vivant du compte

- **ADS 4 HOOK 1 (PACK 4)** aurait dû être cut **autour de 1 500 CHF de spend** (seuil 2× CAC) quand il devenait clair que taux LPV→Lead = 0 %. Au lieu de ça, il a passé 836 CHF supplémentaires = **cut non appliqué**.
- **BATCH 3 [10-13]** coche tous les signaux de scale (CPL 60 % sous seuil, taux LPV→Lead meilleur du compte). Il **devrait** être scalé ×4 immédiatement.

---

## 6. Lancement des ads, batch, logique Andromeda

Andromeda = moteur de ranking Meta (lancé 2024) qui optimise mieux quand il a plus de signaux à ingérer.

### a) Toujours lancer en batch (3-5 variantes minimum par angle)

- **1 seule créa lancée** = Andromeda n'a rien à comparer, perf artificiellement basse.
- **3-5 variantes par angle** = Andromeda identifie le gagnant en 48-72h et alloue dessus.
- **Jamais** moins de 3 ads par ad set.

### b) Advantage+ > ABO sauf retargeting

- Acquisition froide → **Advantage+ Shopping Campaign (ASC)** ou Advantage+ Audience.
- Retargeting warm → **ABO manuel** (contrôle des audiences chaudes).
- **Attention** : c'est ce qui semble avoir mal tourné sur PACK 4 — si l'intention était du retargeting, il devrait être en ABO avec un sous-ensemble warm précis, pas en Advantage+.

### c) Protocole de lancement recommandé

| Phase | Timing | Action |
|---|---|---|
| **S0** — préparation | — | Choisir 3 angles principaux (ex : mythe débunk + témoignage + déclaration face camera). |
| S0 | — | Pour chaque angle : produire **5 variantes** (3 hooks × 2 B-roll + 1 statique) = 15 créas. |
| **S1** — launch | J+0 | 1 ASC avec les 15 ads, budget 100-150 CHF/jour → Andromeda alloue. |
| | J+3 | Couper les ads avec thumbstop < 20 % ou CTR link < 0,7 % (keeper ~10/15). |
| | J+7 | Classement par ROAS D7 → garder 3-5 top, couper le reste. |
| | J+14 | **Scale** les top (dupliquer vers lookalikes), lancer un nouveau batch sur l'ASC existant. |

### d) Rythme de renouvellement

- Chaque ad a **14-30 jours de vie utile** avant fatigue.
- Objectif : **3-5 nouvelles ads par semaine**, kill 3-5 par semaine. **Rotation continue**.
- **Diagnostic VEGINSHAPE sur ce point** : le batch OCTOBRE est en place depuis 30-45 jours, aucun nouveau test n'a abouti depuis (PACK 4 raté). Le compte entre en **fatigue créative** → d'où la dégradation CPL +19 % cette semaine.

---

## 7. Recommandations budget ads — prochains 3 mois

### Baseline actuelle

- Spend 30j : **6 103,91 CHF** (soit ~200 CHF/jour en moyenne)
- Leads 30j : 1 131
- Si taux booking lead → R1 ≈ 25 %, show rate ≈ 70 %, close R1 ≈ 20 %, panier 3 000 CHF → **~119 ventes théoriques/mois ≈ 357 k CHF de CA potentiel** (hypothèses prudentes, à affiner avec data réelle Systeme.io)

### Scénarios 3 mois

| Scénario | Spend Meta/mois | Leads attendus | CA attendu (ROAS ~3) | Commission 15 % |
|---|---:|---:|---:|---:|
| **Status quo** | 6 100 CHF | ~1 130 | ~18 300 CHF | **2 745 CHF** |
| **Nettoyage (cut PACK 4)** | 6 100 CHF (même spend, mieux alloué) | **~1 445** (+28 %) | ~23 400 CHF | **3 510 CHF** |
| **Scale modéré** (+50 %) | 9 150 CHF | ~1 850 | ~27 500 CHF | **4 125 CHF** |
| **Scale agressif** (+150 %) | 15 250 CHF | ~2 700 (ROAS 2,4) | ~36 600 CHF | **5 490 CHF** |
| **Défensif** (-50 %) | 3 050 CHF | ~630 (ROAS 3,4) | ~10 400 CHF | **1 560 CHF** |

> ROAS projetés tiennent compte de la **dégradation naturelle liée au scale** (saturation audience, CPM en hausse, dilution qualité trafic).

### Recommandations concrètes

1. **Avant tout scale** : faire le **nettoyage** décrit en Q3 (cut PACK 4, scale BATCH 3). C'est **gratuit** et ça augmente le volume de 28 % sans ajouter un CHF.
2. **Budget 3 mois sûr** : garder 6 000 CHF/mois **après nettoyage** + 1 500 CHF/mois pour **tester un nouvel angle** par mois (batch Octobre V2 ce mois-ci).
3. **Avant le préavis (22/11)** : ne pas lancer de batch coûteux dont les retombées seraient post-22/11 (zone non commissionnable sans avenant écrit).
4. **Post-22/11 (si Elio continue sans nous)** : il risque **-20 à -40 % de ROAS les 2-3 premiers mois** (perte du pilotage, pas de refresh créa, pas d'A/B optimisation). À prendre en compte dans son plan — c'est la valeur réelle qu'apporte la gestion active du compte.

---

## 8. Rédaction d'ads — encore valable ?

### Lecture contractuelle

Comme rappelé dans le message Slack du 01/11 : **non**, dans le contexte d'une sortie au 22/11.

### Pourquoi

- Production d'un batch d'ads (3-5 variantes × 1 angle) = 1-2 semaines + 2 semaines de learning Meta → **retombées mesurables à 4-6 semaines**.
- Toutes ces retombées tombent **après le 22/11** = zone non commissionnée Crème Tech.
- Modèle contractuel art. 5.1 = "setup gratuit, rémunération à la performance sur la durée" + art. 9 = "livrables = propriété Crème Tech jusqu'au paiement complet". Dans un contexte de sortie, **la durée disparait** → le modèle ne tient plus.

### Alternatives

| Option | Scope | Chiffrage |
|---|---|---|
| **Forfait batch unique** | 1 angle × 5 variantes (5 ads) | À chiffrer |
| **Forfait batch complet** | 3 angles × 5 variantes (15 ads) + setup ASC | À chiffrer |
| **Avenant commission étendue** | On continue le modèle actuel + commission 15 % maintenue 6 mois après sortie, sur CA attribuable au dispositif | À discuter |

Sans forfait ou avenant écrit, la logique du setup gratuit ne peut plus tenir.

---

## 9. Rédaction de VSL — encore valable ?

**Même logique que Q8, encore plus marquée** : une VSL est un livrable lourd (2-4 semaines script + tournage + montage + A/B hook + validation) **+ 1-3 mois d'optimisation** avant plein potentiel. Retombées **intégralement post-préavis**.

### Alternatives

| Option | Scope | Chiffrage |
|---|---|---|
| **Forfait VSL complète** | Script + tournage + montage + 3 variantes hook + intégration | À chiffrer |
| **Forfait VSL light** | Re-cut VSL actuelle + nouveau hook + nouvelle CTA (1-2 semaines) | À chiffrer |
| **Avenant commission étendue** | Comme Q8 | À discuter |

Le constat objectif : la VSL actuelle (`l67oat8gve`, ELIO VSL FINAL V2) **performe bien** (play rate 57 %, engagement 35 %, rétention 100 % ~15 %). **Elle n'a pas besoin d'être refaite dans l'immédiat**. Priorité : les ads (voir Q3) et la landing (fuite click → LPV).

---

## Récap & prochaines étapes

### Décisions actionnables **cette semaine** (sans toucher au contrat)

| Action | Urgence | Impact |
|---|---|---|
| **Cut ADS 4 HOOK 1/2/3 (PACK 4)** | Aujourd'hui | +900 CHF/mois réalloués |
| **×4 budget BATCH 3 [10-13]** | Aujourd'hui | +300 leads/mois au CPL 2,87 CHF |
| **Audit landing** vitesse + mobile | Cette semaine | +20 % de LPV |
| **Lancer OPTIN C** (variante majeure, pas tweak) | Cette semaine | +3-5 points sur taux LPV→Lead |
| **Setup CAPI Purchase** | 2 semaines | Débloque optimisation Meta sur achat, +20-40 % ROAS |

### Demandes à Elio (à faire au call)

1. **Date exacte de notification du préavis** (pour calculer les 30 jours au jour près).
2. **Confirmation écrite du périmètre commission** (toutes mensualités de plans signés ≤ 22/11 + tous RDV R1/R2/R3 bookés ≤ 22/11 qui closent après restent commissionnés ; nouvelle acquisition post-22/11 hors périmètre).
3. **Accès au fichier compta** (Qonto / Dougs / Stripe) — demandé 01/11, non reçu.
4. **Snapshot gelé du pipeline au 22/11 23:59** : état Systeme.io (tags Client, RDV booké, Prospects iClosed), plans en cours, Calendly à venir — pour base contractuelle commune.

### Si Elio veut malgré tout prolonger la prestation

- **Devis forfaitaire** pour ads neuves ou VSL neuve (à chiffrer selon scope).
- **OU avenant écrit** maintenant la commission 15 % sur 6 mois post-sortie, sur CA attribuable au dispositif.
- Sans l'un ou l'autre : on reste sur ce qui est fait.

---

*Document interne Crème Tech — à présenter au call avec Elio. Chiffres issus du compte Meta Ads VEG IN SHAPE (act_444571528114901), Systeme.io, Wistia et facturation Veginshape (snapshots 2026-11-07 → 2026-11-10).*
