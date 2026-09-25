# Demandes de devis : audit, HSM, hébergement

**Modèles de demande et grille de comparaison pour établir le budget pluriannuel**

!!! note "Statut du document"
    Guide de travail. Les prestataires d'audit, les fabricants de HSM et les hébergeurs ne publient pas leurs tarifs : le [budget du livre blanc (§ 5.5)](../livre-blanc/index.md#55-structure-de-couts-et-garanties) ne contient donc **aucun montant** tant que des devis comparés n'ont pas été obtenus. Aucune demande n'a encore été envoyée.

---

## 1. Principes

1. **Trois devis au moins par poste**, pour que la comparaison soit défendable auprès des financeurs.
2. **Demander des fourchettes chiffrées et les hypothèses qui les fondent**, pas seulement un accord de principe.
3. **Écrire au nom de l'initiative**, tant que l'association n'est pas déclarée, avec l'adresse de rôle `contact@otspi.org`. Ne jamais indiquer d'adresse personnelle.
4. **Ne rien engager.** Toute demande précise qu'il s'agit d'une étude de coûts sans engagement d'achat.
5. **Publier les montants retenus**, avec leur date et leur source, dans le budget pluriannuel, sans divulguer les conditions commerciales confidentielles d'un prestataire sans son accord.

## 2. Informations communes à joindre

| Élément | Formulation |
|---|---|
| Porteur | Open Trusted Service Provider Initiative (OTSPI), initiative d'intérêt général en cours de constitution sous forme d'association loi 1901 |
| Projet | Prestataire de services de confiance ouvert : horodatage électronique qualifié (RFC 3161, ETSI EN 319 421 et 319 422) en premier service, puis autorité de certification TLS, cachet, signature et identité |
| Documentation | [Livre blanc](https://about.otspi.org/livre-blanc/) et [site](https://www.otspi.org/) |
| Statut | Aucune qualification demandée à ce jour ; environnement d'essai public non qualifié |
| Calendrier | Aucun calendrier fixé : la phase actuelle est une étude de coûts |
| Contact | `contact@otspi.org` |

## 3. Modèle : organisme d'évaluation de la conformité (audit eIDAS)

> **Objet : demande d'estimation, évaluation de la conformité eIDAS d'un prestataire de services de confiance (horodatage)**
>
> Bonjour,
>
> OTSPI est une initiative d'intérêt général, en cours de constitution sous forme d'association, qui prépare un prestataire de services de confiance ouvert dont le premier service serait l'horodatage électronique qualifié. Nous établissons un budget et souhaitons connaître vos ordres de grandeur, sans engagement.
>
> Pourriez-vous nous indiquer :
>
> 1. votre accréditation (ETSI EN 319 403-1, organisme national d'accréditation) pour les services de confiance ;
> 2. une **fourchette de prix** pour l'évaluation initiale d'un prestataire proposant un service d'horodatage qualifié sur deux sites, et pour les évaluations de suivi au moins tous les 24 mois, avec les hypothèses de périmètre retenues ;
> 3. la **durée** habituelle et les **jalons** (revue documentaire, audit sur site, cérémonie de clés) ;
> 4. les **prérequis** que vous attendez avant de démarrer (documents, politiques, maturité du système de management) ;
> 5. les éventuelles **prestations de pré-évaluation** à distinguer de l'audit lui-même ;
> 6. si vous auditez aussi WebTrust for CAs, une fourchette pour une autorité de certification TLS à deux branches.
>
> Notre documentation est publique : [livre blanc](https://about.otspi.org/livre-blanc/). Merci d'avance.
>
> [Signature de rôle] · contact@otspi.org

## 4. Modèle : fabricant ou revendeur de HSM

> **Objet : demande de devis indicatif, HSM réseau certifié pour une autorité de confiance eIDAS**
>
> Bonjour,
>
> OTSPI prépare un prestataire de services de confiance ouvert (horodatage qualifié, puis autorité de certification). Nous étudions le coût de l'équipement cryptographique, sans engagement d'achat.
>
> Besoin à chiffrer :
>
> - **HSM réseau** certifiés Common Criteria EAL4+ conformes à l'EN 419 221-5, mention de qualification en tant que dispositif de création de cachet ou de signature le cas échéant ;
> - **deux sites** distants, chacun avec redondance, plus un HSM hors ligne pour une racine ;
> - clés de racine sous **quorum** (par exemple 3 sur 5), cartes ou jetons d'administrateurs ;
> - support et maintenance sur 5 ans, coût des licences (nombre de partitions, débit de signature), délais de livraison ;
> - conditions éventuelles pour une association d'intérêt général ou un projet open source.
>
> Pourriez-vous nous adresser un devis indicatif ou une fourchette, avec la liste des références et options ? Merci d'avance.
>
> [Signature de rôle] · contact@otspi.org

## 5. Modèle : hébergeur (colocation sur deux sites européens)

> **Objet : demande de conditions, colocation sécurisée sur deux sites européens, projet d'intérêt général**
>
> Bonjour,
>
> OTSPI prépare une infrastructure de services de confiance ouverte et cherche des hébergeurs, éventuellement en mécénat technologique. Nous souhaitons connaître vos conditions, sans engagement.
>
> Besoin :
>
> - deux sites européens **géographiquement distincts** ;
> - baie ou cage **verrouillée** avec contrôle d'accès et traçabilité des entrées, vidéosurveillance ;
> - certification **ISO/IEC 27001** des sites, idéalement qualification ou référencement de sécurité de niveau supérieur ;
> - connectivité redondante, IPv4 et IPv6, énergie redondante ;
> - possibilité d'accueillir des **HSM** et de recevoir des **auditeurs** sur site ;
> - **conditions** pour une association d'intérêt général : tarif, mécénat, valorisation et reçu fiscal si la loi le permet.
>
> Pourriez-vous nous indiquer vos tarifs et conditions pour une, puis deux baies ? Merci d'avance.
>
> [Signature de rôle] · contact@otspi.org

## 6. Autres postes à chiffrer

| Poste | Interlocuteurs à solliciter | Point d'attention |
|---|---|---|
| Source de temps et récepteurs GNSS (OSNMA) | Équipementiers de synchronisation temporelle | Redondance, oscillateurs, traçabilité à l'UTC |
| Assurance responsabilité civile professionnelle | Courtiers et assureurs spécialisés | Garanties exigées par le régime eIDAS |
| Cabinets WebTrust | Cabinets habilités à réaliser les audits WebTrust | Phase 4, après la qualification de l'horodatage |

## 7. Grille de comparaison

À remplir au fur et à mesure, puis à reporter (montants et dates) dans le budget pluriannuel.

| Poste | Prestataire | Date de la réponse | Fourchette ou prix | Hypothèses de périmètre | Confidentialité |
|---|---|---|---|---|---|
| Audit eIDAS |  |  |  |  |  |
| Audit eIDAS |  |  |  |  |  |
| Audit eIDAS |  |  |  |  |  |
| HSM |  |  |  |  |  |
| HSM |  |  |  |  |  |
| HSM |  |  |  |  |  |
| Hébergement |  |  |  |  |  |
| Hébergement |  |  |  |  |  |
| Hébergement |  |  |  |  |  |

## 8. Suites

- [ ] Choisir au moins trois destinataires par poste
- [ ] Envoyer les demandes depuis `contact@otspi.org`
- [ ] Consigner les réponses dans la grille
- [ ] Publier le budget pluriannuel à l'issue de la Phase 1 et retirer la mention « aucun montant » du § 5.5 du livre blanc
