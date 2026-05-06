from medusa.database import get_session, Case
session = get_session()

print("=== ICE / PREGNANT GIRLS ===")
results = session.query(Case.summary).filter(
    Case.summary.ilike('%pregnant%ICE%') |
    Case.summary.ilike('%ICE%pregnant%') |
    Case.summary.ilike('%detention%pregnant%minor%') |
    Case.summary.ilike('%unaccompanied%pregnant%') |
    Case.summary.ilike('%ORR%pregnant%')
).all()
print(f"{len(results)} records")
for r in results:
    print(' -', r.summary[:80])

print()
print("=== TRUCK STOP TRAFFICKING ===")
results2 = session.query(Case.summary).filter(
    Case.summary.ilike('%truck stop%') |
    Case.summary.ilike('%I-20%') |
    Case.summary.ilike('%interstate%traffick%') |
    Case.summary.ilike('%Flying J%') |
    Case.summary.ilike('%Pilot%traffick%') |
    Case.summary.ilike('%rest stop%traffick%')
).all()
print(f"{len(results2)} records")
for r in results2:
    print(' -', r.summary[:80])
