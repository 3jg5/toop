# Midmak — "White Sand" Theme (Implementation Package)

## 1. Sampled colours (from the supplied image, 973 × 865 px)
Method: exact pixel histogram of the PNG (flat-colour artwork, no gradients). The background covers 804,713 px (≈ 95.6 %).

| Role | HEX | RGB | HSL | Source |
|---|---|---|---|---|
| **White sand (primary background)** | **`#FFE7C2`** | **255, 231, 194** | 36°, 100 %, 88 % | Page background |
| Maroon (wordmark body, accent) | `#790000` | 121, 0, 0 | 0°, 100 %, 24 % | Arabic letters م د ا + MIDMA |
| Deep maroon (wordmark first letter, ink) | `#3C0000` | 60, 0, 0 | 0°, 100 %, 12 % | Arabic letter ك |
| Navy (final K) | `#001F3C` | 0, 31, 60 | 210°, 100 %, 12 % | Latin K |

Derived tints (not in the image; chosen so every pairing passes AA):

| Token | HEX | Use |
|---|---|---|
| `--sand-soft` | `#FFF3DC` | Cards, tables, simulation shells (lighter than the page) |
| `--sand-deep` | `#F5D9AB` | Alternate section band (how-it-works), mobile menu |
| `--line` | `#E3C898` | Borders and dividers |
| `--mute` | `#6B2E22` | Secondary text |

## 2. Transcribed Arabic text (verbatim from the image)
The image contains one Arabic word set in a custom angular display lettering: **مدماك** (read right to left: م – د – م – ا – ك), with the Latin line **MIDMAK** below it (letter-spaced capitals, final **K** in navy). No other Arabic text appears in the image.

Placement: the lettering is **not typed text**; it was traced from the image into vector paths (`brand/sand/*.svg`, inline `<symbol id="midmak">` in `index.html`) so shape, weight, spacing and the two-tone ink are exactly as shown. The accessible name is supplied by `aria-label="مدماك"` and an SVG `<title>`; the plain text «مدماك» is used everywhere else in running copy.

## 3. Global theming — token diff (`index.html`, `<style>`)
```diff
-:root{--em:#10B981;--em-d:#047857;--rock:#64748B;--bg:#F4F6F5;--surf:#fff;--ink:#0F1A17;--mute:#475569;--line:#D9E0DD;--night:#0A1311;--night2:#0F2A22;
+:root{--sand:#FFE7C2;--sand-soft:#FFF3DC;--sand-deep:#F5D9AB;--em:#790000;--em-d:#3C0000;--rock:#001F3C;
+      --bg:var(--sand);--surf:var(--sand-soft);--ink:#3C0000;--mute:#6B2E22;--line:#E3C898;
+      --night:#3C0000;--night2:#6B0000;--on-em:#FFE7C2;color-scheme:light;
-@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0C1513;...}}   /* all 4 dark blocks removed: single sand theme */
 header{
-  background:rgba(10,19,17,.85); border-bottom:1px solid rgba(255,255,255,.08); color:#fff
+  background:rgba(255,231,194,.9); border-bottom:1px solid rgba(60,0,0,.14); color:var(--ink)
 .hero{
-  color:#fff; background:radial-gradient(...rgba(16,185,129,.32)...),linear-gradient(160deg,var(--night) 30%,var(--night2))
+  color:var(--ink); background:radial-gradient(900px 500px at 15% 85%,rgba(121,0,0,.12),transparent 60%),
+    radial-gradient(700px 420px at 90% 10%,rgba(0,31,60,.07),transparent 60%),linear-gradient(160deg,#FFE7C2 30%,#F8DDB0)
-.how{background:var(--night);color:#fff}        +.how{background:var(--sand-deep);color:var(--ink)}
-.btn{color:#03120b} .tab.on{color:#03120b}    +color:var(--on-em)
 footer / .call / .pitch  → deep maroon (--night) with sand text   (accent bands, as in the wordmark)
 simulation windows (.cv .scene .cs .sh .hs) → warm dark panels #4B1612→#240806 (maroon-brown), semantic water/plant colours kept
```
Full before/after files: `index.html`, `admin.html` (same tokens). Overlays: header/menu use `rgba(255,231,194,.9)` + `backdrop-filter`; safe-area bar `rgba(255,231,194,.96)`.

