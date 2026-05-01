# Medusa — Every Act Documented.
**Version 1.3.0**
Built on Project Themis · Founded by Krone the Architect · Powers Tracey Lynn · 2026

---

Medusa documents every reported act of male violence against women and children
in the United States. Every public record. Every credible source. Every case
pinned to the map.

Court filings. DOJ prosecutions. Congressional records. Civil judgments.
News archives. FBI statistics. Title IX findings. State AG announcements.
Wikipedia homicide records. Wikipedia femicide lists.

Politicians. Judges. Officers. Anyone the public record names.

Cast wide. Let sources speak.

---

## How to Run

```bash
pip install -r requirements.txt
export DATABASE_URL=postgresql://user:pass@host/db

python main.py              # Web server (port 5050)
python main.py --scan       # Scan all public sources now
python main.py --status     # Case counts by type
python main.py --export cases.json
> EOF
~/medusa $
