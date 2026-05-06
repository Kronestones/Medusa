from medusa.database import get_session, Case
session = get_session()
results = session.query(Case.summary).filter(
    Case.summary.ilike('%chainsaw%') |
    Case.summary.ilike('%hysteria%') |
    Case.summary.ilike('%hysteri%') |
    Case.summary.ilike('%lobotomy%') |
    Case.summary.ilike('%vibrator%') |
    Case.summary.ilike('%asylum%women%') |
    Case.summary.ilike('%thalidomide%') |
    Case.summary.ilike('%DES%diethyl%') |
    Case.summary.ilike('%twilight sleep%') |
    Case.summary.ilike('%symphysiotomy%')
).all()
print(f"{len(results)} matching records")
for r in results:
    print(' -', r.summary[:80])
