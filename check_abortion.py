from medusa.database import get_session, Case
session = get_session()
results = session.query(Case.summary, Case.city, Case.state).filter(
    Case.summary.ilike('%amber thurman%') |
    Case.summary.ilike('%candi miller%') |
    Case.summary.ilike('%amanda zurawski%') |
    Case.summary.ilike('%josseli%') |
    Case.summary.ilike('%abortion ban%died%') |
    Case.summary.ilike('%denied%abortion%died%') |
    Case.summary.ilike('%abortion%death%') |
    Case.summary.ilike('%miscarriage%denied%') |
    Case.summary.ilike('%ectopic%denied%')
).all()
print(f"{len(results)} matching records")
for r in results:
    print(f"  {r.city}, {r.state} — {r.summary[:80]}")
