# Règlement Intérieur de l'Association Open eIDAS

*Adopté par le Conseil d'Administration en application de l'Article 20 des Statuts.*  
*Conforme aux critères d'intérêt général (CGI art. 200 & 238 bis), aux principes directeurs d'utilité publique et à la politique de redevabilité publique intégrale (Public Accountability).*

---

## Préambule

Le présent Règlement Intérieur précise les modalités pratiques de mise en œuvre des statuts de l'Association **Open eIDAS**. Il définit les obligations de transparence publique, les procédures de sécurité opérationnelle, les garanties de protection des données personnelles (RGPD) et les règles d'éthique garantissant la gouvernance désintéressée d'une infrastructure numérique d'intérêt général.

---

## Titre I — Redevabilité Publique Intégrale (*Full Public Accountability*)

### Article 1 — Principe de publication intégrale des travaux et réunions

1. En application de l'Article 3 des Statuts, toutes les décisions, réunions et orientations stratégiques de l'association font l'objet d'une documentation publique et transparente.
2. Sont obligatoirement rendus publics en libre accès dans les dépôts ouverts de l'organisation :
   - Les convocations et ordres du jour des réunions du Conseil d'Administration, des Assemblées Générales et du Comité de Pilotage Technique (TSC) ;
   - Les comptes-rendus et procès-verbaux de délibérations ;
   - Les documents de cadrage stratégique, feuilles de route (*roadmaps*) et spécifications techniques (RFCs) ;
   - Les budgets prévisionnels, comptes annuels certifiés, rapports moraux et financiers ;
   - Les rapports d'évaluation d'audit de conformité (normes ETSI EN 319 401, EN 319 421 / 422, règlements eIDAS) ;
   - Les politiques de certification (CP/CPS) et politiques d'horodatage (TSP).

---

### Article 2 — Dérogation n°1 : Protection de la vie privée et conformité RGPD

1. Conformément au Règlement (UE) 2016/679 (Règlement Général sur la Protection des Données - RGPD), le droit à la protection de la vie privée des membres, votants, donateurs et contributeurs est expressément garanti.
2. **Mesures d'anonymisation et de pseudonymisation préalables à toute publication** :
   - Avant publication de tout procès-verbal, relevé de vote ou liste de présences, les données nominatives et personnelles sensibles (adresses postales personnelles, adresses e-mails privées, numéros de téléphone, situations familiales, montants précis des dons nominatifs de particuliers) sont systématiquement expurgées ou anonymisées.
   - Les adhérents et votants peuvent demander l'usage de leur identifiant public (pseudonyme de contributeur ou identifiant GitHub / PGP) pour la consignation des votes électroniques.
   - Seuls les noms et prénoms légaux des administrateurs et dirigeants légaux obligatoirement déclarés en préfecture font l'objet d'une mention nominative officielle, sans mention de leurs coordonnées privées.

---

### Article 3 — Dérogation n°2 : Sécurité opérationnelle et divulgation coordonnée de vulnérabilités (*Coordinated Vulnerability Disclosure*)

1. La sécurité des utilisateurs de l'infrastructure de confiance constitue un impératif d'ordre public. Par exception au principe de publication immédiate, les signalements de vulnérabilités techniques critiques font l'objet d'un protocole de **divulgation coordonnée et responsable** (*Coordinated Vulnerability Disclosure - CVD*) :
   - Tout signalement reçu sur le canal sécurisé (`security@open-eidas.eu`) est traité sous **embargo de confidentialité temporaire** ;
   - La période d'embargo est strictement délimitée au temps indispensable à l'analyse de l'impact, au développement, au test et au déploiement en production du correctif de sécurité (délai cible standard de 90 jours maximum, sauf urgence opérationnelle) ;
   - Dès le correctif déployé, l'embargo est immédiatement levé et un **avis de sécurité public complet (*Security Advisory*)** avec numéro CVE est publié en toute transparence, détaillant la nature de la faille, les risques, les correctifs appliqués et les mesures correctives.
2. Le secret technique absolu des clés privées racines et des secrets matériels protégés au sein des modules HSM certifiés relève de la sécurité opérationnelle et n'est en aucun cas diffusable.

---

## Titre II — Membres, Collèges et Fonctionnement Démocratique

### Article 4 — Collèges représentatifs

