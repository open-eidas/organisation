# Arc d'identifiants d'objet (OID) d'OTSPI

## Plan d'obtention d'un numéro d'entreprise IANA et d'allocation de l'arc

!!! note "Statut du document"
    Document de cadrage, version 0.1, en cours d'examen par le Comité des Politiques de Confiance (CPC). Il décrit une démarche à engager ; la demande auprès de l'IANA n'a pas encore été déposée.

---

## 1. Pourquoi un arc d'OID propre

Les jetons d'horodatage, les certificats et les politiques d'OTSPI portent des **identifiants d'objet (OID)**. Ces identifiants sont gravés dans des preuves qui doivent rester vérifiables pendant des décennies : ils ne peuvent ni changer, ni être réutilisés, ni appartenir à un tiers.

Le service de staging utilise aujourd'hui l'OID de test `1.3.6.1.4.1.99999.1.1.1`. Ce choix était acceptable pour un banc d'essai, mais il ne peut pas être conservé :

- le numéro d'entreprise `99999` n'est pas réservé à l'usage de test. Le registre IANA des numéros d'entreprise (*Private Enterprise Numbers*, PEN), mis à jour le 24 septembre 2026, en est au numéro 66 956 et les attribue dans l'ordre : **le numéro 99999 sera un jour attribué à une autre organisation**, qui deviendrait alors titulaire légitime de l'arc que nous utilisons ;
- un OID de politique doit relever d'un arc **dont OTSPI est titulaire**, conformément à l'ETSI EN 319 401 et à l'ETSI EN 319 421 (identification de la politique d'horodatage).

## 2. Titulaire de l'attribution : l'association, pas une personne

L'IANA accepte les attributions au nom d'une organisation ou d'une personne physique. Pour OTSPI, le titulaire doit être **l'association**, pour deux raisons :

- l'arc d'OID fait partie des actifs immatériels inaliénables du projet (article 13 du projet de statuts) et ne doit pas dépendre d'une personne ;
- une attribution personnelle créerait une dépendance à un individu pour un identifiant destiné à durer plus longtemps que ses fondateurs.

**Calendrier recommandé.**

| Situation | Démarche |
|---|---|
| Association déclarée en préfecture (numéro RNA obtenu) | Déposer la demande au nom de l'association. **Voie à privilégier.** |
| Déclaration pas encore effectuée | Déposer la demande au nom de l'initiative (« Open Trusted Service Provider Initiative (OTSPI) »), avec une adresse de contact de rôle, puis faire mettre à jour le titulaire auprès de l'IANA dès la déclaration de l'association. |

La demande est **gratuite** ; l'IANA envoie un e-mail de confirmation à l'adresse indiquée et, sans complément d'information à fournir, l'attribution intervient dans les sept jours suivant la réponse.

## 3. Informations de la demande

Le formulaire IANA comporte une section *Assignee* et une section *Contact*. Les informations du registre sont **publiques** : elles doivent donc être limitées à celles qui peuvent l'être.

| Champ | Valeur prévue |
|---|---|
| Organisation | Open Trusted Service Provider Initiative (OTSPI) |
| Adresse et pays | Adresse postale du siège (Métropole de Lyon, France), à saisir au moment de la demande |
| Contact (nom) | Un intitulé de rôle plutôt qu'un nom de personne, tel que « OTSPI — Trust Policy Committee » |
| Contact (e-mail) | `contact@otspi.org` (adresse de rôle, non nominative) |
| Téléphone, fax | Non renseignés (facultatifs) |

L'adresse de contact doit rester relevable à long terme : elle servira à la confirmation initiale et à toute mise à jour ultérieure de l'attribution.

## 4. Allocation de l'arc

Notation : `<PEN>` désigne le numéro qui sera attribué, sous l'arc `1.3.6.1.4.1.<PEN>`.

| Arc | Usage |
|---|---|
| `<PEN>.1` | Politiques de service (production) |
| `<PEN>.1.1` | Politiques d'horodatage (TSA) ; `<PEN>.1.1.1` : première politique d'horodatage |
| `<PEN>.1.2` | Politiques de cachet et de signature (réservé) |
| `<PEN>.1.3` | Politiques de certificats TLS (réservé) |
| `<PEN>.2` | Politiques de certification (CP/CPS) |
| `<PEN>.3` | Extensions et attributs (réservé) |
| `<PEN>.9` | **Test et staging**, qui reproduit à l'identique la structure ci-dessus (ex. `<PEN>.9.1.1.1`) |

Règles de gestion :

1. **Séparation stricte du test et de la production.** Un jeton émis par le staging ne doit jamais pouvoir être pris pour un jeton de production : le staging utilise uniquement l'arc `<PEN>.9`.
2. **Immuabilité.** Un OID publié n'est jamais réutilisé ni modifié ; une évolution de politique donne un nouvel OID (dernier arc incrémenté).
3. **Registre public.** Chaque attribution est consignée dans un registre publié dans le dépôt de gouvernance, avec sa date, son objet et le document de référence.
4. **Approbation par le CPC.** Toute nouvelle branche de l'arc est approuvée par le CPC, comme les politiques de certification et de service dont il a la charge (article 8 bis du projet de statuts).
5. **Conformité à la politique de référence.** La Politique d'Horodatage d'OTSPI déclare sa conformité à la politique *Best Practices Time-Stamp Policy* de l'ETSI EN 319 421 (OID `0.4.0.2023.1.1`). La forme exacte de cette déclaration (OID propre référençant la BTSP, ou reprise directe de l'OID de l'ETSI) est à arrêter avec l'organisme d'évaluation de la conformité lors de la phase 2.

## 5. Plan de remplacement dans le code

Le remplacement est essentiellement une affaire de **configuration** : l'OID de politique du moteur est lu dans la variable d'environnement `OPENEIDAS_POLICY_OID`. Il faut néanmoins traiter **toutes** les occurrences de la valeur de test, aujourd'hui au nombre de 18 dans le dépôt du moteur :

| Élément | Fichier |
|---|---|
| Valeur par défaut de la configuration et test associé | `crates/oe-config/src/lib.rs` |
| Tests d'intégration et de bout en bout | `crates/oe-crosstsa/tests/`, `crates/oe-httpapi/tests/`, `crates/oe-tsa-core/tests/`, `crates/oe-tsa-core/src/lib.rs` |
| Déploiement | `deploy/helm/open-eidas/values.yaml`, `docker-compose.yml` |
| Documentation | `docs/API.md`, `docs/ARCHITECTURE.md`, `docs/CPS.md` |

Séquence :

1. Obtenir le numéro d'entreprise et l'enregistrer dans le registre d'OID.
2. Remplacer la valeur de test par `<PEN>.9.1.1.1` (arc de **test**) partout, y compris dans la configuration du staging.
3. Ne renseigner l'OID de production `<PEN>.1.1.1` qu'au moment de la mise en service du service qualifié, après approbation de la Politique d'Horodatage par le CPC.
4. Faire échouer la mise en production si l'OID configuré appartient à l'arc de test (garde-fou à prévoir dans le moteur).

Les jetons déjà émis par le staging sous l'ancien OID n'ont aucune valeur juridique et n'ont pas à être migrés.

## 6. Prochaines étapes

- [ ] Décision du CPC sur le titulaire de l'attribution (association ou initiative)
- [ ] Dépôt de la demande auprès de l'IANA
- [ ] Publication du registre d'OID
- [ ] Remplacement de l'OID de test dans le moteur et le staging
- [ ] Garde-fou de mise en production
