# Water Systems — Design System Reference

Living reference for the visual language of the Water Systems Catalogue (`index.html`), pulled directly from the CSS variables and component patterns actually in use. Update this when a token or pattern changes — it should always describe what's really in the file, not an aspirational version of it.

Neutrality rule (from the root `CLAUDE.md`, applies to every component below): state facts, cite the primary source, avoid loaded language, even where the underlying documents are damning. Anything added to this design system should support reading as a credible, apolitical third party — not a "produced" or app-like experience.

## Color palette

| Token | Hex | Used for |
|---|---|---|
| `--bc-blue` | <span style="background:#003366;color:#fff;padding:1px 8px;border-radius:3px;">#003366</span> | Primary brand blue — buttons, links, hover states |
| `--bc-blue-dark` | <span style="background:#002244;color:#fff;padding:1px 8px;border-radius:3px;">#002244</span> | Darker brand blue — headers, footer, emphasis text |
| `--bc-gold` | <span style="background:#FCBA19;padding:1px 8px;border-radius:3px;">#FCBA19</span> | Accent gold — header border, focus rings |
| `--bc-gold-hover` | <span style="background:#e0a50d;padding:1px 8px;border-radius:3px;">#e0a50d</span> | Gold hover state |
| `--bg-canvas` | <span style="background:#F8FAFC;padding:1px 8px;border-radius:3px;border:1px solid #ddd;">#F8FAFC</span> | Page background |
| `--surface-card` | <span style="background:#FFFFFF;padding:1px 8px;border-radius:3px;border:1px solid #ddd;">#FFFFFF</span> | Card/panel background |
| `--text-main` | <span style="background:#1F2933;color:#fff;padding:1px 8px;border-radius:3px;">#1F2933</span> | Body text |
| `--text-muted` | <span style="background:#64748B;color:#fff;padding:1px 8px;border-radius:3px;">#64748B</span> | Secondary text — `.year-marker-label` default, dates |
| `--text-dark` | <span style="background:#475569;color:#fff;padding:1px 8px;border-radius:3px;">#475569</span> | One step darker than `--text-muted` — currently on `.key-event-marker-date` |
| `--border-light` | <span style="background:#E2E8F0;padding:1px 8px;border-radius:3px;border:1px solid #ddd;">#E2E8F0</span> | Card borders, empty/unpopulated `.year-marker` lines |
| `--border-medium` | <span style="background:#CBD5E1;padding:1px 8px;border-radius:3px;border:1px solid #ddd;">#CBD5E1</span> | Populated `.year-marker` line (default state) |
| `--border-dark` | <span style="background:#94A3B8;padding:1px 8px;border-radius:3px;">#94A3B8</span> | One step darker than `--border-medium` — for markers that need to read as related-but-distinct |
| `--accent-blue-soft` | <span style="background:#EFF6FF;padding:1px 8px;border-radius:3px;border:1px solid #ddd;">#EFF6FF</span> | Quote badges, key-point reference tags |

## Status colors

Finalized 5-state taxonomy. Two axes, not one: whether the address *loads* (a code fact) and whether it's *findable* through normal navigation (a separate, non-code fact). Hidden (403) and Absent (404) intentionally share one color — both mean "you can't see it," a hard line rather than a sliding scale like the other three. Icon + label are the only differentiator between them; no new color token was added for Hidden (403), it reuses `absent`'s triplet directly.

Wording rule for all five: describe the transaction, never the actor's intent. See `authority-classes.md`'s sibling doc (private context, not in this repo) for the full reasoning — the short version is every word here has already been fought over once, don't casually reword these.