Pour garantir une gouvernance équilibrée conforme aux critères d'utilité publique :
1. **Collège des Développeurs et Contributeurs Actifs** : Personnes physiques contribuant au développement, à l'infrastructure, à la cryptographie, à la conformité juridique ou à la documentation.
2. **Collège des Utilisateurs et Citoyens** : Particuliers et bénéficiaires de l'infrastructure soutenant le droit à la confiance numérique ouverte.
3. **Collège des Personnes Morales et Soutiens Institutionnels** : Entreprises, fondations, universités, associations ou collectivités publiques soutenant la mission d'intérêt général par des dons, des compétences ou de l'infrastructure.

### Article 5 — Procédures d'adhésion et non-discrimination

1. Les demandes d'adhésion s'effectuent par voie dématérialisée auprès du Bureau (`contact@open-eidas.eu`).
2. Aucune condition financière disproportionnée ne peut faire obstacle à l'adhésion de particuliers. Un tarif réduit de cotisation (ou dispense pour motif économique) est prévu pour garantir l'accès démocratique à tous.

---

## Titre III — Gouvernance Technique et Sécurité Cryptographique

### Article 6 — Le Comité de Pilotage Technique (TSC — Technical Steering Committee)

1. Le TSC est composé d'experts en cryptographie, systèmes distribués, sécurité matérielle (HSM) et conformité réglementaire eIDAS / ETSI.
2. Toutes les réunions du TSC sont documentées sous forme de comptes-rendus publics archivés dans les dépôts de l'organisation.
3. Les propositions d'évolution d'architecture ou de protocoles suivent le processus ouvert des **RFCs (*Request for Comments*)**, garantissant à tout membre de la communauté le droit de proposer, commenter et relire les spécifications.

### Article 7 — Cérémonies de clés et contrôle à quatre yeux (Dual Control)

1. Toute opération sur les clés cryptographiques de confiance (génération de clé d'autorité d'horodatage, renouvellement de certificat, révocation, scellement de sauvegarde) est obligatoirement soumise au **principe du double contrôle (*dual control*)** avec au moins deux officiers de sécurité habilités.
2. Chaque cérémonie de clés se déroule selon un script prédéfini et fait l'objet d'un **Procès-Verbal de Cérémonie de Clés** signé par les participants et les témoins/auditeurs indépendants, puis publié publiquement.

### Article 8 — Plan de terminaison d'activité et continuité de service

1. Conformément à la norme ETSI EN 319 401 et aux règlements eIDAS, l'association maintient un plan formel de fin d'activité (*Termination Plan*).
2. Ce plan prévoit la garantie d'accès continu aux listes de révocation (CRL) et journaux d'horodatage pour une durée d'au moins dix (10) ans après émission, même en cas de cessation d'activité de l'association, via un dépôt d'archives probantes auprès d'une institution publique ou d'un tiers de confiance partenaire.

---

## Titre IV — Éthique, Bénévolat Strict et Prévention des Conflits d'Intérêts

### Article 9 — Strict bénévolat et absence de rémunération

1. Les mandats d'administrateurs et de dirigeants sont strictement bénévoles.
2. Les administrateurs et dirigeants ne peuvent en aucun cas percevoir d'honoraires, de gratifications, de commissions ou d'avantages en nature de la part de l'association.
3. Les remboursements de frais réels engagés pour l'association sont soumis à production de factures originales et à l'approbation conjointe du Président et du Trésorier, et sont annexés au rapport financier annuel.

### Article 10 — Déclaration d'intérêts et prévention des conflits d'intérêts

1. Chaque membre du Conseil d'Administration et du TSC signe une déclaration publique d'intérêts mentionnant ses liens professionnels ou d'affaires avec des entreprises du secteur de la confiance numérique.
2. En cas de délibération concernant un contrat, un partenariat ou une décision technique impliquant une structure avec laquelle un administrateur a un lien d'intérêt, celui-ci s'abstient impérativement de participer au vote.

### Article 11 — Régime des dons et mécénat

1. L'association n'accorde aucune contrepartie directe ou indirecte, matérielle ou immatérielle, aux donateurs et mécènes, conformément aux critères de déductibilité fiscale des dons aux organismes d'intérêt général (articles 200 et 238 bis du CGI).
2. Aucun don ou subvention assorti de clauses restreignant l'indépendance de l'infrastructure, l'ouverture des codes sources sous licence libre ou l'égalité d'accès des utilisateurs ne peut être accepté.
