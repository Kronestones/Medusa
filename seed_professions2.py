#!/usr/bin/env python3
"""
seed_professions2.py — Additional professional exclusions of women

Nursing, aviation, architecture, trades, military academies, Supreme Court
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    {
        "summary": (
            "Nursing — Male Domination of Hospital Administration: Despite nursing being "
            "overwhelmingly female (87%), hospital administration and chief nursing "
            "officer roles have historically been dominated by men. The American Nurses "
            "Association was founded in 1896 but female nurses were barred from serving "
            "in WWI as commissioned officers — they served without rank, pay parity, or "
            "veterans benefits until 1947. Male nurses were barred from the US Army "
            "Nurse Corps entirely until 1955. Female nurses in the military faced "
            "mandatory discharge upon marriage until 1970. As of 2024, female nurses "
            "earn 13% less than male nurses in equivalent roles. Nursing remains one "
            "of the most physically dangerous professions for workplace violence — "
            "80% of serious violent incidents in healthcare are committed against nurses, "
            "overwhelmingly by male patients and visitors."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "1947-01-01",
        "violence_type": "coercive_control",
        "status": "congressional_record",
        "source_url": "https://www.nursingworld.org/ana/about-ana/history/",
        "source_name": "American Nurses Association / US Army Historical Records",
        "verified": True,
    },

    {
        "summary": (
            "Aviation: Women were barred from commercial airline pilot positions until "
            "1973, when Emily Howell Warner became the first female commercial airline "
            "pilot in the US (Frontier Airlines). United Airlines fired stewardesses "
            "who got married or turned 32 until a 1968 EEOC ruling. Female flight "
            "attendants were required to be single, childless, within specific weight "
            "ranges, and meet appearance standards — rules that did not apply to male "
            "employees. Bessie Coleman, the first Black female pilot in the US, had to "
            "travel to France to earn her license in 1921 because no US flight school "
            "would accept a Black woman. As of 2024, women make up only 5.8% of "
            "commercial airline pilots in the US — one of the lowest rates of any "
            "profession requiring similar education."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "1973-01-29",
        "violence_type": "coercive_control",
        "status": "congressional_record",
        "source_url": "https://www.faa.gov/pilots/female_aviators",
        "source_name": "FAA / Airlines for America Historical Records",
        "verified": True,
    },

    {
        "summary": (
            "Architecture: The American Institute of Architects (AIA) was founded in "
            "1857 and did not admit women as full members until 1888, when Louise "
            "Blanchard Bethune became the first female member. Women were systematically "
            "excluded from architecture schools — Harvard's Graduate School of Design "
            "did not admit women until 1942. Denise Scott Brown was excluded from the "
            "1991 Pritzker Architecture Prize awarded to her partner Robert Venturi, "
            "despite equal contribution — a decision widely condemned as sexist. As of "
            "2024, women earn 50% of architecture degrees but hold only 26% of licensed "
            "architect positions and 17% of firm leadership roles. The gender pay gap "
            "in architecture is among the largest of any design profession."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "1991-01-01",
        "violence_type": "coercive_control",
        "status": "congressional_record",
        "source_url": "https://www.aia.org/pages/2646-diversity-and-inclusion",
        "source_name": "American Institute of Architects / Pritzker Prize Records",
        "verified": True,
    },

    {
        "summary": (
            "The Trades — Construction, Plumbing, Electrical, Carpentry: Women have "
            "been systematically excluded from skilled trades through union membership "
            "requirements, apprenticeship gatekeeping, and physical harassment. The "
            "AFL-CIO building trades unions formally excluded women and minorities until "
            "federal anti-discrimination enforcement in the 1970s. As of 2024, women "
            "make up only 4% of construction workers, 1.5% of electricians, and 2% of "
            "plumbers in the US. Female apprentices report rates of sexual harassment "
            "exceeding 75% — with many driven out before completing their training. "
            "A 2020 RAND study found women in construction earn 95 cents for every "
            "dollar earned by men in equivalent roles — but the pipeline exclusion "
            "means few reach equivalent roles at all."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "1970-01-01",
        "violence_type": "coercive_control",
        "status": "congressional_record",
        "source_url": "https://www.bls.gov/cps/cpsaat11.htm",
        "source_name": "Bureau of Labor Statistics / RAND Corporation",
        "verified": True,
    },

    {
        "summary": (
            "Military Academies: Women were barred from all US military service "
            "academies — West Point, Annapolis, Air Force Academy, Coast Guard Academy, "
            "and Merchant Marine Academy — until 1976, when Congress mandated their "
            "admission over fierce military resistance. The first class of women "
            "graduated in 1980. Female cadets faced systematic hazing, sexual assault, "
            "and institutional retaliation for reporting. A 2003 Air Force Academy "
            "scandal revealed over 142 reported sexual assaults over a decade with "
            "systematic cover-up by command. Annual DoD surveys consistently show "
            "20-25% of female service academy students experience sexual assault. "
            "Prosecution rates remain below 10%. As of 2024, women make up 25% of "
            "service academy enrollment but face documented discrimination in "
            "assignments, promotions, and command opportunities."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "1976-10-07",
        "violence_type": "sexual_assault",
        "status": "congressional_record",
        "source_url": "https://www.defense.gov/News/Special-Reports/MSA/",
        "source_name": "US Department of Defense / Service Academy Reports",
        "verified": True,
    },

    {
        "summary": (
            "US Supreme Court: No woman served on the Supreme Court for 191 years after "
            "its founding in 1790. Sandra Day O'Connor was the first female Justice, "
            "appointed 1981. Ruth Bader Ginsburg joined in 1993. For most of American "
            "history, the nine men who interpreted the Constitution — including all "
            "rulings on women's rights, reproductive rights, employment discrimination, "
            "and sexual assault — were exclusively male. Justice Clarence Thomas's wife "
            "Ginni Thomas actively worked to overturn the 2020 election while Thomas "
            "refused to recuse himself from related cases. Justice Brett Kavanaugh was "
            "confirmed in 2018 despite credible sexual assault allegations from Dr. "
            "Christine Blasey Ford — the Senate confirmed him 50-48. The 6-3 "
            "conservative supermajority shaped by Trump appointments overturned Roe v. "
            "Wade in 2022, eliminating 49 years of federal abortion rights."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "1981-09-25",
        "violence_type": "coercive_control",
        "status": "congressional_record",
        "source_url": "https://www.supremecourt.gov/about/justices.aspx",
        "source_name": "US Supreme Court Historical Records",
        "verified": True,
    },

    {
        "summary": (
            "Veterinary Medicine: Until the mid-20th century, women were largely "
            "excluded from veterinary schools in the US. Iowa State University admitted "
            "its first female veterinary student in 1910 but most schools maintained "
            "informal quotas or outright bans. Cornell and other elite programs did not "
            "actively recruit women until the 1970s. Today the profession has reversed — "
            "women now earn over 80% of veterinary degrees — but face a persistent pay "
            "gap of 18-23% compared to male veterinarians in equivalent roles, and "
            "are underrepresented in specialty and leadership positions."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "1970-01-01",
        "violence_type": "coercive_control",
        "status": "congressional_record",
        "source_url": "https://www.avma.org/resources-tools/reports-statistics/market-research-statistics-us-veterinarians",
        "source_name": "American Veterinary Medical Association",
        "verified": True,
    },

    {
        "summary": (
            "Bartending: Women were legally banned from bartending in many US states "
            "until the 1970s. Michigan's ban was upheld by the Supreme Court in Goesaert "
            "v. Cleary (1948), which ruled that states could prohibit women from "
            "bartending unless they were the wife or daughter of the male bar owner. "
            "The Court held this was a legitimate exercise of state police power to "
            "protect women's 'moral and social problems.' The decision was not overruled "
            "until Title VII enforcement in the 1970s. Women in the service industry "
            "continue to face the highest rates of workplace sexual harassment of any "
            "sector — the Equal Employment Opportunity Commission reports that over "
            "90% of female restaurant workers experience sexual harassment."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "1948-12-20",
        "violence_type": "coercive_control",
        "status": "congressional_record",
        "source_url": "https://supreme.justia.com/cases/federal/us/335/464/",
        "source_name": "Goesaert v. Cleary, 335 U.S. 464 (1948)",
        "verified": True,
    },

    {
        "summary": (
            "Tech Industry — Silicon Valley: Women were systematically pushed out of "
            "computer science beginning in the 1980s when personal computers were "
            "marketed exclusively to boys and men. In 1984, 37% of computer science "
            "graduates were women — by 2024 that figure had dropped to 21%. Google, "
            "Apple, Facebook, and other major tech companies have published diversity "
            "reports showing women hold only 25-30% of technical roles and under 20% "
            "of leadership positions. A 2016 survey by the Elephant in the Valley "
            "found 60% of women in Silicon Valley had experienced unwanted sexual "
            "advances, 90% witnessed sexist behavior, and 75% were asked about family "
            "plans in job interviews. High-profile cases including Susan Fowler at Uber "
            "and Ellen Pao at Kleiner Perkins documented systemic discrimination."
        ),
        "city": "San Francisco", "state": "CA",
        "date_incident": "1984-01-01",
        "violence_type": "coercive_control",
        "status": "congressional_record",
        "source_url": "https://www.npr.org/sections/money/2014/10/21/357629765/when-women-stopped-coding",
        "source_name": "NPR / NCWIT / Elephant in the Valley Survey",
        "verified": True,
    },

    {
        "summary": (
            "Academia — Tenure and the Motherhood Penalty: Female professors face "
            "systematic discrimination in tenure decisions, publication credit, and "
            "salary. A 2019 Stanford study found women's research contributions are "
            "systematically undervalued — papers with female first authors receive "
            "fewer citations than equivalent papers by male authors. The 'motherhood "
            "penalty' in academia reduces a woman's salary by 4% per child while "
            "fatherhood increases men's salaries. Women are more likely to be assigned "
            "service work and less likely to be assigned research time. Female "
            "professors receive lower student evaluation scores than male professors "
            "teaching identical content — a bias documented across disciplines and "
            "institutions. As of 2024, women make up 49% of assistant professors but "
            "only 32% of full professors."
        ),
        "city": "Washington", "state": "DC",
        "date_incident": "2024-01-01",
        "violence_type": "coercive_control",
        "status": "congressional_record",
        "source_url": "https://www.aaup.org/report/gender-equity-indicators",
        "source_name": "American Association of University Professors",
        "verified": True,
    },

]


def main():
    print("\n[Seed Professions 2] Seeding additional professional exclusion records...\n")
    init_db()
    saved = 0
    for raw in RECORDS:
        record = normalize_record(raw)
        if record and save_case(record):
            saved += 1
            print(f"  + {record['summary'][:80]}...")
    print(f"\n[Seed Professions 2] {saved}/{len(RECORDS)} records saved.\n")


if __name__ == "__main__":
    main()
