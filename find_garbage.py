from medusa.database import get_session, Case
session = get_session()

# Find records that don't belong
garbage = session.query(Case.case_id, Case.summary, Case.source_name).filter(
    Case.summary.ilike('%chick-fil-a%') |
    Case.summary.ilike('%gubernatorial%') |
    Case.summary.ilike('%vineyard%leesburg%') |
    Case.summary.ilike('%mac-and-cheese%') |
    Case.summary.ilike('%frontrunner%') |
    Case.summary.ilike('%battle spotted%') |
    Case.summary.ilike('%fake news%') |
    Case.summary.ilike('%stock market%') |
    Case.summary.ilike('%bitcoin%') |
    Case.summary.ilike('%recipe%') |
    Case.summary.ilike('%restaurant%review%')
).all()

print(f"Potential garbage records: {len(garbage)}")
for r in garbage:
    print(f"  {r.case_id} — {r.summary[:80]}")
