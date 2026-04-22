"""
seed.py — Medusa
Seeds known documented cases from public court records.
Sources: SDNY filings, Maxwell trial, Virgin Islands AG suit,
unsealed depositions, NSOPW, DOJ SMART Office.
Run once: python3 -c "from medusa.seed import seed_all; seed_all()"
"""

import os
from datetime import datetime, timezone
from sqlalchemy import create_engine, text

DB = os.environ.get("DATABASE_URL", "")

def get_engine():
    return create_engine(DB, pool_pre_ping=True, pool_recycle=300)

# ── Epstein Network — named in court records only ─────────────────────────────
# Sources:
#   SDNY USA v. Ghislaine Maxwell (20-cr-330)
#   USVI AG v. JPMorgan Chase
#   USVI AG v. Deutsche Bank
#   Julie K. Brown / Miami Herald investigative series
#   Unsealed Epstein civil deposition transcripts (SDNY 2024)
#   Maxwell trial testimony transcripts

EPSTEIN_CASES = [
    {
        "summary": "Jeffrey Epstein convicted sex offender, federal charges of sex trafficking of minors. Died in federal custody 2019 awaiting trial on trafficking conspiracy charges. Victims documented across New York, Palm Beach, and US Virgin Islands.",
        "city": "New York", "state": "NY",
        "violence_type": "trafficking",
        "status": "convicted",
        "is_public_figure": True,
        "date_incident": "1994-01-01",
        "source_url": "https://www.justice.gov/usao-sdny/press-release/file/1182621/download",
        "source_name": "SDNY Indictment USA v. Epstein 2019",
    },
    {
        "summary": "Ghislaine Maxwell convicted on 5 federal counts including sex trafficking of minors and conspiracy. Trial established she recruited and groomed underage girls for Epstein. Sentenced to 20 years federal prison 2022.",
        "city": "New York", "state": "NY",
        "violence_type": "trafficking",
        "status": "convicted",
        "is_public_figure": True,
        "date_incident": "1994-01-01",
        "source_url": "https://www.justice.gov/usao-sdny/press-release/file/1457236/download",
        "source_name": "SDNY USA v. Maxwell conviction 2021",
    },
    {
        "summary": "Jean-Luc Brunel, modeling agency operator, charged in France with rape of minors and trafficking in connection with Epstein network. Named in multiple victim depositions filed in SDNY. Found dead in French prison 2022 awaiting trial.",
        "city": "New York", "state": "NY",
        "violence_type": "rape",
        "status": "charged",
        "is_public_figure": True,
        "date_incident": "1990-01-01",
        "source_url": "https://www.miamiherald.com/news/local/article239474328.html",
        "source_name": "Miami Herald / Julie K. Brown investigation",
    },
    {
        "summary": "Alan Dershowitz named in civil deposition by Virginia Giuffre, filed SDNY. Accusations of sexual abuse when Giuffre was a minor. Deposition unsealed 2024 by federal court order.",
        "city": "New York", "state": "NY",
        "violence_type": "sexual_assault",
        "status": "credible_allegation",
        "is_public_figure": True,
        "date_incident": "2000-01-01",
        "source_url": "https://storage.courtlistener.com/recap/gov.uscourts.nysd.447706/gov.uscourts.nysd.447706.1274.0.pdf",
        "source_name": "SDNY unsealed deposition transcripts 2024",
    },
    {
        "summary": "Prince Andrew named in civil suit by Virginia Giuffre alleging sexual abuse when Giuffre was 17. Settled out of court 2022 for undisclosed sum. Named in multiple unsealed SDNY documents.",
        "city": "New York", "state": "NY",
        "violence_type": "sexual_assault",
        "status": "civil_judgment",
        "is_public_figure": True,
        "date_incident": "2001-01-01",
        "source_url": "https://storage.courtlistener.com/recap/gov.uscourts.nysd.539612/gov.uscourts.nysd.539612.267.0.pdf",
        "source_name": "SDNY Giuffre v. Prince Andrew — settlement 2022",
    },
    {
        "summary": "Leslie Wexner, founder of L Brands, named in USVI AG lawsuit as Epstein associate. Epstein managed Wexner finances and used Wexner properties. USVI suit documents Epstein using business connections for trafficking network.",
        "city": "Columbus", "state": "OH",
        "violence_type": "trafficking",
        "status": "credible_allegation",
        "is_public_figure": True,
        "date_incident": "1990-01-01",
        "source_url": "https://www.documentcloud.org/documents/23589649-usvi-v-jpmorgan",
        "source_name": "USVI AG v. JPMorgan Chase — Epstein network suit",
    },
    {
        "summary": "Ghislaine Maxwell and Jeffrey Epstein operated trafficking network from Little Saint James, US Virgin Islands. USVI AG lawsuit established island used as base for abuse of trafficking victims. JPMorgan and Deutsche Bank settlements confirmed financial facilitation.",
        "city": "Charlotte Amalie", "state": "VI",
        "violence_type": "trafficking",
        "status": "civil_judgment",
        "is_public_figure": True,
        "date_incident": "1998-01-01",
        "source_url": "https://www.documentcloud.org/documents/23589649-usvi-v-jpmorgan",
        "source_name": "USVI AG v. JPMorgan — $75M settlement 2023",
    },
]

