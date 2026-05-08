from medusa.database import get_session, Case
session = get_session()
results = session.query(Case.summary, Case.source_name).filter(
    Case.summary.ilike('%sex offender registry%') |
    Case.summary.ilike('%NSOPW%') |
    Case.summary.ilike('%registered sex offender%') |
    Case.source_name.ilike('%registry%') |
    Case.summary.ilike('%Megan%law%')
).all()
print(f"{len(results)} matching records")
for r in results:
    print(f"  {r.source_name[:40]} — {r.summary[:70]}")
