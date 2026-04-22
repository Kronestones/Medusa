# Medusa — Every Act Documented.
**Version 1.0.0**  
Built on Project Themis · Founded by Krone the Architect · Powers Tracey Lynn · 2026

---

Medusa documents every reported act of male violence against women in the United States.
Every public record. Every credible source. Every case pinned to the map.

Police reports. Court filings. Congressional records. Civil suits.
News archives. DOJ and FBI announcements. Title IX findings.
Politicians. Judges. Officers. Anyone the public record names.

Cast wide. Let sources speak.

---

## How to Run

```bash
pip install -r requirements.txt
export DATABASE_URL=postgresql://user:pass@host/db

python main.py              # Web server (port 5050)
python main.py --scan       # Scan public records now
python main.py --status     # Case counts by type
python main.py --export cases.json
```

## Deploy to Render

The `render.yaml` provisions a Postgres database and web service automatically.
Set `DATABASE_URL` via Render's environment dashboard or use the linked DB in render.yaml.

---

## Case Types

| Type | Color | Notes |
|------|-------|-------|
| Homicide / Femicide | Dark Red | |
| Attempted Murder | Red | |
| Rape | Deep Purple | |
| Sexual Assault | Purple | |
| Domestic Violence | Dark Orange | |
| Assault | Orange | |
| Stalking | Blue | |
| Harassment | Light Blue | |
| Human Trafficking | Teal | |
| Coercive Control | Grey | |

## Status Tags

| Tag | Meaning |
|-----|---------|
| `reported` | Filed with police or reported in news |
| `charged` | Perpetrator charged |
| `convicted` | Convicted in court |
| `acquitted` | Acquitted or charges dropped |
| `civil_judgment` | Civil court finding |
| `credible_allegation` | Credible public allegation, not yet charged |
| `congressional_record` | Appears in congressional/ethics record |
| `unknown` | Status unclear from available sources |

## Public Figures

Cases where the perpetrator is a politician, government official, law enforcement
officer, judge, or other public servant are automatically flagged with an **Official**
badge. They are searchable via the "Officials" tab in the sidebar.

Sources searched for officials specifically:
- Congressional ethics committee records
- State legislative ethics investigations
- Law enforcement internal affairs records (publicly disclosed)
- Court records
- Investigative journalism (ProPublica, Marshall Project, local outlets)

---

## Scanner

The `MedusaScanner` runs 4 focused search queries per scan cycle using the Claude API
with the `web_search_20250305` tool:

1. General recent cases (all types)
2. Politicians and government officials specifically
3. Recent court convictions and charges
4. Civil suits, Title IX, and institutional records

Each query geocodes results via OpenStreetMap Nominatim (no API key required)
and generates a stable `MEDUSA-YYYY-XXXXXXXX` case ID to prevent duplicates.

---

## Architecture

Adapted from Project Themis v1.1.0:

| Themis | Medusa |
|--------|--------|
| `database.py` | `database.py` (cases table) |
| `argos.py` (RF scanner) | `scanner.py` (web search + AI) |
| `web.py` | `web.py` |
| `templates/map.html` | `templates/map.html` |

---

No victim names stored. Sources always cited.  
The documentation does not stop.
