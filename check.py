from medusa.database import get_session, Case
session = get_session()
results = session.query(Case.summary).filter(
    Case.summary.ilike('%pornhub%') |
    Case.summary.ilike('%mindgeek%') |
    Case.summary.ilike('%Renee%') |
    Case.summary.ilike('%62 million%')
).all()
print(len(results), 'matching records')
for r in results:
    print(' -', r.summary[:80])
