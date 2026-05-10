from medusa.database import get_session, Case
session = get_session()

bad = session.query(Case.case_id, Case.summary).filter(
    Case.summary.ilike('%alien smuggling%') |
    Case.summary.ilike('%smuggling organization%') |
    Case.summary.ilike('%Pervis Payne%') |
    Case.summary.ilike('%warden%respondent%') |
    Case.summary.ilike('%illegal alien%') |
    Case.summary.ilike('%appellate%civil procedure%')
).all()
print(f"Bad records found: {len(bad)}")
for r in bad:
    print(f"  {r.case_id} — {r.summary[:70]}")
