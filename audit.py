from medusa.database import get_session, Case
session = get_session()

total = session.query(Case).count()
print(f"Total cases: {total}\n")

from sqlalchemy import func
types = session.query(Case.violence_type, func.count(Case.id)).group_by(Case.violence_type).order_by(func.count(Case.id).desc()).all()
print("BY TYPE:")
for t, c in types:
    print(f"  {t:25} {c}")

print("\nSAMPLE SUMMARIES BY KEYWORD:")
keywords = ['trafficking', 'stalker', 'online', 'deepfake', 'AI', 'prison', 'military', 'war', 'slavery', 'abortion provider', 'clinic bombing', 'foster', 'runaway']
for kw in keywords:
    count = session.query(Case).filter(Case.summary.ilike(f'%{kw}%')).count()
    print(f"  {kw:25} {count}")
