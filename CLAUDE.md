# water-systems (submodule — separate git repo)

Own remote: `github.com/vancouver-island-regional-database/water-systems`. Commit/push from inside this folder, not from VIRD root.

## Purpose

The "Water Systems Catalogue" — public disclosure mirror for regional water assets, WWTP/WTP compliance notices, DFO closure notices, and annual water reports. Deployed at `/water-systems/` on the live site. Includes `tol-wwtp/timeline.html`, a standalone timeline view. This is the most mature/developed data pipeline in the project — treat its CSV schema as the reference model when unifying schemas elsewhere.

## Data flow (in order)

1. **`../raw_documents/`** (VIRD root) — original source PDFs, may contain personal identifying info in metadata/text layer.
2. **`../water-systems/scrub.py`** (⚠️ path bug, see below) — uses PyMuPDF to black-bar-redact specific personal terms from the visible text layer of each PDF.
3. **`../vird-pipeline/fix_metadata.py`** (⚠️ path bug, see below) — strips PDF metadata fields (Author, Creator, Producer, Subject, Title, dates) after redaction.
4. **`../vird-pipeline/data/water-systems.csv`** — the master CSV. Full column set: `doc-title`, `link-status-for-code`, `file-name`, `source-url`, `jurisdiction`, `doc-date`, `Notes` (private), `Code Variations`, `doc-summary`, `doc-nb`, `p#1`–`p#8` / `p-description1`–`8` (numeric water-quality parameter + description pairs), `tag1`–`tag5`, `***LINK-STATUS***`, `xml-doc-title`, `cat-slug`, `xml-file-name`, `lastmod`.
5. **`../vird-pipeline/generator.py`** — reads the CSV + templates in `../vird-pipeline/snippets/` (`item-pdf-template.txt`, `sitemap-template.txt`, and per-status snippets for live/orphaned/403/404 link states), writes compiled output to `../vird-pipeline/staging/` (`compiled_ledger_batch.html`, `compiled_sitemap_batch.xml`).
6. **`files/`** — final clean PDFs served publicly.
7. **`index.html`** — the catalogue page itself (`index-old.html` kept alongside — check which is actually deployed before editing; don't assume `index.html` is current without diffing against what's live).

## ⚠️ Known bug — stale paths

`scrub.py`, `fix_metadata.py`, and `generator.py` all hardcode `/Users/betheapenny/Documents/Github/VIRD/vird-water-systems/...`. That folder doesn't exist anymore — it was renamed to `water-systems` (per root repo's git log). Until these three scripts are updated to point at `water-systems/files`, running them as-is will error or silently write to the wrong place. Fix before next pipeline run.

## Schema notes

- `Notes` (private) vs `doc-summary` (public) is the existing convention for keeping private research separate from public-facing text — this is the pattern to extend when building the public/private split described in the Preservation Archive doc, not a new mechanism to invent.
- `p#N`/`p-descriptionN` columns are for structured numeric readings (e.g. lab/turbidity values) — keep these as separate fields rather than folding them into free text; this structure is what lets you later chart/compare readings over time.
