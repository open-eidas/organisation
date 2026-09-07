# Comité de Pilotage Technique (TSC — Technical Steering Committee)

---

## 1. Rôle et Mandat

Le **Comité de Pilotage Technique (TSC)** est l'organe collégial responsable de la direction technique, de la politique de sécurité cryptographique et de la conformité normative des logiciels et infrastructures d'Open eIDAS.

Le TSC opère sous la supervision du Conseil d'Administration de l'association.

### Domaines de compétence :
- **Architecture PKI & TSA** : Définition des profils de certificats, politiques d'horodatage (TSP / *Time-Stamping Policy*), politiques de certification (CP/CPS).
- **Conformité eIDAS & Normes ETSI** : Veille et application des normes ETSI EN 319 401 (exigences générales de sécurité des TSP), ETSI EN 319 421 / 422 (profils d'horodatage), ETSI TS 119 312 (algorithmes cryptographiques).
- **Sécurité Matérielle (HSM)** : Gestion des modules cryptographiques qualifiés (QSCD / CC EAL4+), procédures de cérémonies de clés, dual-control, plan de reprise après sinistre (DRP).
- **Projets Open Source & Codebase** : Validation des architectures, revues de code critiques, maintien des dépôts officiels sur l'organisation GitHub `@open-eidas`.

---

## 2. Processus de Décision et RFC (*Request for Comments*)

Le TSC adopte une philosophie inspirée de l'IETF : **« Rough consensus and running code »** (consensus général et code fonctionnel).

### Cycle de vie d'une proposition (RFC) :
1. **Élaboration** : Tout contributeur ou membre peut soumettre une proposition d'évolution technique sous forme d'une RFC ou d'une Issue documentée sur GitHub.
2. **Débat public** : Période de discussion ouverte de 14 jours minimum permettant à la communauté d'émettre des objections ou suggestions.
3. **Évaluation de sécurité et de conformité** : Le TSC vérifie que la proposition ne compromet ni la qualification eIDAS, ni la sécurité physique ou cryptographique.
4. **Adoption** : Validation par consensus au sein du TSC (ou vote à la majorité qualifiée en cas de désaccord persistant).

---

## 3. Politique de Sécurité et Divulgation Responsable (*Responsible Disclosure*)

La sécurité de nos utilisateurs et de l'infrastructure de confiance est notre priorité absolue.

- **Signalement de vulnérabilités** : Tout chercheur en sécurité ou utilisateur ayant identifié une vulnérabilité potentielle est invité à la signaler en toute confidentialité à l'adresse de contact officielle (en précisant `[Sécurité]` en objet) :  
  📧 **contact@open-eidas.eu** (ou via PGP / GitHub Security Advisories privés).
- **Délai de correction** : Le TSC s'engage à accuser réception sous 48 heures ouvrées et à publier un correctif avant toute divulgation publique.
- **Transparence après résolution** : Un avis de sécurité public (Security Advisory avec CVE si applicable) est publié conjointement avec la mise à jour corrective.

---

## 4. Politique de Releases et Environnements

Pour concilier innovation et stabilité réglementaire, les services sont divisés en deux environnements distincts :

1. **Staging / Bac à Sable (Staging Environment)** :
   - URL et endpoints dédiés aux tests d'intégration, CI/CD et développeurs ;
   - Même niveau technique et algorithmique que la production, mais certificats non qualifiés ;
   - Déploiements continus des nouvelles fonctionnalités.
2. **Production Qualifiée (eIDAS Production)** :
   - Hébergement hautement sécurisé avec HSM certifiés en environnement datacenter certifié ISO 27001 / SecNumCloud ;
   - Certificats qualifiés émis après audit formel de conformité ;
   - Mises à jour strictement encadrées par des fenêtres de maintenance et validation collégiale du TSC.
