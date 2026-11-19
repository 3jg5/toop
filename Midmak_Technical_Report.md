# Midmak — Insect-Repellent Recycled Brick
## Technical Report v1.0 (design stage, pre-laboratory)

<div dir="rtl" class="ar" markdown="1">

**ملخص تنفيذي (بالعربية).** مدماك مشروع طلابي لتحويل مخلفات البناء إلى طابوق وبلاط حدائق. هذا التقرير يقترح ميزة إضافية: **طبقة سطحية وظيفية** في الطابوق تحمل مواد نباتية طاردة (زيت السدر الأرزي وزيت حشيشة الليمون كأساس) وتُطلقها ببطء لتقليل اقتراب الحشرات وتجمّعها قرب الجدران وأحواض الحدائق. التوصية الهندسية: وضع المادة في **كبسولات حيوية مع طبقة ختم** داخل طبقة بسُمك نحو 10 مم، وليس خلطها في كتلة الطابوق، وتجديد الختم سنويًا. المحاكاة تُظهر أن التحرر المحكوم بالانتشار (مثل الحمل على حاملات مسامية) يتناقص مع الزمن ولا يصلح وحده، وأن التصميم ذا مخزن وغشاء (كبسولات) هو الوحيد الذي يبقي الانبعاث ثابتًا تقريبًا نحو 10 أشهر عند 25 °م، لكن عمره يهبط إلى نحو 4 أشهر عند 40 °م ونحو 7 أسابيع عند 55 °م. **مدى الأثر المتوقع قريب من الجدار (نحو متر في فناء محمي) وليس مظلة واسعة.** كل القيم الحركية في هذا التقرير **مفترضة** ولم تُقَس؛ المطلوب الآن مرحلة نماذج أولية ومختبر (انظر خطة النماذج الأولية).

</div>

> **Status statement.** This is a design-stage engineering package. Nothing here has been measured on a real brick. All kinetic parameters, thresholds, prices and emission factors are *assumed values* chosen from published orders of magnitude, so that the simulation shows **what the lab must achieve** and **which parameters decide success**. The word "validated" applies to the *method and the model's internal consistency*, not to repellent efficacy. No efficacy, safety or health claim should be made publicly before the tests in the Prototyping & Test Plan are completed.

---

## 1. Concept and design logic

**Goal.** Reduce the approach and aggregation of nuisance insects (mosquitoes, ants, flies, moths) near recycled-brick walls, planters and paving in gardens and green spaces, using plant-derived agents that are released gradually.

**What is physically realistic.** A brick wall is a *weak, long-lived, low-power* emitter. A 1 m² wall face releasing a few µg/s creates a repellent-relevant concentration only within about **0.5–1 m** in sheltered air, and only a *contact/landing-zone* effect in open, breezy air (Section 6). The product should therefore be positioned as **local deterrence near the surface** (e.g., planter walls, seating edges, door thresholds, ant trails along borders), not as an area repellent such as a coil or diffuser.

**Core design decisions**

| Decision | Choice | Reason |
|---|---|---|
| Where the active lives | **10 mm functional skin** on the exposed face (sandwich brick: structural core + skin) | Keeps core strength; puts the active where release occurs; allows re-coating |
| What carries it | Oil-loaded **porous carriers** (diatomite/zeolite/biochar) → **biopolymer microcapsules** → **silicate/lime sealer** | Pure diffusion matrices decay as t^-1/2 (Section 5); reservoir + membrane gives ~zero-order release |
| Which actives | **Cedarwood oil** (sesquiterpenes: low volatility, alkali-stable) + **citronella/lemongrass** fractions rich in geraniol/citronellol (higher volatility, fast onset) | Combines persistence and onset; avoids aldehyde-rich fractions inside cement (unstable at pH > 12) |
| Service model | **Re-coat the sealer/skin yearly** | Heat in Oman shortens life (Arrhenius); renewable surface is cheaper than a longer-life embedded system |

## 2. Candidate plant-derived repellents

