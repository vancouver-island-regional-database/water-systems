# Authority Classes — Tracking Sheet

Registry of every `authority-*` class used on `.doc-card` / `.doc-card-footer` / `.stack-count-badge`, so a new jurisdiction can be added consistently instead of improvised per-card. Update this file in the same commit that adds a new class.

Icon files live in `vancouver-island-regional-database.github.io/assets/`, referenced from `water-systems/index.html` as `../vancouver-island-regional-database.github.io/assets/fav_*.png`. Naming convention: `fav_<abbreviation>.png`.

## Tier vs. entity — the actual rule

Not every class should be named the same way. The deciding question: **does a real, official, shared visual identity exist above the individual org, or is the org's color its own?**

- **Federal and provincial stay as shared tiers.** Canada's Federal Identity Program and BC's provincial visual identity standards both mandate one unified color across every department underneath them — that's *why* DFO and any other federal body already share the same navy. Grouping by tier here reflects a real policy, not a shortcut.
- **Everything else gets its own entity-specific class.** A municipality, a regional district, a school district, and a First Nation are each their own body with their own independent branding — there's no "municipal blue" the way there's a "BC blue." Lumping Ladysmith, CVRD, and RDN under one `authority-municipal`/`authority-regional` class would mean either picking one color to represent multiple unrelated organizations, or constantly overriding it per-card — same problem SD68 already ran into.

## Active

| Class | Tier or entity | Represents | Example issuing org(s) seen in the data | Color | Hex | Icon file |
|---|---|---|---|---|---|---|
| `authority-federal` | Tier | Government of Canada (all departments) | Fisheries and Oceans Canada (DFO) | <span style="background:#26374A;color:#fff;padding:1px 8px;border-radius:3px;">#26374A</span> | `#26374A` | `fav_gov-ca.png` |
| `authority-provincial` | Tier | Province of British Columbia (all ministries/agencies) | BC Environmental Assessment Office | <span style="background:#1A5A96;color:#fff;padding:1px 8px;border-radius:3px;">#1A5A96</span> | `#1A5A96` | `fav_bc-ca.png` |
| `authority-municipal` *(→ rename to `authority-ladysmith`, see Renames Needed)* | Entity | Town of Ladysmith | Town of Ladysmith | <span style="background:#0885AD;color:#fff;padding:1px 8px;border-radius:3px;">#0885AD</span> | `#0885AD` | `fav_ladysmith.png` |

Federal/provincial colors match each government's own official brand color (GC navy, BC blue) — keep that pattern; it makes the color itself citable/verifiable, not decorative. Entity colors should match that specific org's own logo/brand color the same way (Ladysmith's teal already does).

## Fallback (not a real tier)

| Icon file | Used when |
|---|---|
| `fav_w.png` | Generic/unknown-org fallback — currently only seen on `.doc-card.status-unpublished` example in the Card Type Reference Deck, footer background falls back to `var(--text-muted)` instead of an authority color |

## Renames needed (not yet done — confirm before touching `index.html`)

| From | To | Why |
|---|---|---|
| `authority-municipal` | `authority-ladysmith` | It's already Ladysmith's own color, not a generic municipal one. Renaming now, while there's only one entity in it, is far cheaper than after CVRD/RDN cards exist and something is (incorrectly) sharing the class |

## Planned

| Class | Tier or entity | Represents | Color | Hex | Icon file | Status |
|---|---|---|---|---|---|---|
| `authority-cvrd` | Entity | Cowichan Valley Regional District | — | — | — | Needed — color/icon not yet sourced |
| `authority-rdn` | Entity | Regional District of Nanaimo | — | — | — | Needed — color/icon not yet sourced |
| `authority-sd68` | Entity | School District 68 (Nanaimo-Ladysmith) | <span style="background:#5f7d3e;color:#fff;padding:1px 8px;border-radius:3px;">#5f7d3e</span> | `#5f7d3e` | `fav_sd68.png` *(not yet added)* | Color confirmed, icon sourced (below), not yet wired in |
| `authority-stzuminus` | Entity | Stz'uminus First Nation | — | — | — | Needed — color/icon not yet sourced |

All four come from the root project's jurisdiction list (Town of Ladysmith, CVRD, RDN, SD68, Stz'uminus First Nation) — CVRD/RDN/Stz'uminus aren't in the water-systems data yet, but worth reserving the row now that the naming question came up.

**SD68 favicon candidates found** (from `https://www.sd68.bc.ca/`'s own `<link rel="icon">` tags, live DOM — not a guess):

- `https://www.sd68.bc.ca/wp-content/uploads/NLPS_logo-150x150.png` — 32×32, what the browser tab actually uses
- `https://www.sd68.bc.ca/wp-content/uploads/NLPS_logo.png` — 192×192 / apple-touch-icon, full-res version of the same colored logo (name + fish graphic)

Neither has been downloaded into `assets/` yet — say the word and I'll pull one in as `fav_sd68.png` (stating source/size first), or grab it yourself from either URL above.

## Optional: keeping a tier concept without forcing shared colors

If something later needs to know "is this any kind of local government" without enumerating every entity class (filtering, grouping, etc.), that's a separate, additive concern from color — e.g. a `data-tier="local-government"` attribute alongside the entity class, rather than folding it back into the class/color system. Not needed yet; noting it so the entity-based rename above doesn't get reversed later for the wrong reason.
