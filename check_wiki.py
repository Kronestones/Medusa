from medusa.database import get_session, Case
session = get_session()
wiki = session.query(Case).filter(
    Case.source_name.ilike('%wikipedia%')
).count()
print(f"Wikipedia records: {wiki}")
total = session.query(Case).count()
print(f"Total records: {total}")
