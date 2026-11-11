---
id: partner-iagon-wurth-project
title: "Iagon & Würth: Catalyst project"
type: partner
status: draft
owner: Pavlo Babenko
updated: 2026-11-11
reviewed: 2026-11-10
visibility: team
sources: [raw/archive/2026-11-11-claude-project-iagon-sources.md, res-wurth-m4-evidence, res-wurth-m4-video, res-wurth-m4-acceptance]
related: [series-wurth]
tags: [catalyst, wurth, enterprise, 3d-printing, ip]
---

# Iagon & Würth: Catalyst project

**Full name:** Iagon & Würth: Platform for Secure 3D Printing and Intellectual Property Management.

## Project facts

- **Catalyst:** Fund13, #1300111. Budget 1,560,000 ADA.
- **Partner:** Würth Canada Limited, within Würth Group. Not "Würth Group" as a whole.
- **Stage:** pilot / validation, not production. Prototype runs on the Cardano **preprod testnet**.
- **Public naming:** the pilot is public, naming the partner is legitimate. Co-branding and quotes from Würth staff need written approval.

## Milestones

| # | Milestone | Status |
|---|---|---|
| M1 | _name to add_ | Completed (January 2026) |
| M2 | _name to add_ | Approved |
| M3 | _name to add_ (storage connector designed here) | _status to confirm_ |
| M4 | Complete initial development prototype on testnet | Proof of Achievement drafted 2026-11-10, accepted by Würth Canada |
| M5 | _name to add_ (production hardening of the connector) | Next |

## Milestone 4: what was delivered

Source: M4 Proof of Achievement draft (2026-11-10). Full evidence: [M4 evidence package](https://github.com/IagonAS/iagon-wurth-catalyst-public/tree/main/docs/milestone-4).

The prototype links Würth's **ORSY Connect** storefront and admin to four Iagon components: the royalty orchestrator, the partner dashboard, the storage connector and the royalty smart contracts. As agreed in M3, buyers use Würth's own ORSY Connect, there is no separate storefront. The storage connector also serves Würth's **Digital Inventory Services (DIS)**.

### Headline numbers

- **25 testers** from Würth Canada (13), the ORSY Connect team at Würth IT India (2) and Iagon (10). 15 shop accounts, 2 admin accounts, 8 with both.
- **101 tests across 8 scenarios, all passed.** Average ease rating 4.96 / 5. Forms dated 2026-10-29 to 2026-11-03.
- **32 orders**: 31 settled on chain in **26 transactions**, 1 test order cancelled inside its 24-hour window and never settled.
- **First vendor payout** from the treasury on 2026-11-05: 15.00 tUSD.
- Dashboard export on 2026-11-05: 21 vendors, 24 licences, 32 orders. 31 settled orders worth 634.36 tUSD. 26 settlements issued 75.75 tUSD of royalties and 2.4845 tUSD of maintainer fee as IOU.
- **27 of 27 transactions** confirmed on preprod. Script use within 5.1% of the memory limit and 3.2% of the CPU limit per transaction.
- All 22 IOU balances on the dashboard (21 vendors + maintainer) match the chain to the micro-unit.
- Storage connector: **35 of 35** automated component tests passed (2026-11-05, commit ce5c01d). 12 integration tests need a running gateway and weren't part of this offline run. Upload and print-queue scenarios passed 10 of 10 each in the tester round.
- Settlement 4 to 236 seconds after the cancellation window closed.

### The four outputs

- **A. User Portal Beta.** Buyers browse IP and buy print licences in ORSY Connect UAT. Würth admins send print files to the print queue. Smart contracts settle each order on chain. Four changes shipped during the test round: self-service API keys, download links tied to orders, clearer API errors, owner-only file access. Next step agreed with Würth: support for additional printers.
- **B. Admin Dashboard Prototype.** Admin work in the ORSY Connect admin (register IP holders, add parts and licences, upload print files, create print jobs, track orders) and in the Iagon partner dashboard as the ledger (Overview, Vendors, Licenses, Orders, Payouts, Files). Würth said it was happy with the dashboard and with how fast two questions were closed.
- **C. Storage Connector.** A compatibility gateway: Würth's systems talk to it through a standard enterprise object-storage interface, and it turns each request into Iagon storage operations. Würth keeps its usual tooling while files live in Iagon's decentralized storage. Serves ORSY Connect UAT and DIS. Download links are issued only for an existing, non-cancelled order containing the part, and every link request is logged.
- **D. Smart Contract Test Logs.** The royalty script works as an IOU minting policy and a treasury spending validator. After the 24-hour cancellation window the settlement mints the royalty and maintainer fee as IOU tokens. A payout burns the vendor's IOU and the treasury releases the same amount of tUSD. **A licence-to-print purchase becomes a royalty token on chain, redeemable one to one from the treasury.** Orders already settled keep the royalty they were placed with.
- **E. Video walkthrough and partner acceptance.** About 8 minutes, one order from start to finish. Würth Canada signed a Partner Acceptance Statement via DocuSign: the work meets the agreed scope and quality, M4 is complete.

### Worked example

Order Test_10-1_30: a buyer bought 3 × GOLF MOUNTING BRACKET at a royalty of 2.00 tUSD per piece. It settled 15 seconds after its window closed and minted 6.00 IOU for the vendor and 0.204 IOU for the maintainer. [Settlement on the explorer](https://preprod.cexplorer.io/tx/e5d354535feb326e3a440b7453cb76392f79834518178d80155d299b26df7216).

## Marketing use

- Strongest proof points for the [Würth series](../../series/wurth/series.md), Act II (what we built): a royalty token per licence-to-print purchase, file access tied to orders, Würth's own storage tooling on top of decentralized storage.
- Everything is on **testnet with test stablecoin (tUSD)**. Always say so. Never present tUSD amounts as revenue.
- Tester names and emails are redacted. Partner-confidential test details are given in general terms on purpose. Keep it that way.

## Links

- [M4 evidence package](https://github.com/IagonAS/iagon-wurth-catalyst-public/tree/main/docs/milestone-4)
- [Video walkthrough](https://youtu.be/VSj8q51m_9A)
- [Würth Canada Partner Acceptance Statement](https://iagon.media/Wurth-iagon-evidence-M4-confirmation.pdf)
- Royalty script on preprod: `b6a73a46f799c90029baf4e0e623779ada9d98b614df432db3a08eec`
