# Midmak — Repellent Brick: Prototyping & Test Plan v1.0

<div dir="rtl" class="ar" markdown="1">

**الغرض بالعربية.** خطة تنفيذية لتحويل التصميم النظري إلى نماذج أولية واختبارها على أربع بوابات قرار. القاعدة: **لا ادعاء علنيًا قبل البوابة 2**، وأي نتيجة تخالف الفرضيات (خصوصًا عتبة الطرد C\*) تُحدِّث النموذج قبل المتابعة.

</div>

## 1. Phases and decision gates

| Gate | Window | Question | Pass criteria | If it fails |
|---|---|---|---|---|
| **G0 Materials screen** | Weeks 0–4 | Do oils, carriers and shells survive the alkaline skin and keep set/strength? | Set-time shift ≤ ±30 min; 7-day strength ≥ 90 % of control; capsules intact after 30 min in pore solution pH 13 (microscopy + free-oil test) | Switch shell (silica/Pickering) or use sealer-only variant |
| **G1 Release + repellency (lab)** | Weeks 4–16 | Is flux in the 0.2–0.4 g/day·m² window and does it change insect behaviour? | Flux window met for ≥ 30 d at 25 °C; wind-tunnel landing reduction ≥ 60 % at 0.3 m; **EC₅₀ (C\*) measured** | Re-fit model with measured C\*; resize loading or reposition as contact-zone deterrent |
| **G2 Durability + safety** | Months 4–9 | Does the brick stay compliant and safe? | Strength ≥ 90 % of control at 28 d and after 20 wet/dry cycles; no efflorescence; ecotox margins met; odour ≤ weak | Reformulate (lower loading, different oil cut) |
| **G3 Field pilot** | Months 9–21 | Does it work outdoors in Oman heat for 6–12 months? | ≥ 40 % fewer visits/landings at 0.5 m vs untreated; flux retained ≥ 15 % at 12 months in shade; no complaints | Adjust re-coat interval, shading rules, claims |

## 2. Experimental matrix

| ID | Description | Purpose |
|---|---|---|
| **C0** | Plain recycled-aggregate brick (project mix) | Negative control (mechanical + behaviour) |
| **C1** | Same skin with **empty** carriers/capsules + sealer (no oil) | Separates physical effects (porosity, colour) from chemical repellency |
| **F0** | Neat oil in skin (benchmark of the worst case) | Burst reference |
| **F1** | Oil on diatomite/zeolite carrier in skin | Diffusion-controlled carrier |
| **F2** | β-CD complex + carrier in skin | Premium sustained variant |
| **F3** | Biopolymer capsules in skin + capsule-loaded sealer | Primary design |
| **F3-Cd / F3-Cs** | F3 with cedarwood-rich / citronella-rich oil cut | Persistence vs onset trade-off |

Per formulation: **3 independent batches × 12 bricks** (20 × 10 × 10 cm sandwich: 90 mm core + 10 mm skin) = 36 bricks; allocate 10 to mechanical, 6 to release chambers, 8 to bioassays, 12 to ageing/field. Randomise brick position in all tests and blind the scorer to treatment codes.

## 3. Prototype fabrication (lab scale)

