# Association OTSPI — Organisation, Gouvernance & Redevabilité Publique
## « Open Trusted Service Provider Initiative »

[![Site Web](https://img.shields.io/badge/Portail_Web-about.otspi.org-blue?style=flat-square)](https://about.otspi.org)
[![Structure](https://img.shields.io/badge/Structure-Intérêt_Général_&_Gestion_Désintéressée-purple?style=flat-square)](#)
[![Normes](https://img.shields.io/badge/Normes-eIDAS_2.0_|_ETSI_|_WebTrust-blue?style=flat-square)](#)
[![Gouvernance](https://img.shields.io/badge/Gouvernance-Ségrégation_des_Devoirs-green?style=flat-square)](#)
[![Redevabilité](https://img.shields.io/badge/Redevabilité-100%25_Publique-orange?style=flat-square)](#)
[![Licence](https://img.shields.io/badge/Licence-CC--BY--4.0-lightgrey?style=flat-square)](LICENSE)

Ce dépôt centralise l'ensemble des documents juridiques, administratifs, réglementaires et de conformité de l'association **« Open Trusted Service Provider Initiative » (OTSPI)**, régie par la loi du 1er juillet 1901, conforme aux critères de l'**intérêt général** (articles 200 et 238 bis du CGI) et aux exigences des **prestataires de services de confiance qualifiés (eIDAS / ETSI / WebTrust)**.

> 🌐 **Portail officiel en ligne : [about.otspi.org](https://about.otspi.org)**  
> Retrouvez l'intégralité des statuts, du règlement intérieur et du socle de conformité présentés sous forme d'un site interactif avec recherche plein texte et liens d'édition directe.

---

## 🏛️ Mission d'Intérêt Général et Confiance Numérique

L'association **OTSPI** a pour vocation d'intérêt général de lever les barrières économiques, techniques, administratives et éducatives à la sécurité, à la confidentialité et à la confiance numérique dans les communications électroniques mondiales.

À l'instar du modèle d'infrastructure d'intérêt général développé par l'**ISRG (*Let's Encrypt*)** pour le chiffrement du Web :
- Nous concevons, opérons et pérennisons des **infrastructures critiques de confiance numérique ouvertes, souveraines, transparentes et universellement accessibles** (horodatage électronique qualifié, scellement, signature numérique, archivage probatoire, gestion des identités) conformes aux règlements européens **eIDAS / eIDAS 2.0** et aux standards internationaux **ETSI** et **WebTrust** ;
- La gouvernance est strictement **désintéressée** (bénévolat strict des dirigeants, inaliénabilité des logiciels libres et des marques, absence de distribution d'actifs) ;
- Un **Fonds de réserve et de garantie opérationnelle** sanctuarisé (Article 12 bis des Statuts) finance l'exécution du plan de fin d'activité (*Termination Plan*, maintien des CRL/OCSP pendant 10 ans), et l'actif net subsistant est dévolu à un organisme d'intérêt général similaire.

---

## ⚖️ Architecture de Gouvernance et Ségrégation des Fonctions

La gouvernance d'OTSPI applique une séparation stricte des devoirs conformément aux normes ETSI EN 319 401 et WebTrust :

1. **Direction Opérationnelle (*Executive Management*)** :  
   Assurée par le **Bureau** issu du **Conseil d'Administration** (Président, Trésorier, Secrétaire Général). Il porte la responsabilité juridique et financière, assure la mise en œuvre de la politique de sécurité et les relations institutionnelles.
2. **Comité des Politiques de Confiance (CPC / PMA)** :  
   Organe collégial technique indépendant garant de la rigueur cryptographique et normative. Il approuve les CP/CPS et politiques de service, valide les protocoles de cérémonies de clés, supervise l'habilitation des Officiers d'Autorité et nomme le Responsable de la Sécurité des Systèmes d'Information (RSSI / CISO). L'appartenance au Bureau est strictement incompatible avec le CPC.
3. **Officiers d'Autorité & Gardiens de Clés (*Key Custodians*)** :  
   Opérateurs habilités assurant sous contrôle à quatre yeux (*Dual Control*) les cérémonies de clés et disposant d'un pouvoir autonome de **révocation d'urgence** sans délai.

---

## 📁 Panoplie Documentaire Complète

```
├── docs/
│   ├── index.md                     # Page d'accueil du portail web about.otspi.org
│   ├── CNAME                        # Configuration du domaine personnalisé (about.otspi.org)
│   ├── statuts/
│   │   └── statuts-association.md   # Statuts constitutifs adoptés (OTSPI, Lyon, 20 septembre 2026)
│   ├── reglement-interieur/
│   │   └── reglement-interieur.md   # RI complet : cursus Officiers, MFA FIPS/ANSSI, Key Custodians, dépenses
│   ├── administratif/
│   │   ├── pv-ag-constitutive-modele.md # PV d'AG Constitutive (élections, mandats fiscaux L.80 CB, RC Pro)
│   │   ├── rescrit-fiscal-mecenat.md    # Demande formelle de rescrit fiscal DGFIP (Méthode 4P)
│   │   └── declaration-prefecture.md    # Guide des formalités préfecture (RNA, JOAFE, SIRET)
│   ├── cadrage/
│   │   ├── index.md                 # Présentation du socle d'audit initial TSP / PKI
│   │   ├── cp-cps-cadre.md          # Cadre général CP/CPS conforme RFC 3647 & ETSI EN 319 411
│   │   ├── pssi.md                  # PSSI (ISO 27001 & ETSI EN 319 401, RSSI, incidents)
│   │   └── termination-plan.md      # Plan de fin d'activité (archivage 10-30 ans, séquestre financier)
│   ├── gouvernance/
│   ├── charte-ethique.md            # Charte d'éthique, de déontologie et de gestion désintéressée
│   │   └── comite-technique.md      # Articulation CPC (PMA), TSC (ingénierie logicielle) & RFCs
│   ├── adhesion/
│   │   └── bulletin-adhesion.md     # Formulaires d'adhésion (sympathisants, titulaires, bienfaiteurs)
│   └── reunions/
│       └── index.md                 # Registre public des réunions et procès-verbaux (caviardage RGPD)
├── mkdocs.yml                       # Configuration Material for MkDocs (about.otspi.org)
├── .github/workflows/
│   └── deploy-pages.yml             # Déploiement automatique GitHub Pages
├── LICENSE                          # Licence Creative Commons Attribution 4.0 International
└── README.md                        # Documentation générale du dépôt
```

---

## 📬 Contacts

- **Général & Adhésions** : `contact@otspi.org`
- **Sécurité & Signalement de vulnérabilités (CVD)** : `security@otspi.org` *(avec mention `[Sécurité]` en objet)*
- **Portail web** : [about.otspi.org](https://about.otspi.org)