| Agent | Main actives | Evidence / typical use | Volatility class | Stability in alkaline cement/geopolymer | Main concerns | Verdict |
|---|---|---|---|---|---|---|
| **Cedarwood oil** (*Juniperus virginiana*, *Cedrus atlantica*) | cedrol, thujopsene, α-cedrene | Moth, ant, tick and cockroach deterrent; used in closets, mulch | **Low** (sesquiterpenes, bp > 250 °C) | **Good** (alcohol + hydrocarbons) | Dermal sensitisation possible; aquatic toxicity | **Backbone** (persistence) |
| **Citronella oil** (*Cymbopogon winterianus/nardus*) | citronellal, geraniol, citronellol | Classic mosquito spatial repellent (candles, diffusers); effect lasts hours when neat | **Medium–high** (bp ≈ 205–230 °C) | Aldehydes **poor**; alcohols (geraniol, citronellol) **moderate** | Skin sensitisers (geraniol, citronellol); short life | **Onset fraction**, use alcohol-rich cut, add late |
| **Lemongrass oil** (*C. citratus*) | citral (geranial+neral) | Mosquito, fly and ant deterrent | Medium–high | **Poor** (citral degrades in strong acid/base) | Citral is a strong sensitiser | Surface coat only, not in the cement mix |
| **Lemon-eucalyptus / PMD** | p-menthane-3,8-diol | Best-documented plant-derived skin repellent | Low–medium | Good | Regulated active (biocide registration) → heavier approval | Phase 2 option |
| **Catnip oil** | nepetalactones | Strong lab mosquito repellency | Medium | Unknown | Cost; cat attraction in gardens | Not recommended (cost, pets) |
| **Peppermint oil** | menthol, menthone | Ant and spider deterrent | Medium–high | Moderate | Irritant; pets | Optional for ant-specific variant |
| Clove oil | eugenol | Strong, broad | Medium | Moderate | **Phytotoxic; retards cement setting; sensitiser** | **Exclude** from the mix |
| Thyme / oregano | thymol, carvacrol | Strong | Medium | Moderate | Thymol is bee-active; phytotoxic | **Exclude** near planting and hives |
| Neem | azadirachtin | Antifeedant, not volatile | Very low | Poor (UV, alkali) | Insecticidal regulation | Out of scope |
| Pyrethrins | pyrethrins | Insecticide | — | — | Highly toxic to bees and fish | **Exclude** (not a repellent) |

*Selection rule used:* choose agents that (i) are stable at pH 12–13.5, (ii) have a persistence class matching a 6–12 month goal, (iii) are not phytotoxic/bee-active at the expected air concentrations, (iv) are safe around children and pets, and (v) sit on a short, well-known regulatory path.

## 3. Incorporation methods

| Method | How | Strengths | Weaknesses | Use in Midmak |
|---|---|---|---|---|
| **Direct mixing** of neat oil | Add to wet mix | Simplest | Oil coats cement grains, retards setting, lowers strength, bursts out in days, partly destroyed by alkali | **Not recommended** (control formulation F0) |
| **Porous carrier loading** | Vacuum/soak oil into diatomite, zeolite (clinoptilolite), expanded perlite, biochar; add 1–3 % of mass | Cheap, local sourcing possible (biochar from agri waste); protects oil from paste | Diffusion-controlled → release decays as t^-1/2 | Carrier **inside** capsules/sealer (F1) |
| **β-Cyclodextrin inclusion complex** | Co-precipitate oil with β-CD (~10–15 wt % loading) | Thermally stable, sustained, food-grade | Costly (≈ 0.8 kg CD per 0.1 kg oil), loading low, release strongly humidity/temperature dependent | Option for premium variant (F2) |
| **Biopolymer microcapsules** | Complex coacervation (gelatin/gum arabic) or spray-drying (gum arabic + maltodextrin) or chitosan–alginate; 20–100 µm | Liquid core keeps constant vapour activity → **~zero-order** flux; shell tunable | Process cost; capsules must survive handling; alkaline attack on some shells | **Primary** (F3) |
| **Pickering emulsion / silica shell** | Oil droplets stabilised by silica or clay particles | Alkali-compatible, no synthetic polymer | Newer, needs optimisation | Backup if biopolymer shells fail in alkali |
| **Surface coating/sealer** | Lime-wash or silicate paint with capsules; water-based topcoat | Renewable by re-coating; keeps actives out of paste | Weathering, UV, abrasion | **Primary reservoir carrier** and rate-controlling membrane |
| Synthetic polymer shells (PMMA, polyurea, melamine) | Interfacial polymerisation | Robust | **Microplastics** concern: EU restriction on intentionally added synthetic polymer microparticles (Reg. (EU) 2023/2055) | **Avoid** (regulatory and environmental) |

