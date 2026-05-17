"""
seed_femicide_statistics.py — Medusa

Statistical records documenting femicide patterns in the United States.
Sources:
  - Bureau of Justice Statistics (BJS), Female Murder Victims and
    Victim-Offender Relationship, 2021 (NCJ 305613)
    https://bjs.ojp.gov/female-murder-victims-and-victim-offender-relationship-2021
  - Violence Policy Center (VPC), When Men Murder Women annual reports
    https://vpc.org/studies/wmmw2023.pdf
  - CDC National Violent Death Reporting System (NVDRS)
    https://www.cdc.gov/violenceprevention/datasources/nvdrs/index.html

NOTE: The Femicide Census (femicidecensus.org) is a UK-based database —
its data belongs in the International/Global tab, not this US seed.
Add UK femicide records to seed_global.py when that tab is built out.

Run:
    cd ~/medusa && python3 seed_femicide_statistics.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [

    # ── BJS 2021: National intimate partner homicide rate ─────────────────────

    {
        "case_id":        "stat_bjs_2021_female_murder_ip",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "In 2021, an estimated 4,970 women were victims of murder or "
            "nonnegligent manslaughter in the United States. Of these, 34% — "
            "approximately 1,690 women — were killed by an intimate partner "
            "(current or former spouse, boyfriend, or girlfriend). The rate of "
            "intimate partner homicide for female victims was five times higher "
            "than for male victims, of whom only 6% were killed by an intimate "
            "partner. Source: BJS, Female Murder Victims and Victim-Offender "
            "Relationship, 2021 (NCJ 305613)."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://bjs.ojp.gov/female-murder-victims-and-victim-offender-relationship-2021",
        "source_name":    "Bureau of Justice Statistics",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2021-01-01",
    },

    # ── BJS 2021: Known vs. stranger breakdown ────────────────────────────────

    {
        "case_id":        "stat_bjs_2021_female_murder_known",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "BJS 2021 data: 76% of female murder victims were killed by someone "
            "known to them — intimate partners, family members, or acquaintances. "
            "Only 12% were killed by a stranger. By comparison, 56% of male murder "
            "victims were killed by someone known to them, and 21% by a stranger. "
            "An additional 16% of female victims were killed by a non-intimate "
            "family member (parent, sibling, in-law). For 1 in 5 female murder "
            "victims, the offender relationship was unknown. Source: BJS NCJ 305613."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://bjs.ojp.gov/female-murder-victims-and-victim-offender-relationship-2021",
        "source_name":    "Bureau of Justice Statistics",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2021-01-01",
    },

    # ── VPC: When Men Murder Women — annual US totals ─────────────────────────

    {
        "case_id":        "stat_vpc_2021_when_men_murder_women",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "Violence Policy Center, When Men Murder Women (2023 report, using "
            "2021 FBI SHR data): In 2021, 1,690 women were killed by male "
            "intimate partners in single-victim, single-offender incidents where "
            "the weapon type was known. Of these, 52% were killed with a gun — "
            "making firearms the leading weapon in intimate partner femicide. "
            "States with the highest rates of women killed by men per 100,000 "
            "female residents: Louisiana (2.49), Mississippi (2.27), South "
            "Carolina (2.22), Wyoming (2.10), and Alabama (2.04). "
            "Source: VPC, When Men Murder Women 2023."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://vpc.org/studies/wmmw2023.pdf",
        "source_name":    "Violence Policy Center",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2021-01-01",
    },

    # ── VPC: State-level — Louisiana (highest rate) ───────────────────────────

    {
        "case_id":        "stat_vpc_2021_louisiana_femicide",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "Louisiana ranked #1 in the nation for the rate of women killed by "
            "men in 2021, at 2.49 per 100,000 female residents — more than double "
            "the national average. In raw numbers, 91 women were killed by men in "
            "Louisiana that year. 78% of victims knew their killer. "
            "Source: VPC, When Men Murder Women 2023 (2021 FBI SHR data)."
        ),
        "city":           "New Orleans",
        "state":          "LA",
        "lat":            29.9511,
        "lng":            -90.0715,
        "source_url":     "https://vpc.org/studies/wmmw2023.pdf",
        "source_name":    "Violence Policy Center",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2021-01-01",
    },

    # ── VPC: State-level — Mississippi ───────────────────────────────────────

    {
        "case_id":        "stat_vpc_2021_mississippi_femicide",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "Mississippi ranked #2 nationally for rate of women killed by men "
            "in 2021, at 2.27 per 100,000 female residents. Guns were the "
            "predominant weapon. Mississippi has among the weakest domestic "
            "violence gun laws in the country, with no background check "
            "requirement for private sales. Source: VPC, When Men Murder Women 2023."
        ),
        "city":           "Jackson",
        "state":          "MS",
        "lat":            32.2988,
        "lng":            -90.1848,
        "source_url":     "https://vpc.org/studies/wmmw2023.pdf",
        "source_name":    "Violence Policy Center",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2021-01-01",
    },

    # ── VPC: State-level — South Carolina ────────────────────────────────────

    {
        "case_id":        "stat_vpc_2021_south_carolina_femicide",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "South Carolina ranked #3 nationally for rate of women killed by men "
            "in 2021, at 2.22 per 100,000 female residents. South Carolina has "
            "consistently ranked in the top five states for intimate partner "
            "femicide for over a decade. Source: VPC, When Men Murder Women 2023."
        ),
        "city":           "Columbia",
        "state":          "SC",
        "lat":            34.0007,
        "lng":            -81.0348,
        "source_url":     "https://vpc.org/studies/wmmw2023.pdf",
        "source_name":    "Violence Policy Center",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2021-01-01",
    },

    # ── CDC NVDRS: Firearms as leading weapon in intimate partner femicide ─────

    {
        "case_id":        "stat_cdc_nvdrs_firearms_femicide",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "CDC National Violent Death Reporting System (NVDRS): Firearms are "
            "the leading cause of death in intimate partner femicide, accounting "
            "for more than half of all women killed by male partners in the US. "
            "Research published in the American Journal of Public Health found "
            "that access to a gun in a domestic violence situation increases the "
            "risk of homicide for women by 500%. Women in states with background "
            "check requirements for all gun sales have 14% lower rates of intimate "
            "partner gun homicide. "
            "Source: CDC NVDRS; Everytown for Gun Safety research."
        ),
        "city":           "Atlanta",
        "state":          "GA",
        "lat":            33.7490,
        "lng":            -84.3880,
        "source_url":     "https://www.cdc.gov/violenceprevention/datasources/nvdrs/index.html",
        "source_name":    "CDC National Violent Death Reporting System",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2021-01-01",
    },

    # ── Leaving is the most dangerous time ───────────────────────────────────

    {
        "case_id":        "stat_dv_leaving_danger_peak",
        "violence_type":  "domestic_violence",
        "status":         "congressional_record",
        "summary": (
            "Research consistently shows that the period when a woman attempts "
            "to leave an abusive relationship is the most lethal. Studies find "
            "that women are 70 times more likely to be killed in the two weeks "
            "after leaving than at any other time during or after the relationship. "
            "This pattern is reflected across thousands of femicide cases — the "
            "act of leaving triggers escalation, not safety. "
            "Sources: Dr. Jacquelyn Campbell, Johns Hopkins University; "
            "National Domestic Violence Hotline research."
        ),
        "city":           "Baltimore",
        "state":          "MD",
        "lat":            39.2904,
        "lng":            -76.6122,
        "source_url":     "https://bjs.ojp.gov/female-murder-victims-and-victim-offender-relationship-2021",
        "source_name":    "Bureau of Justice Statistics / Johns Hopkins University",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2021-01-01",
    },

    # ── Strangulation as predictor of femicide ────────────────────────────────

    {
        "case_id":        "stat_strangulation_femicide_predictor",
        "violence_type":  "attempted_murder",
        "status":         "congressional_record",
        "summary": (
            "Non-fatal strangulation is one of the strongest predictors of future "
            "femicide. Research by Gael Strack and Casey Gwinn (Training Institute "
            "on Strangulation Prevention) found that women who have been strangled "
            "by an intimate partner are 7 times more likely to be killed by that "
            "partner. Despite this, strangulation was for many years treated as a "
            "misdemeanor assault in most states. As of 2023, 49 states have passed "
            "felony strangulation laws, largely due to advocacy by survivors and "
            "prosecution reform campaigns. "
            "Source: Training Institute on Strangulation Prevention."
        ),
        "city":           "San Diego",
        "state":          "CA",
        "lat":            32.7157,
        "lng":            -117.1611,
        "source_url":     "https://www.strangulationtraininginstitute.com/",
        "source_name":    "Training Institute on Strangulation Prevention",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2021-01-01",
    },

    # ── Native women: femicide rate 10x national average ─────────────────────

    {
        "case_id":        "stat_native_women_femicide_rate",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "American Indian and Alaska Native (AIAN) women face murder rates "
            "more than 10 times the national average in some counties, according "
            "to CDC data. Homicide is the third leading cause of death for AIAN "
            "women. The vast majority of perpetrators are non-Native men — a "
            "jurisdictional gap created by federal law long prevented tribal "
            "courts from prosecuting non-Native offenders. The Violence Against "
            "Women Act (VAWA) 2022 reauthorization expanded tribal jurisdiction "
            "to cover non-Native perpetrators of domestic violence, sexual assault, "
            "sex trafficking, and stalking on tribal lands. "
            "Sources: CDC NVDRS; Urban Indian Health Institute; VAWA 2022."
        ),
        "city":           "Billings",
        "state":          "MT",
        "lat":            45.7833,
        "lng":            -108.5007,
        "source_url":     "https://www.cdc.gov/violenceprevention/datasources/nvdrs/index.html",
        "source_name":    "CDC National Violent Death Reporting System",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2021-01-01",
    },

    # ── Black women: disproportionate intimate partner homicide ──────────────

    {
        "case_id":        "stat_black_women_ip_homicide_rate",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "Black women are killed by intimate partners at disproportionately "
            "high rates. VPC data shows Black women are murdered by men at nearly "
            "twice the rate of white women. In 2021, the intimate partner homicide "
            "rate for Black women was approximately 4.4 per 100,000 — compared to "
            "1.4 per 100,000 for white women. Structural factors including housing "
            "insecurity, economic dependence, and systemic distrust of police are "
            "barriers to safety planning and exit. "
            "Sources: VPC When Men Murder Women 2023; BJS NCJ 305613."
        ),
        "city":           "Chicago",
        "state":          "IL",
        "lat":            41.8781,
        "lng":            -87.6298,
        "source_url":     "https://vpc.org/studies/wmmw2023.pdf",
        "source_name":    "Violence Policy Center",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2021-01-01",
    },

    # ── Prior DV history in femicide cases ────────────────────────────────────

    {
        "case_id":        "stat_prior_dv_history_femicide",
        "violence_type":  "domestic_violence",
        "status":         "congressional_record",
        "summary": (
            "Multiple studies of intimate partner femicide find that in 60–80% "
            "of cases, there was documented prior domestic violence — police "
            "calls, protective orders, or hospital visits — before the killing. "
            "Despite these warnings, systemic failures in law enforcement response, "
            "court enforcement of protective orders, and firearm surrender "
            "requirements result in preventable deaths. Research by the "
            "Domestic Violence Fatality Review Initiative found that many femicide "
            "victims had contacted police or courts in the months before their death. "
            "Source: National Domestic Violence Fatality Review Initiative."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://bjs.ojp.gov/female-murder-victims-and-victim-offender-relationship-2021",
        "source_name":    "Bureau of Justice Statistics / NDVFRI",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2021-01-01",
    },

]


def main():
    print("\n  [Medusa] Seeding femicide statistics...\n")
    try:
        init_db()
    except Exception as e:
        print(f"  [DB] Warning: {e}")

    saved = 0
    skipped = 0
    for case in CASES:
        if save_case(case):
            saved += 1
            print(f"  + {case['case_id']}")
        else:
            skipped += 1
            print(f"  ~ skipped (exists): {case['case_id']}")

    print(f"\n  Done. {saved} saved, {skipped} skipped.\n")


if __name__ == "__main__":
    main()