**Light/dark:** the site is now a single light theme (`color-scheme:light`); the OS dark-mode override was removed deliberately so the sand identity never inverts. If a dark variant is wanted later, reuse `--night` (#3C0000) as the page colour and `--sand` as ink (ratio 14.65:1).

## 4. Accessibility — WCAG 2.1 AA (computed)
| Pair | Foreground | Background | Ratio | Level |
|---|---|---|---|---|
| Body/headings | `#3C0000` | `#FFE7C2` | **14.65:1** | AAA |
| Body on cards | `#3C0000` | `#FFF3DC` | **16.03:1** | AAA |
| Body on alt band | `#3C0000` | `#F5D9AB` | **12.91:1** | AAA |
| Secondary text | `#6B2E22` | `#FFE7C2` | **8.56:1** | AAA |
| Secondary on cards | `#6B2E22` | `#FFF3DC` | **9.37:1** | AAA |
| Secondary on alt band | `#6B2E22` | `#F5D9AB` | **7.55:1** | AAA |
| Accent text / links / numbers | `#790000` | `#FFE7C2` | **9.63:1** | AAA |
| Accent on cards | `#790000` | `#FFF3DC` | **10.54:1** | AAA |
| Accent on alt band | `#790000` | `#F5D9AB` | **8.49:1** | AAA |
| Navy (K, 2nd numbers) | `#001F3C` | `#FFE7C2` | **13.84:1** | AAA |
| Button text | `#FFE7C2` | `#790000` | **9.63:1** | AAA |
| Footer / call-out text | `#FFE7C2` | `#3C0000` | **14.65:1** | AAA |
| Footer body | `#F3D5A6` | `#3C0000` | **12.48:1** | AAA |
| Error text (admin) | `#A4161A` | `#FFE7C2` | **6.45:1** | AA |

Automated audit of the rendered page (every text element, computed styles, 51 unique colour/size combinations): **0 failures; lowest ratio 6.83:1** (AA needs 4.5:1 normal, 3:1 large). Dark simulation panels use light text (≥ 12:1). **Fallback variants:** high-contrast ink `#2A0000` on `#FFE7C2` (17:1) and, for accent text on `--sand-deep`, use `--em-d` `#3C0000` (12.9:1) — both already available as tokens. Focus ring: 3 px `--em` (9.6:1 on sand). Colour is never the only signal (tags carry text; ring and labels in the simulation).

## 5. Typography and RTL
- **Headings:** Cairo 800/900 (matches the heavy angular wordmark). **Body/UI:** Tajawal 400/500/700. Both load from Google Fonts with `display=swap` (already in the page).
- **Fallback stack (added):** `Tajawal, "Noto Sans Arabic", "Segoe UI", Tahoma, system-ui, sans-serif`; headings `Cairo, Tajawal, "Noto Sans Arabic", "Segoe UI", Tahoma, sans-serif`. `text-rendering:optimizeLegibility` for Arabic ligatures.
- RTL: `<html lang="ar" dir="rtl">` unchanged; all spacing uses logical properties (`inset-inline`, `margin-inline`); numerals stay LTR via `.num{direction:ltr;unicode-bidi:isolate}`.
- Optional hardening: self-host Cairo/Tajawal WOFF2 (`font-display:swap`, `unicode-range` Arabic + Latin) to remove the Google Fonts dependency in Oman networks.

## 6. Other files changed
`admin.html` (sand tokens), `manifest.webmanifest` (`theme_color` and `background_color` `#FFE7C2`), `<meta name="theme-color">`, PWA icons regenerated (`icons/`: 192, 512, maskable 512, apple-touch 180) with the wordmark on sand, new logo files in `brand/sand/` (onsand, onsand-bg, ondark, mono-maroon SVG).

## 7. Responsive screenshots (`docs/screenshots/`)
`mobile-390-hero.png / -full.png`, `tablet-820-hero.png / -full.png`, `desktop-1280-hero.png / -full.png`, `admin-desktop-1280.png`. No horizontal overflow at 390, 820, 1280. *Note:* captured in a sandbox with no internet, so Google Fonts did not load and the system Arabic fallback was used; text widths will differ slightly with Cairo/Tajawal.

## 8. Deployment checklist
- [ ] Upload together: `index.html`, `admin.html`, `site-content.js`, `firebase-config.js`, `manifest.webmanifest`, `sw.js`, `icons/*`, `logo-*.png`.
- [ ] Hard-refresh / bump cache (service worker is empty; clear CDN cache for `index.html`, `manifest.webmanifest`, `icons/*`).
- [ ] Re-install the PWA (or clear site data) so the new icon and `theme_color` apply.
- [ ] Check `https://…/icons/icon-192.png` and `apple-touch-icon.png` return 200.
- [ ] Admin page opens and saves (Firebase config unchanged).
- [ ] Confirm Google Fonts loads (Network tab) or self-host.

## 9. QA checklist (cross-browser / device)
- [ ] Chrome, Edge, Firefox, Safari (macOS + iOS), Samsung Internet; latest two versions.
- [ ] Widths 360, 390, 768, 820, 1024, 1280, 1920; portrait/landscape on phones.
- [ ] RTL: nav order, burger menu, tables scroll horizontally on mobile, no clipped text.
- [ ] Header logo, hero logo, footer logo (sand version) render crisply at 1× and 2× DPR.
- [ ] Contrast spot-check with browser DevTools on: nav links, muted text on cards, tags, table headers, footer.
- [ ] Forced colours / Windows High Contrast and `prefers-reduced-motion` (animations off).
- [ ] OS dark mode does **not** change the page.
- [ ] Zoom 200 % and large text: layout intact.
- [ ] Simulations (rain, CO₂, shock, heat, repellent) draw on warm panels with readable labels.
- [ ] Lighthouse accessibility ≥ 95; print preview readable.