## 4. Compatibility with brick manufacturing routes

| Route | Process conditions | What happens to a plant-oil active | Recommended integration |
|---|---|---|---|
| **Fired clay/ceramic brick** | 900–1100 °C | Everything organic burns off | **Post-fire only**: surface coat or vacuum impregnation of the fired brick (open porosity 10–20 %) with carrier/capsule slurry; no addition before firing |
| **Hydraulic cured (cement/lime, compacted RCA bricks and paving)** | Paste pH 12.5–13.5; hydration heat to 40–60 °C; moist curing 7–28 d | Aldehydes and esters degrade; phenolics retard set; high temperature drives volatile loss; gelatin shells can hydrolyse | **Sandwich brick**: cast the 10 mm skin last with pre-protected carriers (capsules or sealed carriers, ≤ 3 wt % of skin), add at the **end of mixing** (≤ 2 min), cure below 35 °C, then apply sealer. Check initial/final set (EN 196-3 / ASTM C191) for retardation |
| **Geopolymer (alkali-activated)** | NaOH/waterglass, pH > 13.5; thermal cure 40–80 °C for ~24 h | Strong base + heat: most oil lost or converted | **Do not add to the mix.** Impregnate or coat **after cure**; prefer sesquiterpene-rich cedarwood |
| **Existing product, retrofitted** | Ambient | Active in sealer only | Water-based **silicate or lime sealer with capsules**, applied on site; renewable yearly |

**Process rules (all routes):** keep flash-point-aware handling (oils have flash points roughly 70–110 °C → no ovens, hot-air dryers or open flames while loading); load oil into carriers *separately* from the brick line; never exceed 35 °C in curing for oil-bearing skins; record oil batch, carrier lot and capsule lot on the brick traveler.

## 5. Release-kinetics model and results

**Source terms.** Per 1 m² of wall face: skin thickness *L* = 10 mm, density 1900 kg/m³, active loading 0.5 wt % → **M₀ = 95 g/m²**.

**Model A (formulations F0–F2): Fickian release from a one-face-open slab**

F(t) = 1 − Σₙ [8 / ((2n+1)²π²)] · exp(−(2n+1)²π² D t / (4L²)),  Q(t) = M₀ · dF/dt,  D(T) = D₂₅ · exp[ Eₐ/R · (1/298.15 − 1/T) ]

**Model B (formulation F3): reservoir + membrane.** Liquid-core capsules hold vapour activity constant, so flux is constant until ~10 % of the oil remains, then decays first-order: Q = Q₀ · min(1, m/0.10), with Q₀ = M₀ / T_dep.

**Assumed parameters (to be replaced by TGA and headspace data)**

| Formulation | Model | D₂₅ (m²/s) or T_dep | Eₐ (kJ/mol) |
|---|---|---|---|
| F0 neat oil in porous skin | A | 1.0 × 10⁻¹¹ | 45 |
| F1 oil on diatomite/zeolite carrier | A | 4.0 × 10⁻¹³ | 50 |
| F2 β-CD complex + carrier | A | 1.5 × 10⁻¹³ | 65 |
| F3 biopolymer capsules + sealer | B | T_dep = 330 d at 25 °C (*design target*, i.e. the membrane permeance the lab must hit) | 55 |

**Results (simulation/summary_metrics.csv)** — service life = days with r_eff ≥ 0.5 m (sheltered air, C\* = 100 µg/m³):

