from medusa.database import get_session, Case
session = get_session()
results = session.query(Case.summary).filter(
    Case.summary.ilike('%marlise%') |
    Case.summary.ilike('%munoz%') |
    Case.summary.ilike('%life support%pregnant%') |
    Case.summary.ilike('%brain dead%pregnant%') |
    Case.summary.ilike('%incubator%') |
    Case.summary.ilike('%John Peter Smith%')
).all()
print(f"{len(results)} matching records")
for r in results:
    print(' -', r.summary[:80])