| Status | Badge | Description (goes in the lightbox's Link Status field) | bg | text | border |
|---|---|---|---|---|---|
| `live` | `✓ LIVE (200)` | "Available at the original web address." | `#E6F4EA` | `#137333` | `#A8DAB5` |
| `delisted` | `⊘ DELISTED (200)` | "The path is still active via direct query ID, but has been unlinked from public indexing and layout directories." | `#FEF7E0` | `#B06000` | `#FAD28C` |
| `hidden403` | `🔒 HIDDEN (403)` | "This link has been actively restricted/hidden by the source website." | `#FCE8E6` | `#C5221F` | `#F5B4B1` |
| `absent` | `✕ ABSENT (404)` | "This link has broken or been removed entirely from the source website." | `#FCE8E6` | `#C5221F` | `#F5B4B1` |
| `unpublished` | `◌ UNPUBLISHED` | "No verified public release. Document absent from local government records." | `#DCE0E3` | `#3C4043` | `#C6CBCF` |

Notes:
- "Absent," not "removed" — removed implies someone's action; absent doesn't. The one place "removed" is still allowed is inside the Absent description itself ("broken **or** been removed"), because the "or" is what makes it safe — it's offering two possible causes side by side, not asserting one.
- Delisted's description deliberately doesn't say "intentionally" unlinked. The fact pattern (still resolves, removed from every navigable path) already implies a choice without the word doing that work for it.
- Every Primary Source link stays a real, clickable `<a href>` even when the status is known-broken (Delisted/Hidden/Absent) — never `.source-action-button.disabled`. Letting someone click through and hit the wall themselves is treated as part of the evidence, not a UX problem to smooth over. The one exception is Unpublished, where there's no known address to link in the first place.
- HTTP codes in badges should reflect what was actually observed per document, not a stock label — "(200)" on Live/Delisted and "(404)" on Absent are examples, not defaults to copy blindly. Verify before publishing.

## Other tokens

| Token | Value |
|---|---|
| `--shadow-sm` | `0 1px 2px 0 rgba(0,0,0,0.05)` |
| `--shadow-md` | `0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -2px rgba(0,0,0,0.05)` |
| `--shadow-lg` | `0 10px 15px -3px rgba(0,0,0,0.08), 0 4px 6px -4px rgba(0,0,0,0.08)` |
| `--transition-smooth` | `all 0.25s cubic-bezier(0.4, 0, 0.2, 1)` |

## Typography

Font stack: `'Inter', 'BCSans', 'Helvetica Neue', Arial, sans-serif`. Inter is the workhorse everywhere; nothing else is loaded.

| Element | Size | Weight | Notes |
|---|---|---|---|
| `.doc-card h5` (title) | card default | 600–700 | |
| `.doc-card h6` (doc ID) | small, uppercase-adjacent | 700 | |
| `.doc-card p` (description) | body | 400–500 | |
| `.year-marker-label` | 16px | 600 | |
| `.key-event-marker-date` | 11px | 700, uppercase, letter-spacing 0.03em | |
| `.key-event-marker-title` | 12px | 600 | |
| `.lightbox-section-label` | 11px | 700, uppercase, letter-spacing 0.04em | |

## Component inventory

Reference markup for every card state lives in **`style-guide.html`** (its own standalone file as of this writing — split out of `index.html`, which had been carrying the wireframe/reference material inline since the page's earliest wireframing days). It's a fully self-contained page (own copy of the stylesheet, own asset paths) so it renders correctly on its own — check there before building a new variant rather than reverse-engineering one from the live timeline. It will drift from `index.html`'s actual CSS over time; treat this doc, not that file, as the source of truth for tokens.

- **`.doc-card`** — the base unit. Status bar (top, 4px, colored by status) + date row + body (ID/title/description) + footer (authority icon + org name, colored by `authority-*` class). See `authority-classes.md` for the authority color/icon registry.
- **`.status-badge`** — pill badge, one of `live` / `orphaned` / `absent` / `unpublished` / `quote`.
- **`.month-stack` / `.month-stack-expanded`** — density stacking for months with 3+ documents. Front card + ghost cards imply depth; expanding shows the full list. The front card duplicates the first expanded card — don't count both when extracting data.
- **`.year-marker`** — per-year divider + label spanning both row bands. Collapses to a hatched strip when a year has no content in either row.
- **`.key-event-marker`** — non-document milestones (e.g. WWTP Grand Opening) placed inline at their exact chronological position. Currently a pale palette matching the unpopulated `.year-marker` line (`--border-light` line, `--text-dark`/`--text-muted` text) rather than the original gold/navy.
- **`.doc-lightbox`** (prototype) — native `<dialog>`-based detail view, now living in `style-guide.html` alongside the Card Type Reference Deck rather than in `index.html`. Holds the content that doesn't fit on the card face: link status description (mandatory), disclaimer/note (optional), extracted key points, and the three source/mirror/archive links. See `#lightbox-demo` in `style-guide.html` for the working example before it's promoted to real cards.

## Layout notes

- The timeline is a single CSS Grid (`grid-auto-flow: column`, 2 fixed row bands) — row height is shared across **every** column in that row band, which is why an inline-expanding component (like a native `<details>` accordion) would shift the whole row, not just its own card. This is why the lightbox pattern was chosen over an inline expand for card detail.
- `padding-top` on `.matrix-grid-flex` exists specifically to reserve headroom for whatever sits above row 1 (year labels, key-event labels) — if you add another marker type with its own floating label, budget for it here too rather than letting it float into negative space and hope.
