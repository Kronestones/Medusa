from medusa.database import get_session, Case
session = get_session()
results = session.query(Case.summary).filter(
    Case.summary.ilike('%AI%')
).limit(20).all()
print("Sample AI matches:")
for r in results:
    print(' -', r.summary[:100])
