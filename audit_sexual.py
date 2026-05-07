from medusa.database import get_session, Case
from sqlalchemy import func
session = get_session()

print("=== SEXUAL ASSAULT AUDIT ===\n")

# Total counts
total_sa = session.query(Case).filter(
    Case.violence_type.in_(['sexual_assault', 'rape'])
).count()
print(f"Total rape/sexual assault records: {total_sa}")

# Check key perpetrators
names = [
    'Cosby', 'Weinstein', 'Sandusky', 'Penn State',
    'R. Kelly', 'Kelly', 'USA Swimming', 'Nassar',
    'Hadden', 'Tyndall', 'Strauss',
    'rape kit', 'backlog',
    'date rape', 'rohypnol', 'GHB',
    'athlete', 'football', 'basketball',
    'Epstein', 'Maxwell',
]

print("\n=== KEY PERPETRATORS / TOPICS ===")
for name in names:
    count = session.query(Case).filter(
        Case.summary.ilike(f'%{name}%')
    ).count()
    if count > 0:
        print(f"  ✓ {name:25} {count} records")
    else:
        print(f"  ✗ {name:25} MISSING")

print("\n=== SAMPLE SEXUAL ASSAULT RECORDS ===")
results = session.query(Case.summary, Case.city, Case.state).filter(
    Case.violence_type.in_(['sexual_assault', 'rape'])
).order_by(Case.date_incident.desc()).limit(20).all()
for r in results:
    print(f"  {r.city}, {r.state} — {r.summary[:70]}")
