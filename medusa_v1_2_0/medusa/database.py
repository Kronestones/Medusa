"""
database.py — Medusa

PostgreSQL persistence layer.
Stores documented cases of male violence against women in the US.
Sources: police reports, court records, news archives, congressional
records, DOJ/FBI databases, civil suits, credible journalism.

No victim names stored. Sources always cited.
Cast wide — let sources speak.

Built on Project Themis architecture.
"""

import os
import json
from datetime import datetime, timezone
from sqlalchemy import (
    create_engine,
    Column, String, Float, DateTime, Boolean, Integer, Text
)
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()


# ── Model ─────────────────────────────────────────────────────────────────────

class Case(Base):
    __tablename__ = "cases"

    id              = Column(Integer, primary_key=True, autoincrement=True)
    case_id         = Column(String(64), unique=True, nullable=False)

    # What happened
    violence_type   = Column(String(64), nullable=False)
    # homicide | assault | sexual_assault | stalking |
    # trafficking | domestic_violence | rape | harassment |
    # attempted_murder | child_abuse | coercive_control

    summary         = Column(Text, nullable=True)    # factual, no victim name
    status          = Column(String(64), default="reported")
    # reported | charged | convicted | acquitted | civil_judgment |
    # credible_allegation | congressional_record | unknown

    is_public_figure = Column(Boolean, default=False)
    # True if perpetrator is politician, official, celebrity, etc.

    # When
    date_incident   = Column(DateTime(timezone=True), nullable=True)
    date_reported   = Column(DateTime(timezone=True), nullable=True)

    # Where
    city            = Column(String(128), nullable=False)
    state           = Column(String(64), nullable=False)
    lat             = Column(Float, nullable=True)
    lng             = Column(Float, nullable=True)

    # Source
    source_url      = Column(Text, nullable=True)
    source_name     = Column(String(256), nullable=True)
    # Additional sources (JSON array of {url, name})
    additional_sources = Column(JSONB, nullable=True)

    verified        = Column(Boolean, default=False)
    created_at      = Column(DateTime(timezone=True),
                             default=lambda: datetime.now(timezone.utc))
    extra           = Column(JSONB, nullable=True)


# ── Engine ────────────────────────────────────────────────────────────────────

def get_engine():
    url = os.environ.get("DATABASE_URL", "")
    if not url:
        raise RuntimeError("DATABASE_URL not set")
    return create_engine(
        url,
        pool_pre_ping=True,
        pool_recycle=300,
        pool_size=5,
        max_overflow=10,
    )


def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()


def init_db():
    engine = get_engine()
    Base.metadata.create_all(engine)
    print("[Medusa DB] Tables initialized.")


# ── Writes ────────────────────────────────────────────────────────────────────

def save_case(case_dict: dict) -> bool:
    session = get_session()
    try:
        existing = session.query(Case).filter_by(
            case_id=case_dict.get("case_id")
        ).first()
        if existing:
            return False

        date_incident = case_dict.get("date_incident")
        if isinstance(date_incident, str):
            try:
                date_incident = datetime.fromisoformat(date_incident)
            except Exception:
                date_incident = None

        core_keys = {
            "case_id", "date_incident", "date_reported", "violence_type",
            "city", "state", "lat", "lng", "summary", "source_url",
            "source_name", "status", "verified", "is_public_figure",
            "additional_sources",
        }
        extra = {k: v for k, v in case_dict.items() if k not in core_keys}

        row = Case(
            case_id            = case_dict["case_id"],
            violence_type      = case_dict.get("violence_type", "unknown"),
            summary            = case_dict.get("summary", ""),
            status             = case_dict.get("status", "reported"),
            is_public_figure   = case_dict.get("is_public_figure", False),
            date_incident      = date_incident,
            date_reported      = datetime.now(timezone.utc),
            city               = case_dict.get("city", "Unknown"),
            state              = case_dict.get("state", "Unknown"),
            lat                = case_dict.get("lat"),
            lng                = case_dict.get("lng"),
            source_url         = case_dict.get("source_url", ""),
            source_name        = case_dict.get("source_name", ""),
            additional_sources = case_dict.get("additional_sources"),
            verified           = case_dict.get("verified", False),
            extra              = extra if extra else None,
        )
        session.add(row)
        session.commit()
        return True

    except Exception as e:
        session.rollback()
        print(f"[DB] save_case error: {e}")
        return False
    finally:
        session.close()


# ── Reads ─────────────────────────────────────────────────────────────────────

def get_cases(limit=2000, violence_type=None, state=None,
              public_figure=None) -> list:
    session = get_session()
    try:
        q = session.query(Case)
        if violence_type:
            q = q.filter(Case.violence_type == violence_type)
        if state:
            q = q.filter(Case.state == state)
        if public_figure is not None:
            q = q.filter(Case.is_public_figure == public_figure)
        rows = q.order_by(Case.date_incident.desc()).limit(limit).all()
        return [_to_dict(r) for r in rows]
    except Exception as e:
        print(f"[DB] get_cases error: {e}")
        return []
    finally:
        session.close()


def get_case_count() -> int:
    session = get_session()
    try:
        return session.query(Case).count()
    except Exception:
        return 0
    finally:
        session.close()


def get_stats() -> dict:
    session = get_session()
    try:
        total = session.query(Case).count()
        by_type = {}
        for vt in [
            "homicide", "assault", "sexual_assault", "stalking",
            "trafficking", "domestic_violence", "rape", "harassment",
            "attempted_murder", "child_abuse", "coercive_control",
        ]:
            by_type[vt] = session.query(Case).filter(
                Case.violence_type == vt
            ).count()
        public_figures = session.query(Case).filter(
            Case.is_public_figure == True
        ).count()
        return {
            "total": total,
            "by_type": by_type,
            "public_figures": public_figures,
        }
    except Exception as e:
        print(f"[DB] get_stats error: {e}")
        return {"total": 0, "by_type": {}, "public_figures": 0}
    finally:
        session.close()


# ── Serializer ────────────────────────────────────────────────────────────────

def _to_dict(row: Case) -> dict:
    return {
        "id":                  row.id,
        "case_id":             row.case_id,
        "violence_type":       row.violence_type,
        "summary":             row.summary,
        "status":              row.status,
        "is_public_figure":    row.is_public_figure,
        "date_incident":       row.date_incident.isoformat() if row.date_incident else None,
        "date_reported":       row.date_reported.isoformat() if row.date_reported else None,
        "city":                row.city,
        "state":               row.state,
        "lat":                 row.lat,
        "lng":                 row.lng,
        "source_url":          row.source_url,
        "source_name":         row.source_name,
        "additional_sources":  row.additional_sources,
        "verified":            row.verified,
    }
