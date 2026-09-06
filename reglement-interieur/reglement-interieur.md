# Règlement Intérieur de l'Association Open eIDAS

*Adopté par le Conseil d'Administration en application de l'Article 18 des Statuts.*

---

## Préambule

Le présent règlement intérieur a pour vocation de préciser les modalités pratiques d'application des statuts de l'Association **Open eIDAS**. Il s'impose à tous les membres de l'association, aux administrateurs, ainsi qu'aux contributeurs participant aux activités et aux projets hébergés.

---

## Titre I — Membres et Adhésions

### Article 1 — Collèges de membres

Pour refléter la diversité des parties prenantes tout en préservant l'indépendance de l'infrastructure, l'association s'articule autour des collèges suivants :

1. **Collège des Développeurs et Contributeurs Actifs** : Personnes physiques contribuant au code source, à l'ingénierie système, à la cryptographie, à la documentation ou aux aspects juridiques.
2. **Collège des Utilisateurs et Citoyens** : Personnes physiques souhaitant soutenir le développement de la confiance numérique souveraine et ouverte.
3. **Collège des Personnes Morales et Partenaires Institutionnels** : Entreprises, fondations, universités, associations ou collectivités publiques soutenant la mission d'intérêt général par des dons, des compétences ou de la mise à disposition d'infrastructures.

### Article 2 — Procédure d'adhésion

1. Toute demande d'adhésion est soumise en ligne ou par e-mail adressé au Bureau (`contact@open-eidas.eu`).
2. Le Bureau valide l'adhésion sous réserve de l'accord du postulant avec les statuts, le présent règlement et la charte d'éthique.
3. Les adhésions sont renouvelables annuellement.

### Article 3 — Démission et exclusion

1. Toute démission prend effet dès notification écrite au Bureau.
2. Tout comportement contraire à la sécurité des infrastructures, violation de la charte éthique, tentative d'ingérence malveillante ou atteinte grave à la réputation de l'association peut motiver une procédure d'exclusion immédiate par le Conseil d'Administration, après échange contradictoire.

---

## Titre II — Gouvernance Technique et Opérationnelle

### Article 4 — Le Comité de Pilotage Technique (TSC — Technical Steering Committee)

1. Le Conseil d'Administration institue un **Comité de Pilotage Technique (TSC)** chargé de garantir l'excellence technique, la sécurité cryptographique et la conformité aux normes européennes (ETSI / eIDAS).
2. **Missions du TSC** :
   - Évaluer et valider les choix d'architecture technique (PKI, algorithmes cryptographiques, support post-quantique, HSM, protocoles de synchronisation) ;
   - Superviser le cycle de vie des logiciels ouverts et des déploiements en production ;
   - Examiner les propositions de modifications majeures (processus RFC — Request for Comments) ;
   - Veiller à l'alignement continu sur les profils ETSI (EN 319 401, EN 319 421, EN 319 422, etc.).
3. Les comptes-rendus des réunions du TSC sont publics et archivés dans les dépôts ouverts de l'organisation.

### Article 5 — Processus de décision technique (RFC)

Toute évolution structurelle des protocoles, des formats de données, des API ou des mécanismes de sécurité fait l'objet d'un document RFC (*Request for Comments*) public soumis à relecture ouverte par la communauté avant arbitrage par le TSC.

---

## Titre III — Sécurité Cryptographique et Exploitation de l'Infrastructure

### Article 6 — Principe de souveraineté et d'ouverture logicielle

1. L'ensemble des composants logiciels constitutifs des services de production (serveurs TSA, validation, connecteurs) doit être publié sous licence libre approuvée (GNU AGPLv3 pour le cœur infrastructurel, licences permissives pour les SDKs d'intégration).
2. Aucun composant privateur ou boîte noire non vérifiable ne peut être intégré dans la chaîne critique de confiance, à l'exception des firmwares certifiés des modules matériels de sécurité (HSM) évalués selon les standards Common Criteria (EAL4+ / EN 419 221-5).

### Article 7 — Cérémonies de clés et contrôle à quatre yeux (Dual Control)

1. Toute opération critique sur les clés cryptographiques de production (génération de clé d'Autorité d'Horodatage ou de Cachet, révocation, renouvellement, scellement de sauvegarde) est obligatoirement soumise :
   - Au **principe du double contrôle** (*dual control*) nécessitant la présence et l'authentification conjointe d'au moins deux opérateurs de sécurité habilités ;
   - À l'exécution d'un protocole de **Cérémonie de Clés** documenté à l'avance ;
   - À l'établissement d'un **Procès-Verbal de Cérémonie de Clés** signé par les participants et auditeurs présents, publié publiquement dans un souci de transparence totale.

### Article 8 — Plan de continuité et terminaison d'activité

1. Conformément à la réglementation eIDAS et aux normes ETSI, l'association maintient un **Plan de Terminaison d'Activité** (*Termination Plan*).
2. Ce plan garantit qu'en cas d'interruption ou d'arrêt programmé de l'association :
   - Les listes de révocation (CRL) et services OCSP restent consultables pendant toute la durée de validité des certificats émis ;
   - Les journaux d'horodatage et preuves cryptographiques sont transférés vers un tiers archiveur de confiance ou une institution publique partenaire ;
   - Les utilisateurs et l'organe de contrôle national (ANSSI en France) sont prévenus dans les délais réglementaires.

---

## Titre IV — Éthique, Conflits d'intérêts et Transparence Financière

### Article 9 — Prévention des conflits d'intérêts

1. Tout membre du Conseil d'Administration ou du TSC exerçant des responsabilités ou détenant des intérêts financiers dans une entité commerciale opérant dans le domaine des services de confiance ou des technologies connexes doit en faire la déclaration écrite au Bureau.
2. Tout administrateur en situation de conflit d'intérêt potentiel sur une décision spécifique s'abstient de prendre part au vote délibératif sur ce point précis.

### Article 10 — Transparence financière et dons

1. L'association publie annuellement son bilan financier complet et son compte de résultat de manière transparente.
2. L'association refuse tout financement, subvention ou don qui serait assorti de conditions incompatibles avec l'ouverture du code source, la neutralité du service ou l'indépendance de ses choix cryptographiques.

---

## Titre V — Fonctionnement Quotidien et Frais de Bénévolat

### Article 11 — Outils de communication et vote électronique

1. Les outils officiels de collaboration sont privilégiés parmi les solutions libres, ouvertes ou auditables (dépôts Git de l'organisation, listes de diffusion publiques, messageries chiffrées).
2. Les votes électroniques pour les réunions du CA, du TSC ou des Assemblées Générales sont réalisés via des systèmes garantissant l'émargement et l'intégrité du scrutin.

### Article 12 — Remboursement des frais de mission

1. Les administrateurs et bénévoles peuvent obtenir le remboursement des frais de déplacement, d'hébergement ou d'achat de matériel engagés pour le compte exclusif de l'association.
2. Tout remboursement est conditionné à :
   - Un accord préalable du Bureau pour les dépenses supérieures à un montant fixé par le CA ;
   - La production de factures originales acquittées ou de justificatifs probants.
3. Les bénévoles peuvent également renoncer au remboursement de leurs frais et demander l'établissement d'un reçu fiscal pour don (selon l'éligibilité fiscale de l'association au régime du mécénat).
