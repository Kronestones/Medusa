from medusa.database import get_session, Case
session = get_session()

results = session.query(Case.summary, Case.city, Case.state).filter(
    Case.violence_type == 'child_abuse'
).order_by(Case.date_incident.desc()).limit(30).all()

print(f"Child abuse records: {session.query(Case).filter(Case.violence_type=='child_abuse').count()}")
print()
for r in results:
    print(f"  {r.city}, {r.state} — {r.summary[:80]}")
