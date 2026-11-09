# Analyse complète funnel VEGINSHAPE — réponse aux 9 questions

> Document préparé pour le call de la semaine 10/11/2026.
> **Prestataire** : Crème Tech EI (Rayyân Djeridi) · **Client** : VEG IN SHAPE COACHING FZCO (Elio Morier)
> **Référence contrat** : signé le 19/10/2025, art. 5.1 (commission 15% CA encaissé HT, tous canaux confondus).

---

## Préambule

Les réponses ci-dessous s'appuient sur les snapshots de data réels que nous avons capturés sur le dispositif VEGINSHAPE au 09/11/2026 :

- **12 594 contacts** Systeme.io exportés (3+ ans d'historique, 9 tags actifs)
- **~4 000 plays** sur la VSL Wistia `ELIO VSL FINAL V2` (`l67oat8gve`), **57% play rate**, **35% engagement moyen**
- **8 841 contacts** ActiveCampaign (base historique)
- **50 factures + 2 remboursements** sur 9 sept → 7 nov 2026
- **A/B test opt-in** en cours depuis mai 2026 (25 384 vues par variante)
- **19 cancellations Calendly** sur les 18 derniers jours — dont 6 par Elio lui-même avec raison "Test"/"Doublon"

Certaines réponses demandent de la data supplémentaire (Meta Ads Manager notamment) que nous n'avons pas encore été autorisés à exporter — nous le signalons à chaque fois.

---

## 1. Optin A et B — résultats actuels, lequel fonctionne mieux, pourquoi ?

### Les chiffres bruts (A/B en cours depuis le 19 mai 2026, soit ~5,5 mois)

| Variante | Vues | Conversions | Taux |
|---|---:|---:|---:|
| **A** — Page originale "OPTIN A VSL MAI 2026" | 25 384 | 3 578 | **14,1 %** |
| **B** — Variante "OPTIN B VSL MAI 2026" | 25 384 | 3 673 | **14,5 %** |

### Lecture

**Uplift observé : +0,4 point (soit +2,8 % en relatif pour B).**

- Sample size énorme : ~25 k par variante, bien au-delà du seuil minimum.
- MAIS **l'écart n'est PAS statistiquement significatif à 95 %** sur ces chiffres : avec un baseline à 14,1 % et n = 25 384, le MDE à 95 % est ~0,6-0,7 point. Le +0,4 point de B tombe sous ce seuil.
- Verdict : **B est très légèrement devant, mais rien ne prouve que ce soit un vrai gagnant**. Si on arrête maintenant et qu'on bascule tout sur B, on parie sur du bruit.

### Pourquoi (hypothèses — à valider par les versions)

Sans accès aux deux pages je parle en général : pour un opt-in VSL, les leviers qui déplacent le taux de 1-3 points sont :

1. **Promesse du titre** (clarté > créativité) — ex : chiffre + délai + bénéfice.
2. **Longueur du formulaire** — moins de champs = plus de conversion (mais lead moins qualifié).
3. **Preuve sociale "above the fold"** (logo clients, nombre d'inscrits, témoignages courts).
4. **Angle émotionnel vs rationnel** — selon le trafic source.
5. **Chargement mobile** — chaque seconde = ~5 % conversion perdue.

### Recommandation

- **Arrêter le test B comme "gagnant" prématurément serait une erreur**. Deux options rationnelles :
  - a) Laisser tourner jusqu'à ce que l'écart passe la significativité (ou s'évapore) → ~2-3 mois supplémentaires au rythme actuel de trafic.
  - b) Terminer le test à match nul et lancer une **nouvelle variante C plus audacieuse** (pas des micro-tweaks) pour chercher un vrai uplift.
- Si l'objectif est l'optimisation sérieuse : **option b**, en testant un changement majeur (nouvelle headline + nouveau flow) plutôt que des détails.

---

## 2. Quelles stat / KPI viser sur un funnel de ce type (clic, conversion, …) ?

### Référentiel benchmarks pour un funnel VSL coaching haut panier (2 500-3 500 € HT)

| Étape | KPI | Benchmark acceptable | Benchmark bon | Benchmark excellent |
|---|---|---:|---:|---:|
| **Ad Meta** | CTR (link click) | ≥ 1,0 % | 1,5 - 2,5 % | > 3 % |
| | CPM | < 25 € (FR) | 15-20 € | < 15 € |
| | CPC | < 1,50 € | 0,80 - 1,20 € | < 0,70 € |
| | Thumbstop (vues 3s / impressions) | > 30 % | 40-50 % | > 55 % |
| **Landing opt-in** | Taux de conversion visiteur → email | 10-15 % | 15-20 % | > 20 % |
| | **(Actuel VEGINSHAPE : 14,1 - 14,5 %)** | ✅ Acceptable | | |
| **VSL** | Play rate | 40-50 % | 55-65 % | > 70 % |
| | **(Actuel : 57 % — ✅ dans le "bon")** | | | |
| | Engagement moyen | 25-30 % | 35-40 % | > 45 % |
| | **(Actuel : 35 % — ✅ dans le "bon")** | | | |
| | Rétention à 25 % de vidéo | > 60 % | > 70 % | > 80 % |
| | Rétention à 100 % | 10-15 % | 15-20 % | > 20 % |
| | **(Actuel : 601 watches / 4 000 plays à 11:50 = 15 % — ✅ bon)** | | | |
| **Opt-in → RDV booké** | Conversion opt-in → booking | 10-15 % | 20-25 % | > 30 % |
| **RDV booké → show rate** | % présents au R1 | 60 % | 70-75 % | > 80 % |
| **R1 → vente** | Close rate R1 | 10-15 % | 20-30 % | > 35 % |
| **R1 → R2 → vente** | Close cumulé | 20-25 % | 30-40 % | > 45 % |
| **Funnel complet** | Coût par acquisition client | ≤ panier moyen × 25 % | ≤ 20 % | ≤ 15 % |
| | LTV / CAC | ≥ 3 | ≥ 5 | ≥ 8 |
| | ROAS (CA / spend ads) | ≥ 2 | ≥ 3 | ≥ 5 |

### Lecture pour VEGINSHAPE au 09/11/2026

- Opt-in 14,1-14,5 % : **acceptable**, pas excellent. Marge sur la landing.
- VSL play rate 57 % : **bon**.
- VSL engagement 35 % : **bon** mais pas exceptionnel pour une VSL de 12 min.
- Rétention à 100 % 15 % : **bon** (indique que la VSL tient le spectateur jusqu'au CTA final).
- **Les chiffres aval (opt-in → booking, booking → close, LTV, ROAS) nécessitent l'accès au CRM + Meta Ads Manager pour être calculés précisément** — on les a partiellement via Systeme.io et les factures, mais il manque le lien exact spend-ads ↔ vente.

### Les 3 KPI prioritaires à piloter chaque semaine

1. **CAC (coût d'acquisition client)** = spend Meta de la semaine / nb de nouveaux clients signés.
2. **ROAS** = CA encaissé de la semaine attribuable au funnel / spend Meta.
3. **Taux de show R1** — c'est le plus souvent la fuite majeure d'un funnel VSL+R1.

---

## 3. Analyse des pubs Meta actuelles — lesquelles fonctionnent le mieux, pourquoi, KPI ?

**⚠️ Nous n'avons pas accès à Meta Ads Manager pour l'instant.** Nous demandons l'accès (viewer suffit) pour produire l'analyse chiffrée. En attendant, voici la méthodologie que nous appliquons normalement :

### Grille d'analyse par ad

| Dimension | Métrique | Seuil d'alerte |
|---|---|---|
| **Attention** | Thumbstop (3s views / impressions) | < 25 % → hook faible |
| **Qualité du clic** | CTR link | < 0,8 % → promesse inefficace |
| **Coût trafic** | CPC | > 1,80 € → ciblage ou créa à revoir |
| **Qualification** | Taux opt-in post-click | < 10 % → mismatch message/landing |
| **Fond du funnel** | CPL (coût par lead) | > 15 € sur ce panier → non-tenable |
| **Vente** | CPA (coût par vente) | > 25 % panier → non-rentable |

### Top performers typiques dans ce type de niche (coaching VEG)

- **Ads témoignage client** (UGC 30-45 sec) = souvent le top ROAS
- **Ads "mythe débunk"** sur les protéines végétales / perte de poids vegan
- **Ads "déclaration d'intention"** (Elio face camera parlant d'une erreur commune)
- **Ads carrousel "avant/après"** + CTA → opt-in direct (bypass VSL pour segments froids)

### Ce qu'on produira dès accès Meta accordé

1. Classement de toutes les ads actives par ROAS 7j / 14j / 28j
2. Analyse par angle, hook, format (statique / vidéo / UGC / carrousel)
3. Carte de chaleur **thumbstop × CTR × CPL** pour identifier les 3 segments (top / mid / bottom)
4. Recommandations d'arrêt / de scale / de dupliquement par ad

---

## 4. Quelles stats viser sur les ads ?

Référentiel Meta pour ce funnel (France / Suisse / Belgique, panier 2 500-3 500 €) :

| Métrique | Seuil minimum (survie) | Objectif (scale) | Signal de top performer |
|---|---:|---:|---:|
| Thumbstop | 25 % | 40 % | > 50 % |
| CTR link | 1,0 % | 1,8 % | > 2,5 % |
| CPC | < 1,50 € | < 1,00 € | < 0,70 € |
| CPM | < 25 € | < 20 € | < 15 € |
| CPL (coût lead opt-in) | < 20 € | < 12 € | < 8 € |
| Taux de prise de RDV / lead | > 15 % | > 25 % | > 35 % |
| Coût par RDV | < 60 € | < 40 € | < 25 € |
| **Coût par vente** | < 500 € | < 350 € | < 250 € |
| **ROAS D7** | > 1,5 | > 2,5 | > 4 |
| **ROAS D28** | > 2,0 | > 3,5 | > 6 |

À appliquer **par ad**, pas globalement : une audience peut avoir un bon ROAS global mais contenir 3 ads winners et 7 losers à couper.

---

## 5. Winner / loser : à quel moment cut une ad ?

### Framework de décision (à appliquer dès qu'une ad a dépensé un minimum de data)

| Seuil de dépense | Décision à prendre |
|---|---|
| **< 1× CAC cible** (ex : < 250 €) | **Laisser tourner** — pas assez de signal statistique |
| **1× à 2× CAC cible** (250-500 €) | Checker les métriques amont : si thumbstop < 25 % OU CTR < 0,8 % → **cut**. Sinon, continuer. |
| **2× à 3× CAC cible** (500-750 €) | Checker CPL : si CPL > 2× seuil → **cut**. Sinon, continuer. |
| **3× CAC cible** (750 €) | **Décision finale** : si pas de vente ET CPL > seuil → **cut sans appel**. Si 1 vente et ROAS > 1,5 → **garder et scale**. |
| **5× CAC cible** (1 250 €) | **Si 0 vente à ce stade = cut absolu**, peu importe les métriques amont. |

### Signaux de kill immédiat (avant 1× CAC)

- Thumbstop < 15 % sur 1 000+ impressions = hook cassé, pas la peine d'attendre.
- Freq ≥ 3 avec CPM en hausse de > 30 % vs lancement = fatigue d'audience, kill ou refresh créa.
- CTR qui s'effondre (-50 % vs 48h après lancement) = audience saturée ou saison hostile.

### Signaux de **scale** (à valider sur 7 jours de stabilité)

- CPL < 60 % du seuil, consistant 5+ jours
- ROAS D7 > 3 sur budget quotidien stable
- Freq < 2, CPM stable

Dans ce cas : **dupliquer** l'ad (pas juste augmenter budget — ça casse l'algo) en gardant la créa et en variant audience / placement.

---

## 6. Lancement des ads, batch, logique avec Andromeda

Andromeda = moteur de ranking de Meta (lancé 2024) qui favorise les placements où l'IA a le plus de signaux. Deux conséquences majeures :

### a) **Toujours lancer en batch** (3-5 variantes minimum par angle)

- 1 seul creative lancé = Andromeda n'a pas de quoi apprendre et distribue mal. Résultat : perf artificiellement basse.
- 3-5 variantes par angle = Andromeda alloue sur la meilleure et donne du volume au gagnant rapidement (en 48-72h).
- **Jamais** moins de 3 ads par ad set.

### b) **Advantage+ > ABO** sauf cas précis

- Pour l'acquisition froide : **Advantage+ Shopping Campaign (ASC)** ou Advantage+ Audience → laisser l'IA Meta décider.
- Pour le retargeting : garder **ABO manuel** (meilleur contrôle des audiences chaudes).

### c) Protocole de lancement recommandé (batch testing)

1. **Semaine 0 — préparation** : choisir 3 angles principaux (ex : mythe débunk + témoignage + déclaration Elio).
2. Pour chaque angle : produire **5 variantes** = 3 hooks différents × 2 B-roll + 1 statique.
3. **Semaine 1 — launch** : 1 ASC avec les 15 ads, budget quotidien 100-150 € → laisser Andromeda allouer.
4. **J+3** : couper les ads avec thumbstop < 20 % ou CTR < 0,7 % (keeper ~10/15).
5. **J+7** : classement par ROAS D7 → garder les 3-5 top, couper le reste.
6. **J+14** : scale les top ads (dupliquer vers audiences similaires) et relancer un nouveau batch d'angles sur l'ASC initial.

### d) Rythme de renouvellement des créas

- Chaque ad a une **durée de vie utile de 14-30 jours** avant fatigue créative.
- Objectif : **sortir 3-5 nouvelles ads par semaine**, kill 3-5 par semaine. Rotation continue.
- Dans ce cadre, la question n'est pas "a-t-on besoin d'une nouvelle VSL ou pas", c'est **a-t-on besoin de nouvelles ads qui pointent vers une VSL existante ou nouvelle**. Priorité absolue : les ads.

---

## 7. Recommandations sur le budget ads pour les prochains mois

### Hypothèse de départ

Si le ROAS actuel est à ~3 (CA encaissé mensuel / spend Meta) :
- Chaque 1 € investi en ads = 3 € de CA encaissé HT.
- Dans ce cas, **doubler le budget** augmente le CA de ~80 % (l'efficacité marginale décroit avec le volume).

### Scénarios proposés

| Scénario | Spend Meta mensuel | CA mensuel attendu (ROAS 3) | Commission 15 % (si contrat renouvelé) |
|---|---:|---:|---:|
| Status quo | 10 000 € | 30 000 € | 4 500 € |
| Scale modéré (+50 %) | 15 000 € | ~40 000 € (ROAS 2,7) | 6 000 € |
| Scale agressif (+150 %) | 25 000 € | ~60 000 € (ROAS 2,4) | 9 000 € |
| Réduction défensive (-50 %) | 5 000 € | ~17 000 € (ROAS 3,4) | 2 550 € |

**Les ROAS projetés tiennent compte de la dégradation naturelle liée au scale** (saturation d'audience, augmentation CPM, dilution qualité trafic).

### Recommandations concrètes

1. **Avant tout scale** : nettoyer la stack d'ads en gardant uniquement les 5 top performers par angle. Beaucoup de budget se gaspille sur des ads mortes-vivantes.
2. **Budget 3 mois "sûr"** : garder le niveau actuel + 1 000-2 000 € par mois pour tester un angle nouveau par mois.
3. **Avant le préavis** : ne pas lancer de nouveau batch coûteux dont les retombées seraient post-22/11 (pour Elio comme pour nous, c'est de l'argent qui ne reviendrait pas en pipe commissionnable).
4. **Post-22/11 (si Elio continue sans nous)** : il risque une décroissance 20-40 % du ROAS les 2-3 premiers mois (perte du pilotage, pas de refresh créa, pas d'A/B optimisation). À considérer dans son plan.

---

## 8. Rédaction d'ads — encore valable ?

### Lecture contractuelle

Rappelée dans notre message Slack du 01/11 : **non**, dans le contexte d'une sortie au 22/11.

### Pourquoi

- Production d'un batch d'ads (3-5 variantes × 1 angle) = 1 à 2 semaines + 2 semaines de learning phase Meta = **retombées mesurables à 4-6 semaines**.
- Toutes ces retombées tombent **après le 22/11** = zone non-commissionnée pour Crème Tech.
- Le modèle contractuel est "setup gratuit, rémunération à la performance sur la durée" (art. 5.1 + art. 9). Dans un contexte de sortie, la durée disparait → le modèle ne tient plus.

### Alternative proposée

- **Devis forfaitaire** pour une batch d'ads (angle + 5 variantes) : à chiffrer selon le scope exact souhaité.
- Idem pour une nouvelle VSL (voir Q9).

### Si tu veux qu'on continue malgré tout en perf

- La seule logique acceptable serait un **avenant écrit** qui prolonge la commission 15 % **sur tout CA encaissé jusqu'à 6 mois après la sortie**, sur les plans signés et sur l'attribution de performance des assets nouveaux.
- Sans cet avenant, on reste sur : setup payé fixe en amont, ou pas de setup.

---

## 9. Rédaction de VSL — encore valable ?

**Même logique que Q8, mais encore plus marquée** : une VSL c'est un livrable lourd (2-4 semaines minimum entre script, tournage, montage, A/B test de hook, validation) + **1-3 mois d'optimisation** avant d'atteindre son plein potentiel. Les retombées sont intégralement post-préavis.

### Ce qu'on propose

- **Devis forfaitaire VSL complète** (script + tournage + montage + 3 variantes hook + intégration) → à chiffrer.
- Ou une **nouvelle itération** de la VSL actuelle (re-cut, nouveau hook, nouvelle CTA) → plus court, 1 à 2 semaines, forfait plus léger.

### Ce qu'il ne faut PAS faire

- Repartir sur un chantier de 1 mois+ dans l'inconnu commercial. Soit avec un cadre forfaitaire clair, soit pas du tout.

---

## Récap & prochaines étapes

### Ce qui est actionnable en call

| Point | Statut | Décision à prendre au call |
|---|---|---|
| A/B opt-in A vs B | Pas de gagnant stat. sig. | Laisser tourner ou tenter variante C |
| KPI pilotage hebdo | Référentiel donné | Mettre en place dashboard partagé (Looker / Metabase) |
| Analyse ads détaillée | **Bloqué par accès Meta** | Elio nous accorde-t-il l'accès viewer Meta Ads ? |
| Cut criteria ads | Framework donné | Appliquer à la stack actuelle (nettoyage) |
| Logique batch Andromeda | Protocole donné | Elio applique en interne ou on produit (devis) |
| Budget 3 mois | 4 scénarios donnés | Elio choisit scénario |
| Production ads neuves | Devis forfaitaire proposé | Scope + prix à chiffrer |
| Production VSL neuve | Devis forfaitaire proposé | Scope + prix à chiffrer |

### Ce dont on a besoin de ta part

1. **Accès viewer Meta Ads Manager** (compte VEGINSHAPE) pour chiffrer la Q3.
2. **Accès au fichier compta** (Qonto / Dougs / Stripe / export mensuel) — déjà demandé le 01/11, non reçu.
3. **Confirmation par écrit** de la date exacte de la notification du préavis (pour calculer les 30 jours au jour près).
4. **Confirmation par écrit** du périmètre de la commission comme discuté (toutes les mensualités à venir sur plans signés ≤ 22/11 + tous les RDV bookés ≤ 22/11 qui closent après restent commissionnés ; nouvelle acquisition post-22/11 hors périmètre).

---

*Document interne Crème Tech — à partager avec Elio au call. Version du 09/11/2026.*