| Formulation | 25 °C | 40 °C | 55 °C | Time to release 50 % at 25 °C |
|---|---|---|---|---|
| F0 | 105 d | 61 d | 35 d | 23 d |
| F1 | 33 d | 86 d | 162 d | 570 d |
| F2 | 12 d | 43 d | 133 d | > 730 d |
| **F3** | **314 d** | **120 d** | **50 d** | 165 d |

![Cumulative release](../simulation/fig1_cumulative_release.png)
![Emission flux](../simulation/fig2_emission_flux.png)

**Engineering reading of the results**

1. **Diffusion-only systems (F0–F2) cannot hold a flux window.** Flux falls as t^-1/2: either it is high at first and gone within weeks (F0) or it is below the useful flux for most of the year (F1, F2). The apparent "longer life" of F1/F2 at 55 °C only reflects over-emission at that temperature crossing the threshold, not good behaviour.
2. **A reservoir-and-membrane design (F3) is the only architecture that gives a flat flux** (≈ 0.29 g/day per m² at 25 °C, about 3.3 µg/s). The lab target is therefore a **shell/sealer permeance** that delivers ~0.2–0.4 g/day·m² at 25 °C.
3. **Temperature is the dominant risk in Oman.** F3 at 40 °C empties in ~4 months and at 55 °C (sun-heated face) in ~7 weeks. Mitigation: place functional faces in shade/north-facing, light-coloured silicate sealer (lower surface temperature), thicker shell or lower-volatility cut (more cedarwood), and plan a **yearly re-coat** or two capsule generations (fast + slow).
4. **Over-emission wastes active:** F3 at 40 °C releases ~3× the design flux (r_eff ≈ 3 m) — a temperature-responsive shell or a lower design flux at 25 °C is cost-efficient.

![Service life](../simulation/fig4_service_life.png)

## 6. Effective-radius model

Steady-state concentration around a ground-level source in turbulent air with eddy diffusivity *K*: **C(r) = Q / (2π K r)** (half-space point source; regularised with a source radius r₀ = √(A/2π) = 0.40 m for a 1 m² face). The *effective radius* is where C falls to a **threshold C\*** that gives a defined repellency (EC₅₀ to be measured in a wind tunnel; the model uses 10, 100 and 1000 µg/m³ as placeholders). *K* = 0.005 m²/s represents a sheltered courtyard; 0.05 m²/s an open, breezy garden.

| Case (25 °C, sheltered, C\* = 100 µg/m³) | 7 d | 30 d | 90 d | 180 d | 365 d |
|---|---|---|---|---|---|
| F0 neat oil | 6.9 m* | 3.2 m* | 0.8 m | 0 | 0 |
| F1 carrier | 1.3 m | 0.5 m | 0 | 0 | 0 |
| F2 β-CD | 0.8 m | 0.1 m | 0 | 0 | 0 |
| **F3 capsules + sealer** | **1.0 m** | **1.0 m** | **1.0 m** | **1.0 m** | 0 (depleted ~330 d) |

\* Early-time values of F0 are burst-flux upper bounds; the point-source model is not credible beyond a few metres, and real burst release is capped by surface evaporation.

![Effective radius](../simulation/fig3_effective_radius.png)

**Sensitivity.** (i) C\*: at 10 µg/m³ the F3 radius grows to ~10.6 m (threshold must be measured: this single number decides whether the product is a local deterrent or a small-area one); at 1000 µg/m³ the effect collapses to the contact zone. (ii) Airflow: at *K* = 0.05 m²/s every formulation has r_eff below the source radius → **effect is confined to the wall surface and its immediate boundary layer**. (iii) Wall area: Q scales with exposed area, so a 5 m² planter wall extends the radius by ~5×.

## 7. Target performance metrics (proposed; revise after Gate 1)

