---
title: "Hosting transparency — OTSPI"
description: "Where OTSPI's websites and test environment are hosted today, and under which jurisdiction."
lang: en
---

# Hosting transparency

**Where OTSPI's websites and test environment run today, and under which jurisdiction**

!!! note "Status of this document"
    Snapshot of 26 September 2026, based on DNS records and public address databases (approximate location). OTSPI stands for trust infrastructure hosted in Europe: this document does not claim the current situation is final, it states what it is so that anyone can judge. It will be updated with every change. This English version is a translation of the [French page](hebergements.md), which is the reference.

---

## 1. What is hosted where

| Item | Address | Host | Company and applicable law | Indicated location |
|---|---|---|---|---|
| Showcase website | www.otspi.org | Infomaniak | Switzerland (adequacy decision of the European Commission under the GDPR) | Geneva |
| Portal, white paper, statutes | about.otspi.org | GitHub Pages | US company (Microsoft); served through a content delivery network | United States, worldwide delivery network |
| Manifesto signatures (name, email address) | manifesto-sign.otspi.org | o2switch | French company, EU law | France |
| Audience measurement of the showcase website (Matomo, cookieless) | stats.otspi.org | o2switch | French company, EU law | France |
| Web demonstrator | demo.open-eidas.eu | GitHub Pages | Same | Same |
| Test time-stamping API | api.staging.open-eidas.eu | Scaleway | French company, EU law | Paris |
| Source code, discussions, automated deployments | github.com/otspi | GitHub | US company | United States |
| Name servers (DNS) | otspi.org, open-eidas.eu | Infomaniak | Switzerland | Switzerland |

## 2. What this implies

- **Test environment.** Nothing listed above carries a qualified trust service, a production key or sensitive personal data. The only personal data collected are the manifesto signatures, stored in France and withdrawable at any time through a link. Tokens issued by the test bench have no legal value.
- **Gap with the stated ambition.** The future trust service infrastructure must be hosted on two European sites (see the [white paper](../white-paper/index.md#43-physical-hosting)). The presentation sites, the portal and the code are today partly hosted by a US company, and are therefore subject to US law.
- **What is already limited.** Neither the showcase website nor the portal uses external fonts or third-party tracking services. Audience measurement for the showcase website relies on a Matomo instance run by OTSPI at o2switch, cookieless and honouring "Do Not Track"; neither the showcase website nor the signature application sets cookies.

## 3. Possible next steps

| Option | Effect | Status |
|---|---|---|
| Host the portal with a European provider | Brings the portal under EU or Swiss law | To be studied |
| Mirror the code on a non-commercial European forge | Reduces dependence on a single platform | To be studied |
| Hosting of the future infrastructure | Two European sites, certified HSMs | Provided for by the white paper |

None of these changes has been decided to date.