# ── Registry seed — DOJ SMART / NSOPW documented cases ───────────────────────
# These are aggregate documented facts, not individual registry entries
# Source: DOJ Office of Sex Offender Sentencing, Monitoring, Apprehending,
#         Registering, and Tracking (SMART Office)

REGISTRY_SUMMARY_CASES = [
    {
        "summary": "DOJ SMART Office reports 900,000+ registered sex offenders in the United States as of 2024. Majority of victims are female. SORNA (Sex Offender Registration and Notification Act) requires public registry access.",
        "city": "Washington", "state": "DC",
        "violence_type": "sexual_assault",
        "status": "convicted",
        "is_public_figure": False,
        "date_incident": "2024-01-01",
        "source_url": "https://www.smart.ojp.gov/sorna",
        "source_name": "DOJ SMART Office — SORNA National Registry 2024",
    },
    {
        "summary": "FBI Uniform Crime Report 2022: 145,200+ rapes reported to US law enforcement. FBI estimates only 20-25% of rapes are reported. Majority of perpetrators are male, majority of victims are female.",
        "city": "Washington", "state": "DC",
        "violence_type": "rape",
        "status": "reported",
        "is_public_figure": False,
        "date_incident": "2022-01-01",
        "source_url": "https://ucr.fbi.gov/crime-in-the-u.s/2022",
        "source_name": "FBI Uniform Crime Report 2022",
    },
    {
        "summary": "CDC National Intimate Partner and Sexual Violence Survey: 1 in 4 women in the US experience severe intimate partner physical violence. 1 in 3 women experience sexual violence by a partner. 99% of perpetrators are male.",
        "city": "Atlanta", "state": "GA",
        "violence_type": "domestic_violence",
        "status": "reported",
        "is_public_figure": False,
        "date_incident": "2022-01-01",
        "source_url": "https://www.cdc.gov/violenceprevention/intimatepartnerviolence/fastfact.html",
        "source_name": "CDC NISVS — National IPV Survey 2022",
    },
    {
        "summary": "National Human Trafficking Hotline 2023: 10,726 trafficking cases reported in the US. 71% of victims are female. Sex trafficking comprises majority of cases. Traffickers overwhelmingly male.",
        "city": "Washington", "state": "DC",
        "violence_type": "trafficking",
        "status": "reported",
        "is_public_figure": False,
        "date_incident": "2023-01-01",
        "source_url": "https://humantraffickinghotline.org/en/statistics",
        "source_name": "National Human Trafficking Hotline — 2023 Statistics",
    },
]


def seed_all():
    import hashlib
    engine = get_engine()

    all_cases = EPSTEIN_CASES + REGISTRY_SUMMARY_CASES
    added = 0

    with engine.connect() as conn:
        for c in all_cases:
            raw = f"{c['city']}{c['state']}{c['violence_type']}{c['date_incident']}".lower().replace(" ", "")
            h   = hashlib.md5(raw.encode()).hexdigest()[:8].upper()
            yr  = (c["date_incident"] or "")[:4] or "0000"
            case_id = f"MEDUSA-{yr}-{h}"

            exists = conn.execute(
                text("SELECT id FROM cases WHERE case_id = :cid"),
                {"cid": case_id}
            ).fetchone()

            if exists:
                print(f"  SKIP: {c['summary'][:50]}")
                continue

            # Geocode
            try:
                import requests as req
                resp = req.get(
                    "https://nominatim.openstreetmap.org/search",
                    params={"q": f"{c['city']}, {c['state']}, United States",
                            "format": "json", "limit": 1},
                    headers={"User-Agent": "Medusa/1.0"},
                    timeout=5,
                )
                data = resp.json()
                lat = float(data[0]["lat"]) if data else None
                lng = float(data[0]["lon"]) if data else None
            except Exception:
                lat, lng = None, None

            conn.execute(text("""
                INSERT INTO cases
                    (case_id, violence_type, summary, status, is_public_figure,
                     date_incident, date_reported, city, state, lat, lng,
                     source_url, source_name, verified)
                VALUES
                    (:case_id, :vtype, :summary, :status, :is_pub,
                     :date_inc, :date_rep, :city, :state, :lat, :lng,
                     :source_url, :source_name, true)
            """), {
                "case_id":     case_id,
                "vtype":       c["violence_type"],
                "summary":     c["summary"],
                "status":      c["status"],
                "is_pub":      c["is_public_figure"],
                "date_inc":    c["date_incident"],
                "date_rep":    datetime.now(timezone.utc).isoformat(),
                "city":        c["city"],
                "state":       c["state"],
                "lat":         lat,
                "lng":         lng,
                "source_url":  c["source_url"],
                "source_name": c["source_name"],
            })
            conn.commit()
            added += 1
            print(f"  + {c['summary'][:60]}")

    print(f"\nSeeded {added} cases.")


if __name__ == "__main__":
    seed_all()