| # | Metric | Target | Method |
|---|---|---|---|
| 1 | Flux at 25 °C, months 1–9 | 0.2–0.4 g/day·m² (±30 %) | Headspace/dynamic chamber GC-MS |
| 2 | Retained active at 12 months (shade) | ≥ 15 % of M₀ before re-coat | Solvent extraction GC-MS |
| 3 | Lab spatial repellency (wind tunnel, *Aedes aegypti* or *Culex*) at 0.3 m | ≥ 60 % reduction in landings vs control (stretch 80 %) | WHO spatial-repellent guideline design |
| 4 | Ant barrier crossing (*Monomorium*/*Tapinoma*, local species) | ≥ 70 % fewer crossings for ≥ 90 d | Treated-substrate choice assay |
| 5 | Semi-field / field | ≥ 40 % reduction in landing/visits at 0.5 m vs untreated bricks, same site, rotated positions | Latin-square layout |
| 6 | Compressive strength of skinned brick | ≥ 90 % of control; mean ≥ class requirement | EN 772-1 / ASTM C140 |
| 7 | Capillary water absorption | ≤ +15 % vs control | EN 772-11 |
| 8 | Efflorescence / freeze–thaw (if exported) | No increase vs control | ASTM C67 / EN 772-18 as relevant |
| 9 | Ecotoxicity of leachate | No effect at 10× predicted environmental concentration for *Daphnia*, algae; bee contact/oral LD₅₀ margin ≥ 100× | OECD 202, 201, 213/214 |
| 10 | Odour | Perceived intensity ≤ "weak" at 1 m (panel of ≥ 10) | Sensory panel |

## 8. Safety and regulatory checklist

**Positioning and claims.** Describe as "insect-deterrent surface (nuisance insects)". **Do not** claim protection from disease, malaria/dengue vectors or "kills insects". Mosquito/vector claims, or any claim of repelling pests away from the article, can move the product from a "treated article" to a **biocidal/pesticidal product** needing registration.

| Item | Action |
|---|---|
| **Oman** | Confirm with the competent authorities (e.g., Environment Authority; Directorate General for Specifications and Standards) whether the brick is a construction product only or also a biocidal product; obtain written position before sale |
| **EU (if exported)** | Biocidal Products Regulation 528/2012: product type PT 19 (repellents); *treated article* rules; check whether the active is approved or in the review programme |
| **USA (reference)** | FIFRA; 40 CFR 152.25(f) minimum-risk list covers some oils (cedarwood, lemongrass, citronella) but with claim limits; vector claims generally excluded |
| **Chemicals** | REACH/CLP: SDS for each oil; skin sensitiser labelling for geraniol/citronellol/citral; aquatic toxicity classification; allergen declaration |
| **Microplastics** | Avoid synthetic polymer shells; document biodegradability of shells; check Reg. (EU) 2023/2055 |
| **Occupational** | Flash point, vapour exposure (ventilated mixing, nitrile gloves, respirator for powders), no ignition sources, spill kit, fire-safe storage |
| **Public safety** | Children and pets: patch/odour tests, cat-safety review (cats are sensitive to many phenolic/terpenoid oils); avoid eugenol/thymol/carvacrol; no edible-looking forms |
| **Ecology** | Bee (OECD 213/214), aquatic (OECD 201/202/203), terrestrial plant (OECD 208), earthworm (OECD 207) assessments before field rollout; no placement beside hives or ponds |
| **Construction standards** | Declare performance per EN 771-x (units) or national equivalent; document durability, fire reaction, and any change in strength; CPR/CE rules if exported |
| **Records** | Batch traceability for oils, carriers, capsules; COA for each oil (GC-MS fingerprint, no adulterants) |

*Regulatory statements above are a screening checklist, not legal advice; verify current texts with the regulator or a qualified consultant.*

## 9. Environmental impact (screening LCA) and cost

**Functional unit:** 1 m² of 100 mm wall face (190 kg/m², 10 % cement). **Baseline** GWP ≈ **16 kg CO₂e/m²** (cement 0.85 kg CO₂e/kg). **Screening-level** only: factors are assumed ranges, not an ISO 14040/14044 LCA with primary data.

| Formulation | Add-on cost (USD/m²) | Add-on GWP (kg CO₂e/m²) | Add-on vs baseline GWP |
|---|---|---|---|
| F0 neat oil | 2.4–5.7 | 0.2–0.8 | 1–5 % |
| F1 carrier | 2.5–6.0 | 0.3–1.0 | 2–6 % |
| F2 β-CD | 4.8–13.7 | 2.6–5.6 | 16–35 % |
| **F3 capsules + sealer** | **3.9–10.0** | **0.5–1.5** | **3–10 %** |

*Sources of the assumptions are in simulation/cost_lca.py; replace with supplier quotes and EPDs.* **Interpretation:** the oil is the dominant cost and carbon item in all cases (steam distillation, land use); β-CD is the carbon outlier. The add-on equals roughly a few USD per m² of wall, a premium that must be justified by the garden/hospitality market and by a **yearly re-coat service** (annual cost ≈ sealer + labour). **Environmental risks:** essential oils are toxic to aquatic life → keep runoff controlled; carriers (diatomite, zeolite) are mined, biochar from agricultural waste is the lowest-impact carrier; gum arabic and cellulose-based shells are renewable and biodegradable.

## 10. Quality-assurance criteria

| Stage | Control | Acceptance |
|---|---|---|
| Incoming oil | GC-MS fingerprint (cedrol/thujopsene; geraniol/citronellol; citral limit), refractive index, density, peroxide value | Within supplier spec ±10 % on key markers; no synthetic adulterants |
| Carrier / capsule | Particle size (D50 30–80 µm), oil loading, encapsulation efficiency, moisture, free oil on surface | Loading within ±5 % of spec; free oil ≤ 5 % |
| Mix / skin | Fresh density, flow, initial/final set | Set time change ≤ ±30 min vs control |
| Cured brick | Compressive strength, water absorption, dimensions, colour | ≥ 90 % of control; per EN 771-3 / ASTM C140 |
| Release | Flux at 25 °C (30-day and 90-day), mass balance by extraction | Flux window 0.2–0.4 g/day·m²; mass balance 85–115 % |
| Release (hot) | Flux at 40 °C, 7-day acceleration | Ratio to 25 °C ≤ 3.5 (matches design Eₐ) |
| Odour & appearance | Panel + visual | No staining, no tackiness, weak odour |
| Batch release | Retain samples; traveler with oil/carrier/capsule lot numbers | Complete traveler; retains stored 24 months |

## 11. Risks and open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Threshold C\* is much higher than assumed (> 1000 µg/m³) | Medium | Product only deters at contact distance | Measure EC₅₀ first (Gate 1); reposition as contact-zone deterrent |
| Shell fails in alkaline skin | Medium | Rapid burst | Silica-shell/Pickering backup; sealer-only (no cement contact) variant |
| Heat life too short | High (Oman) | Re-coat every ~4 months | Shade placement, reflective sealer, slower cut, two-generation capsules |
| Strength/set retardation | Low–medium | Non-compliant brick | Sandwich skin, ≤ 3 wt % carriers, set-time screening |
| Odour or pet/child complaints | Medium | Reputational | Sensory panel, low-allergen cut |
| Regulatory classification as biocide | Medium | Delay and cost | Early written position, careful claims |

## 12. References (starting set — verify current editions)

1. WHO (2013). *Guidelines for efficacy testing of spatial repellents.* Geneva.
2. OECD Test Guidelines 201, 202, 203, 207, 208, 213, 214 (ecotoxicity).
3. EN 771-1/-2/-3 (masonry units); EN 772-1 (compressive strength), EN 772-11 (capillary absorption), EN 772-18 (freeze–thaw); EN 196-3 (setting time); ASTM C140, C67, C191.
4. CEN/TS 16637-2 (dynamic surface leaching of construction products).
5. Regulation (EU) No 528/2012 (Biocidal Products); Regulation (EU) 2023/2055 (synthetic polymer microparticles); CLP Regulation (EC) 1272/2008.
6. US EPA, 40 CFR 152.25(f) (minimum-risk pesticides); EPA OCSPP 810 series (product performance).
7. ISO 14040/14044 (LCA); EN 15804 (EPD for construction products).
8. Nerio, A. et al. (2010). Repellent activity of essential oils: a review. *Bioresource Technology* 101, 372–378.
9. Crank, J. (1975). *The Mathematics of Diffusion*, 2nd ed. (slab release solution).
