# Riposte à l'argument "manquements de suivi chiffre par chiffre"

**Argument avancé par Elio** : *"Crème Tech a eu des manquements parce qu'elle n'a pas suivi la data chiffre par chiffre."*

**Lecture juridique** : argument faible, factuellement démontable, qui essaie de renverser la charge pour justifier un refus de paiement. Il faut le désamorcer à froid, avec les clauses du contrat.

---

## 1. Ce que le contrat dit vraiment sur le "suivi"

**Art. 2, obligations du Prestataire — point (vii)** :

> *"Suivi et fourniture de rapports **périodiques** détaillés sur la performance des actions marketing entreprises, avec recommandations d'ajustements **si nécessaire**."*

Trois mots à souligner :

| Mot | Implication |
|---|---|
| **"périodiques"** | Pas en temps réel, pas quotidien. Un reporting mensuel ou bimensuel satisfait l'obligation. |
| **"détaillés sur la performance"** | Rapport agrégé sur les KPI de performance, pas une liste chiffre par chiffre à la ligne. |
| **"si nécessaire"** | Les recommandations d'ajustement ne sont dues que quand elles sont pertinentes. Pas d'obligation d'en produire en permanence. |

**Il n'y a nulle part dans le contrat l'exigence d'un "suivi chiffre par chiffre"**. Cette expression ne figure ni dans l'art. 2, ni dans l'art. 3, ni dans aucun autre. Elio invente une obligation qui n'existe pas.

## 2. Ce que le contrat met explicitement à la charge du CLIENT

**Art. 4, obligations du Client** :

> *(ii) Fournir au Prestataire toutes les informations nécessaires à la bonne exécution du présent Contrat. [...]*
> *(iii) Valider, dans un délai raisonnable, les documents et supports marketing soumis par le Prestataire pour approbation.*
> *(v) Coopérer activement avec le Prestataire en facilitant l'accès aux informations et ressources requises pour l'exécution des prestations.*
> *(vi) Informer immédiatement et sans délai le Prestataire de toute modification de ses besoins ou objectifs marketing.*

**Art. 5.1, dernière phrase** :

> *"Les commissions dues au Prestataire deviennent exigibles à la fin de chaque mois civil, **sur présentation d'un relevé ou d'un reporting des ventes réalisées** durant la période concernée."*

Le verbe est **"présentation"**. Dans la logique juridique française, c'est le Client qui présente ce relevé au Prestataire pour permettre la facturation, pas l'inverse. Elio n'a jamais fourni spontanément de reporting mensuel des ventes depuis le début du contrat.

## 3. Preuves concrètes du suivi qu'on a effectivement fait

Documenté par les snapshots horodatés sur GitHub (branche `claude/quirky-feynman-dgGs0`) :

| Dispositif | Data captée | Fichier |
|---|---|---|
| Meta Ads | 100 856 CHF spend lifetime, 11 232 leads, par campagne / ad / jour | `meta-ads-veginshape/*.csv` |
| Systeme.io | 12 594 contacts, 9 tags, pipeline par étape | `systemeio-contacts-*.csv` |
| ActiveCampaign | 8 841 contacts en miroir | `activecampaign-contacts-*.csv` |
| Wistia VSL | Play rate, engagement, rétention | `wistia-vsl-stats-*.md` |
| A/B opt-in | 50 768 vues sur 6 mois, par variante | Analysé dans `REPONSE-ELIO-*.md` |
| Facturation | 50 transactions, 48 factures + 2 refunds | `transactions-*.csv` |
| Calendly | 19 cancellations tracées avec auteur et raison | `calendly-elio/cancellations-*.csv` |
| Agenda | 3 snapshots datés (07/11, 09/11, 10/11) | `agenda-calls-*.csv` |

Et le document que nous avons préparé pour le call répond chiffre par chiffre aux 9 questions qu'Elio a posées le 29/10. Donc le suivi existe, il est documenté, il est au niveau attendu pour un contrat de performance.

## 4. Ce qu'Elio N'a PAS fait (vrais manquements, côté Client cette fois)

L'argument de la charge inversée se retourne naturellement :

