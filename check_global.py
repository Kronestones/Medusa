from medusa.database import get_session, Case
session = get_session()

results = session.query(Case.summary, Case.state, Case.city).filter(
    Case.summary.ilike('%global%') |
    Case.summary.ilike('%worldwide%') |
    Case.summary.ilike('%WHO%') |
    Case.summary.ilike('%international%') |
    Case.summary.ilike('%comfort women%') |
    Case.summary.ilike('%montreal massacre%')
).limit(20).all()
print(f"{len(results)} matching records")
for r in results:
    print(f"  {r.state} — {r.summary[:70]}")