1. **Baseline.** Freeze the current Midmak recycled-aggregate recipe (record RCA grading, water absorption, cement type, w/c). Use it unchanged for C0 and for the core of every brick.
2. **Carrier loading (F1, F2, F3 carriers).** Dry diatomite or clinoptilolite at 105 °C for 2 h; cool in a desiccator; vacuum-impregnate with oil (≈ −0.08 MPa, 30 min) to ≈ 40 wt % loading; rest 24 h; weigh free oil on the surface (target ≤ 5 %). *Safety: oils are flammable; no heat while loaded.*
3. **β-CD complex (F2).** Co-precipitate oil with β-cyclodextrin in water (1:6–1:8 oil:CD by mass), stir 4 h at 40 °C, cool to 4 °C, filter, air-dry < 40 °C; check loading by extraction.
4. **Microcapsules (F3).** Starting recipe: complex coacervation with gelatin (type A) + gum arabic 1:1, pH ≈ 4.0, 40–50 °C, oil:wall ≈ 1:1, crosslink with transglutaminase (avoid glutaraldehyde); wash and dry below 40 °C. Characterise size (target D50 30–80 µm), encapsulation efficiency, and stability in pH-13 pore solution. Backup: silica-stabilised (Pickering) droplets.
5. **Skin mortar.** Fines < 4 mm RCA + cement + water as in the baseline; add carriers/capsules **last** (≤ 3 wt % of skin, ≤ 2 min mixing). Measure flow and set time (EN 196-3 / ASTM C191).
6. **Casting.** Face-down mould: 10 mm skin first, core placed within 30 min (wet-on-wet), vibrate 10 s. Cover 24 h; demould; moist cure 7 d at 25 ± 2 °C; then ≤ 35 °C ambient to day 28.
7. **Sealer (day 28).** Lime or silicate sealer with 3 wt % capsules, 2 coats ≈ 200 g/m² total, 6 h apart; cure 7 d. Record mass added.
8. **Labelling and traveler.** Unique ID per brick; traveler lists oil batch/COA, carrier lot, capsule lot, cure log.
9. **Fired-brick and geopolymer variants (later).** Apply only post-fire/post-cure (vacuum impregnation or coating). Do not add oils to the mix.

## 4. Laboratory protocols

### L1. Release kinetics (replaces all assumed parameters)
- **Dynamic chamber:** one brick face in a 20 L glass chamber, 25 ± 1 °C, 50 % RH, clean-air flow 0.5 L/min; sorbent tubes (Tenax TA) sampled 4 h at days 1, 3, 7, 14, 30, 60, 90; analysis by thermal-desorption GC-MS with calibration per marker compound (cedrol, thujopsene, geraniol, citronellol).
- **Mass-loss:** weigh bricks (±0.01 g) weekly under standard conditions; confirm with solvent extraction of sacrificial bricks at days 0, 30, 90, 180, 365 (mass balance 85–115 %).
- **Temperature series:** repeat at 40 °C and 55 °C for 7 days → fit D₂₅ and Eₐ (Arrhenius). **Output:** CSV of flux vs time per formulation → replace parameters in `simulation/release_model.py` and rerun.
- **TGA/DSC** on carriers, CD complex and capsules (30–300 °C, 5 K/min) to get volatilisation onset and retention.