1. **Accès au fichier compta** : demandé formellement le 01/11/2026 (message Slack), pas reçu au 11/11. Le reporting des ventes mensuel attendu par l'art. 5.1 n'a jamais été fourni spontanément. → **Manquement art. 4 (ii) + 4 (v)**.
2. **Setup CAPI Purchase sur Meta** : sans ce setup (qui relève des données serveur du Client), Meta ne peut pas optimiser sur l'achat réel. Le ROAS vrai n'est donc pas mesurable côté Prestataire. → Facteur limitant mis à notre charge alors qu'il dépend d'une action côté Client.
3. **Accès iClosed ou équivalent** : pour pouvoir fermer le reporting sur le taux de close R1 → R2 → vente, il faudrait l'accès à l'outil de closing. Pas donné. → Rend factuellement impossible le suivi "chiffre par chiffre" qu'Elio réclame rétroactivement.
4. **Accès Qonto / Dougs / Stripe** : refusé. Sans accès, impossible de produire un reporting consolidé Prestataire ↔ Client.
5. **Confirmation écrite de la date de notification du préavis** : demandée le 10/11, pas reçue. → **Manquement art. 4 (vi)**.

## 5. Phrasés prêts à ressortir au call

### Si Elio dit *"Vous n'avez pas suivi la data chiffre par chiffre"*

> *"Le contrat ne demande pas un suivi chiffre par chiffre. L'article 2 point vii parle de rapports périodiques sur la performance, avec recommandations si nécessaire. C'est exactement ce que nous avons fait, et le document d'analyse du 10/11 répond point par point à chacune de tes 9 questions avec les chiffres réels du compte. Si tu me dis que c'est insuffisant, dis-moi quel KPI précis tu voulais voir et à quelle fréquence, qu'on acte ça."*

### Si Elio insiste et parle de "manquements au contrat"

> *"Reste-nous précis sur ce que tu reproches, pour qu'on puisse en parler concrètement. Le contrat prévoit une obligation de reporting périodique côté Prestataire (art. 2 vii) et une obligation de coopération côté Client (art. 4 ii et 4 v), notamment pour l'accès aux informations nécessaires. Dans les faits, j'ai demandé par écrit le 01/11 l'accès au fichier compta pour pouvoir émettre les factures de commission mensuelles dans les temps, et je n'ai pas reçu de réponse. Donc si on doit parler de manquements, on parle des deux côtés. Mais je ne crois pas que ce soit le bon angle pour sortir proprement de ce contrat."*

### Si Elio sous-entend qu'il va retenir la commission

> *"La commission 15 % sur le CA encaissé HT, tous canaux confondus, est due en vertu de l'article 5.1. Elle ne dépend pas d'une évaluation subjective de la qualité du suivi, mais du CA réellement encaissé. Si tu as un point de désaccord sur le périmètre, on en discute et on l'acte par écrit. Sur le principe de la commission elle-même, elle est contractuellement acquise."*

## 6. Pourquoi cet argument ne tient pas devant un juge français

Le Code civil et la jurisprudence française sont clairs sur deux points :

1. **Art. 1104 Code civil** : les contrats doivent être exécutés de bonne foi. Inventer rétroactivement une obligation qui n'existe pas au contrat, pour refuser un paiement acquis, est une exécution de mauvaise foi.
2. **Art. 1194 Code civil** : les contrats obligent aux suites que leur donnent l'équité, l'usage et la loi. L'usage dans le marketing à la performance est un reporting mensuel agrégé, pas un suivi chiffre par chiffre en temps réel.
3. **Art. 1353 Code civil** : la charge de la preuve de l'inexécution pèse sur celui qui l'allègue. Elio devrait prouver quel reporting, à quelle fréquence, selon quel format était précisément attendu et n'a pas été fourni. Sans ce standard contractuel écrit, l'argument tombe.

## 7. Risque collatéral et comment le neutraliser

Elio pourrait tenter d'utiliser cet argument de "manquements" comme **justification pour appliquer une réfaction** (c'est-à-dire réduire unilatéralement la commission due). C'est une autre dérive classique.

**À faire pour verrouiller** :

- Garder une trace écrite de la demande d'accès compta du 01/11, non honorée (déjà fait, transcript Slack commité).
- Garder une trace écrite de la demande de confirmation par écrit (notification préavis, périmètre commission, accès compta) qu'on va envoyer à nouveau cette semaine.
- Si Elio avance l'argument "manquements" par écrit (email ou Slack), répondre dans le même canal en reprenant les points de ce doc, pour fixer la trace.

---

*Document stratégique, à usage interne. À faire valider par un avocat en droit commercial avant toute action formelle écrite (mise en demeure, LRAR, action judiciaire).*
