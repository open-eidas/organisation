# Transparence sur les hébergements

**Où tournent aujourd'hui les sites et le banc d'essai d'OTSPI, et sous quelle juridiction**

!!! note "Statut du document"
    Relevé du 26 septembre 2026, établi d'après les enregistrements DNS et les bases d'adressage publiques (localisation approximative). OTSPI défend une infrastructure de confiance hébergée en Europe : ce document ne dit pas que l'état actuel est définitif, il dit ce qu'il est, pour que chacun puisse en juger. Il sera mis à jour à chaque changement. Une [version anglaise](hosting.md) est disponible.

---

## 1. Ce qui est hébergé où

| Élément | Adresse | Hébergeur | Société et droit applicable | Localisation indiquée |
|---|---|---|---|---|
| Vitrine | www.otspi.org (et otspi.org, otspi.com, otspi.eu, otspi.fr, open-eidas.eu, redirigés) | o2switch | Société française, droit de l'Union | France |
| Portail, livre blanc, statuts | about.otspi.org | o2switch | Société française, droit de l'Union | France |
| Signatures du manifeste (nom, adresse électronique) | manifesto-sign.otspi.org | o2switch | Société française, droit de l'Union | France |
| Mesure d'audience des sites (Matomo Tag Manager, sans cookie) | stats.otspi.org | o2switch | Société française, droit de l'Union | France |
| Démonstrateur Web | demo.open-eidas.eu | o2switch | Société française, droit de l'Union | France |
| API d'horodatage d'essai | api.staging.open-eidas.eu | Scaleway | Société française, droit de l'Union | Paris |
| Code source, discussions, déploiements automatisés | github.com/otspi | GitHub | Société américaine | États-Unis |
| Serveurs de noms (DNS) | otspi.org, open-eidas.eu | Infomaniak | Suisse (décision d'adéquation RGPD de la Commission européenne) | Suisse |
| Messagerie | contact@otspi.org | Infomaniak | Suisse | Suisse |

## 2. Ce que cela implique

- **Environnement d'essai.** Rien de ce qui est listé ci-dessus ne porte de service de confiance qualifié, de clé de production ni de donnée personnelle sensible. Les seules données personnelles recueillies sont les signatures du manifeste, conservées en France et retirables à tout moment par lien. Les jetons du banc d'essai n'ont aucune valeur juridique.
- **Écart avec l'ambition affichée.** La future infrastructure de services de confiance devra être hébergée sur deux sites européens (voir le [livre blanc](../livre-blanc/index.md#43-hebergement-physique)). Depuis le 26 septembre 2026, tous les sites Web sont hébergés en France. Le code source, les discussions et les déploiements automatisés restent sur GitHub, société américaine soumise au droit américain.
- **Ce qui est déjà limité.** Ni la vitrine ni le portail n'utilisent de police de caractères externe ni de service tiers de suivi. La mesure d'audience de la vitrine, du portail, du démonstrateur et du formulaire de signature passe par une instance Matomo gérée par OTSPI chez o2switch, sans cookie et respectueuse de la mention « Do Not Track » ; aucun de ces sites ne dépose de cookie. Le formulaire de signature ne mesure pas les pages dont l'adresse porte un jeton personnel (confirmation, retrait, modération).

## 3. Pistes d'évolution

| Piste | Effet | Statut |
|---|---|---|
| Héberger le portail et le démonstrateur chez un hébergeur européen | Ramène tous les sites sous droit européen | Fait (o2switch, 26 septembre 2026) |
| Miroir du code sur une forge européenne non commerciale | Réduit la dépendance à une seule plateforme | À étudier |
| Hébergement de la future infrastructure | Deux sites européens, HSM certifiés | Prévu par le livre blanc |

Aucune de ces évolutions n'est décidée à ce jour.