### L2. Dose–response (threshold C\* / EC₅₀)
- **Wind tunnel** (e.g. 2 × 0.6 × 0.6 m, 0.2–0.3 m/s, 27 ± 1 °C, 70 % RH), 25 host-seeking, non-blood-fed *Aedes aegypti* (or local *Culex*/*Aedes*) females, 3–7 days old, per run; warm/CO₂ lure as attractant.
- Deliver **five known air concentrations** of the oil blend (e.g. 1, 10, 100, 1000, 10000 µg/m³ via syringe-pump vapour generator, verified by sorbent tubes) → landing/approach ratio vs clean air → **EC₅₀** and 95 % CI. This single measurement fixes **C\*** in the effective-radius model.
- Follow the design principles of WHO (2013) spatial-repellent guidelines (blinding, randomisation, replicates, negative control).

### L3. Treated-brick repellency
- Same tunnel; brick (treated vs C0/C1) beside the lure at 0.3 m and 1.0 m; measure landings and approaches over 10 min; **6 replicate runs per treatment per time point** (days 7, 30, 90, 180), positions randomised; scorer blind.
- **Metric:** repellency % = (C − T) / C × 100 on landing counts; analysis by negative-binomial GLMM with run as random effect (report effect size and CI, not just p).

### L4. Ant and crawling-insect barrier assay
- Local nuisance ants (*Monomorium*, *Tapinoma*, *Paratrechina* spp.): arena with sugar bait; the only access crosses a brick/skin strip (treated vs C0/C1); count crossings in 30 min × 8 replicates, days 7/30/90. Target ≥ 70 % fewer crossings. Repeat after weathering.

### L5. Mechanical, durability, and sealing
- **Compressive strength** EN 772-1/ASTM C140 at 7 and 28 d (≥ 10 units per batch, loaded on the bed face); **capillary absorption** EN 772-11; **dimensions/density**.
- **Wet–dry cycling** (20 cycles, 24 h wet/24 h 60 °C dry — also drives volatile loss, so measure flux before/after) and, for export markets, freeze–thaw per the relevant standard.
- **Efflorescence** (ASTM C67), **UV/xenon ageing** of the sealer (500 h) with colour change ΔE.
- **Abrasion** of treated face (brush test 100 cycles) with mass loss and flux change.

### L6. Safety and ecotoxicity
- **Leaching:** CEN/TS 16637-2 dynamic surface leaching (bricks immersed, eluate renewed at fixed intervals); GC-MS of oil markers in eluate → predicted environmental concentration (PEC).
- **Ecotox on eluate/oil:** *Daphnia magna* acute (OECD 202), algae (OECD 201), fish embryo or acute (OECD 203) if PEC/PNEC > 0.1; **honey-bee** acute contact/oral (OECD 214/213) on oil and on volatile exposure chamber (qualified lab); **plant** seedling emergence near treated bricks (OECD 208, local garden species).
- **Human/pet:** skin-sensitiser review of each oil (existing SDS + QSAR), patch-test via an accredited lab if any new claim; cat-safety review (no eugenol/thymol/carvacrol).
- **Odour panel:** ≥ 10 untrained assessors, 1 m, intensity scale 0–5, target ≤ 2.

## 5. Semi-field and field protocols

**Semi-field (screen-house, G2).** Two enclosures of 4 × 4 × 2.5 m; release 100 lab-reared females; compare landings on bait pads at 0.5 m from treated vs untreated walls, positions swapped daily (Latin square, 8 nights). Ethical constraint: use heated bait pads or a CO₂-baited trap; **do not use human landing catches** without ethics approval and malaria-risk assessment.

**Field pilot (G3, Al Khabourah school garden and one external site).** 6 treated + 6 untreated planter walls per site, ≥ 5 m apart, randomised positions, **rotated every 4 weeks** to cancel location bias. Monitoring every 2 weeks for 12 months: (i) ant trail counts and bait-card visits at 0.5 m; (ii) mosquito trap counts (CO₂ + lure) at 1.0 m; (iii) temperature/humidity loggers on brick face; (iv) sacrificial brick extraction at months 3/6/12 for residual active; (v) complaint log. Reapply sealer in half of the treated walls at month 6 to test the re-coat interval.

**Statistics.** Power for a 40 % reduction with CV ≈ 0.6 on count data and α = 0.05 needs ≈ 12–16 position-weeks per arm; the layout above provides ≈ 150. Analyse with GLMM (location, date as random effects), report rate ratios with 95 % CI. Pre-register the primary endpoint (ant crossings + mosquito trap counts) before unblinding.

## 6. Equipment and consumables (indicative)

- Mixer (Hobart-type) and moulds 20 × 10 × 10 cm; vacuum chamber; oven (≤ 105 °C, not for loaded materials); balance 0.01 g; climate chamber 25–55 °C; compression machine.
- Dynamic chamber glassware, mass-flow controllers, Tenax tubes, thermal-desorption GC-MS (or contracted lab).
- Wind tunnel with insectary access (university/health-ministry entomology partner); insect rearing records.
- Consumables: oils (≥ 3 batches with COA), diatomite/zeolite, gelatin/gum arabic/β-CD, transglutaminase, lime/silicate sealer, PPE, fire-safe cabinet.
- Partners to approach: a university civil/chemistry lab (mechanical, GC-MS), a medical-entomology unit, an accredited ecotox lab, and the competent Omani regulator (early consultation).

## 7. Reporting and data management

- One **brick traveler** per ID (Section 3.8) and one **results sheet** per test (raw counts/flux, operator, date, temperature).
- Re-run the simulation with measured parameters after G1; publish a revised flux/radius table; freeze the formulation only after G2.
- Archive: raw GC-MS files, bioassay video, extraction mass balances, batch COAs; retain samples 24 months.

## 8. Indicative timeline

| Month | 0–1 | 1–4 | 4–9 | 9–21 |
|---|---|---|---|---|
| Work | G0 screen, procurement | Prototypes, L1–L3 | Durability, ecotox, semi-field, regulatory consultation | Field pilot, re-coat trial, claim dossier |
| Output | Go/no-go on shell | Measured C\*, flux | Compliance report | Pilot report, product spec v2 |
