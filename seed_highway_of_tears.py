"""
seed_highway_of_tears.py — Medusa

Highway of Tears — Highway 16, British Columbia, Canada.
Individual records for named victims plus systemic overview.
All records flagged tab="global", country="Canada".

RCMP acknowledges 18 victims 1969–2006.
Indigenous organizations estimate 40–50+ victims.
Over 2,000 Indigenous women and girls reported missing or murdered
across Canada in the past three decades.

Run:
    cd ~/medusa && python3 seed_highway_of_tears.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [

    # ══════════════════════════════════════════════════════════════════════════
    # SYSTEMIC OVERVIEW RECORD
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "highway_of_tears_overview_bc_canada",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "The Highway of Tears is a 724-kilometre stretch of Yellowhead "
            "Highway 16 in northern British Columbia, Canada, between Prince "
            "George and Prince Rupert, where an estimated 40 to 50 or more "
            "women — the majority Indigenous — have been murdered or disappeared "
            "since 1969. Twenty-three First Nations communities border the highway. "
            "The RCMP's official Project E-PANA investigation, launched 2005, "
            "acknowledges only 18 victims between 1969 and 2006. Indigenous "
            "organizations, family members, and community advocates dispute this "
            "number as a severe undercount, arguing it reflects systemic racism "
            "in how police determined which cases qualified for inclusion. "
            "The RCMP's own criteria required victims to be involved in 'high-risk "
            "activities' such as hitchhiking — a standard that reflected victim "
            "blaming rather than the reality that hitchhiking was the only "
            "available transportation for many women in communities with no "
            "public transit and widespread poverty. Until 2017, there was no "
            "public bus service along Highway 16. "
            "Human Rights Watch identified British Columbia as having the highest "
            "rate of unsolved murders of Indigenous women and girls in Canada. "
            "A 2014 RCMP national report found 1,017 Indigenous women had been "
            "murdered across Canada between 1980 and 2012, with another 164 "
            "missing — and many advocates believe the true number exceeds 4,000. "
            "Families repeatedly reported that RCMP investigators dismissed or "
            "delayed responding to reports of missing women, and that cases were "
            "not treated with the same urgency as cases involving non-Indigenous "
            "women. In 2016, Prime Minister Justin Trudeau launched a National "
            "Inquiry into Missing and Murdered Indigenous Women and Girls, "
            "allocating $53 million. The 2019 Inquiry report — 'Reclaiming Power "
            "and Place' — concluded that the violence amounts to genocide. "
            "The term 'Highway of Tears' was coined at a 1998 vigil in Terrace, "
            "BC by Florence Naziel, who named it for the tears of the victims' "
            "families. The 20th anniversary commemoration of the 2006 Highway "
            "of Tears Symposium was held in April 2026. "
            "Sources: RCMP Project E-PANA; Human Rights Watch; National Inquiry "
            "into MMIWG Final Report 2019; Carrier Sekani Family Services."
        ),
        "city":           "Prince George",
        "state":          "DC",   # placeholder — Canadian case
        "lat":            53.9171,
        "lng":            -122.7497,
        "source_url":     "https://www.mmiwg-ffada.ca/final-report/",
        "source_name":    "National Inquiry into MMIWG — Final Report 2019",
        "additional_sources": [
            {"url": "https://highwayoftears.org/highway-of-tears/",
             "name": "Carrier Sekani Family Services"},
            {"url": "https://www.hrw.org/report/2013/02/13/those-who-take-us-away/abusive-policing-and-failures-protection-indigenous-women",
             "name": "Human Rights Watch"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1969-01-01",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # GLORIA MOODY — 1969, first known victim
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "gloria_moody_bc_canada_1969",
        "violence_type":  "homicide",
        "status":         "unsolved",
        "summary": (
            "Gloria Moody, 27, a mother from the Bella Coola Indian Reserve "
            "of the Nuxalk Nation in British Columbia, was travelling with "
            "family on a weekend road trip on October 25, 1969. Her body was "
            "found by hunters on a cattle trail approximately 10 km west of "
            "Williams Lake, BC. She is among the earliest documented victims "
            "on the Highway of Tears. Her murder remains unsolved."
        ),
        "city":           "Williams Lake",
        "state":          "DC",
        "lat":            52.1418,
        "lng":            -122.1415,
        "source_url":     "https://coldcasepg.ca/?p=346",
        "source_name":    "ColdCasePG / RCMP E-PANA",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1969-10-25",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MICHELINE PARE — 1970
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "micheline_pare_bc_canada_1970",
        "violence_type":  "homicide",
        "status":         "unsolved",
        "summary": (
            "Micheline Pare, 18, was last seen alive on Highway 29 at the "
            "gates of Tompkins Ranch between Fort St. John and Hudson's Hope, "
            "BC in July 1970. Two women had given her a ride and dropped her "
            "off there. She was hitchhiking. Her body was recovered by "
            "berry-pickers in Hudson's Hope on August 8, 1970, 21 km from "
            "where she was last seen. She had been beaten to death with a "
            "blunt weapon. Her murder remains unsolved and she is on the "
            "official RCMP list of Highway of Tears victims."
        ),
        "city":           "Hudson's Hope",
        "state":          "DC",
        "lat":            56.0362,
        "lng":            -121.9057,
        "source_url":     "https://coldcasepg.ca/?p=346",
        "source_name":    "ColdCasePG / RCMP E-PANA",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1970-07-01",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # GALE ANN WEYS — 1973
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "gale_ann_weys_bc_canada_1973",
        "violence_type":  "homicide",
        "status":         "unsolved",
        "summary": (
            "Gale Ann Weys disappeared on October 19, 1973. Police believe "
            "she left the service station where she worked in Clearwater, BC "
            "at about 9:30 p.m. to hitchhike back to her parents' house in "
            "Kamloops. Her nude, decomposed body was found nearly a year later, "
            "on April 6, 1974, just off Highway 5 in a water-filled ditch "
            "11 km south of Clearwater. Her murder remains unsolved."
        ),
        "city":           "Clearwater",
        "state":          "DC",
        "lat":            51.6476,
        "lng":            -120.0380,
        "source_url":     "https://coldcasepg.ca/?p=346",
        "source_name":    "ColdCasePG / RCMP E-PANA",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1973-10-19",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MONICA JACK — 1978, age 12
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "monica_jack_bc_canada_1978",
        "violence_type":  "homicide",
        "status":         "convicted",
        "summary": (
            "Monica Jack, 12 years old, was last seen riding her bicycle along "
            "the highway near the Nicola Ranch in Merritt, BC in May 1978. "
            "She was the youngest confirmed victim in the Highway of Tears cases. "
            "Her remains were not found until June 1995 — 17 years after her "
            "disappearance. Garry Taylor Handlen was charged with her murder "
            "and arrested in December 2014. He was convicted of first-degree "
            "murder in 2019. The conviction was upheld on appeal. Monica's "
            "case — solved 41 years after her death — became a symbol of the "
            "decades of indifference to violence against Indigenous girls "
            "and women along the highway."
        ),
        "city":           "Merritt",
        "state":          "DC",
        "lat":            50.1133,
        "lng":            -120.7860,
        "source_url":     "https://people.howstuffworks.com/highway-of-tears-news.htm",
        "source_name":    "HowStuffWorks / RCMP",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1978-05-01",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # COLLEEN MacMILLEN — 1974, linked to serial killer Bobby Fowler
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "colleen_macmillen_bc_canada_1974",
        "violence_type":  "homicide",
        "status":         "solved_perpetrator_deceased",
        "summary": (
            "Colleen MacMillen was murdered along the Highway of Tears in 1974. "
            "DNA evidence later linked her death to Bobby Jack Fowler, an "
            "American serial killer and sex offender who was active along the "
            "highway in the 1970s. Fowler is suspected in at least two other "
            "Highway of Tears cases. He died in an Oregon state prison in 2006 "
            "before he could be formally charged in connection with MacMillen's "
            "death, though the DNA connection was confirmed after his death. "
            "He was never prosecuted for any of the Highway of Tears killings."
        ),
        "city":           "Prince George",
        "state":          "DC",
        "lat":            53.9171,
        "lng":            -122.7497,
        "source_url":     "https://people.howstuffworks.com/highway-of-tears-news.htm",
        "source_name":    "HowStuffWorks / RCMP E-PANA",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1974-01-01",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ALBERTA WILLIAMS — 1989
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "alberta_williams_bc_canada_1989",
        "violence_type":  "homicide",
        "status":         "unsolved",
        "summary": (
            "Alberta Williams, a young Indigenous woman from the Gitxsan Nation, "
            "was murdered in 1989 along Highway 16 near Smithers, BC. Her case "
            "was one of the original nine identified by the RCMP when Project "
            "E-PANA launched in 2005. Her murder remains unsolved. Alberta's "
            "family and community have been among the most vocal advocates for "
            "justice for Highway of Tears victims for over three decades."
        ),
        "city":           "Smithers",
        "state":          "DC",
        "lat":            54.7816,
        "lng":            -127.1669,
        "source_url":     "https://highwayoftears.org/highway-of-tears/",
        "source_name":    "Carrier Sekani Family Services / RCMP E-PANA",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1989-01-01",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # DELPHINE NIKAL — 1990, age 16
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "delphine_nikal_bc_canada_1990",
        "violence_type":  "homicide",
        "status":         "unsolved",
        "summary": (
            "Delphine Nikal, 16 years old and a member of the Wet'suwet'en "
            "Nation, disappeared in June 1990 while hitchhiking near Smithers, "
            "BC along Highway 16. She has never been found. Her disappearance "
            "was one of the original nine cases in Project E-PANA. Delphine "
            "remains missing and her case is unsolved. Her family has spent "
            "over three decades seeking answers."
        ),
        "city":           "Smithers",
        "state":          "DC",
        "lat":            54.7816,
        "lng":            -127.1669,
        "source_url":     "https://highwayoftears.org/highway-of-tears/",
        "source_name":    "Carrier Sekani Family Services / RCMP E-PANA",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1990-06-01",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # RAMONA WILSON — 1994, age 16
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "ramona_wilson_bc_canada_1994",
        "violence_type":  "homicide",
        "status":         "unsolved",
        "summary": (
            "Ramona Wilson, 16 years old and a member of the Gitxsan Nation, "
            "disappeared in June 1994 near Smithers, BC. Her remains were "
            "found in April 1995 near the Smithers Airport. Her case was one "
            "of three that triggered the creation of Project E-PANA and was "
            "featured in the 2006 documentary Finding Dawn by Métis filmmaker "
            "Christine Welsh. Ramona's murder remains unsolved. Her mother, "
            "Matilda Wilson, became one of the most prominent voices calling "
            "for justice along the Highway of Tears for decades after her "
            "daughter's death."
        ),
        "city":           "Smithers",
        "state":          "DC",
        "lat":            54.7816,
        "lng":            -127.1669,
        "source_url":     "https://highwayoftears.org/highway-of-tears/",
        "source_name":    "Carrier Sekani Family Services / RCMP E-PANA",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1994-06-01",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # LANA DERRICK — 1995, age 19
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "lana_derrick_bc_canada_1995",
        "violence_type":  "homicide",
        "status":         "unsolved",
        "summary": (
            "Lana Derrick, 19, a member of the Gitxsan Nation and a student "
            "at the University of Northern British Columbia, disappeared in "
            "October 1995 while hitchhiking near Terrace, BC. She has never "
            "been found. Her disappearance is one of the original E-PANA cases. "
            "She was studying to build a better future for herself and her "
            "community when she vanished. Her case remains unsolved."
        ),
        "city":           "Terrace",
        "state":          "DC",
        "lat":            54.5150,
        "lng":            -128.6037,
        "source_url":     "https://highwayoftears.org/highway-of-tears/",
        "source_name":    "Carrier Sekani Family Services / RCMP E-PANA",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1995-10-01",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ROXANNE THIARA — 1994, age 15
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "roxanne_thiara_bc_canada_1994",
        "violence_type":  "homicide",
        "status":         "unsolved",
        "summary": (
            "Roxanne Thiara, 15 years old, disappeared in August 1994 near "
            "Burns Lake, BC. Her body was discovered a short time later. "
            "Roxanne's case was one of the three original cases — along with "
            "Alisha Germaine and Ramona Wilson — that prompted the RCMP to "
            "create Project E-PANA in 2005. Her murder remains unsolved."
        ),
        "city":           "Burns Lake",
        "state":          "DC",
        "lat":            54.2333,
        "lng":            -125.7667,
        "source_url":     "https://highwayoftears.org/highway-of-tears/",
        "source_name":    "Carrier Sekani Family Services / RCMP E-PANA",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1994-08-01",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ALISHA GERMAINE — 1994, age 15
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "alisha_germaine_bc_canada_1994",
        "violence_type":  "homicide",
        "status":         "unsolved",
        "summary": (
            "Alisha Germaine, 15 years old, disappeared in December 1994 near "
            "Prince George, BC. Her body was found shortly after. She was one "
            "of three cases — alongside Roxanne Thiara and Ramona Wilson — "
            "whose similarities prompted the RCMP to create Project E-PANA "
            "in 2005 to investigate whether a serial killer was operating along "
            "the highway. Her murder remains unsolved."
        ),
        "city":           "Prince George",
        "state":          "DC",
        "lat":            53.9171,
        "lng":            -122.7497,
        "source_url":     "https://highwayoftears.org/highway-of-tears/",
        "source_name":    "Carrier Sekani Family Services / RCMP E-PANA",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1994-12-01",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # NICOLE HOAR — 2002 (non-Indigenous victim)
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "nicole_hoar_bc_canada_2002",
        "violence_type":  "homicide",
        "status":         "unsolved",
        "summary": (
            "Nicole Hoar, 25, a tree planter from Red Deer, Alberta, disappeared "
            "in June 2002 while hitchhiking along Highway 16 near Prince George, "
            "BC to visit her sister in Smithers. She has never been found. "
            "Nicole was the only non-Indigenous woman among the original nine "
            "E-PANA cases. Her disappearance drew significant media attention "
            "in part because of her non-Indigenous background — a disparity in "
            "coverage that her family and Indigenous advocates have since "
            "highlighted as evidence of systemic racism in how missing women "
            "cases are treated by media and police. Her case remains unsolved."
        ),
        "city":           "Prince George",
        "state":          "DC",
        "lat":            53.9171,
        "lng":            -122.7497,
        "source_url":     "https://highwayoftears.org/highway-of-tears/",
        "source_name":    "Carrier Sekani Family Services / RCMP E-PANA",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2002-06-01",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TAMARA CHIPMAN — 2005, age 22
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "tamara_chipman_bc_canada_2005",
        "violence_type":  "homicide",
        "status":         "unsolved",
        "summary": (
            "Tamara Chipman, 22, disappeared in September 2005 near Prince "
            "Rupert, BC while hitchhiking along Highway 16. She has never "
            "been found. Her aunt, Gladys Radford, became one of the most "
            "visible and tireless advocates for the Highway of Tears victims, "
            "travelling to Vancouver and Victoria repeatedly to demand action. "
            "Tamara's disappearance was one of the original nine E-PANA cases. "
            "Her case remains open and unsolved."
        ),
        "city":           "Prince Rupert",
        "state":          "DC",
        "lat":            54.3150,
        "lng":            -130.3208,
        "source_url":     "https://highwayoftears.org/highway-of-tears/",
        "source_name":    "Carrier Sekani Family Services / RCMP E-PANA",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2005-09-01",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # AIELAH SARIC-AUGER — 2006, age 14
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "aielah_saric_auger_bc_canada_2006",
        "violence_type":  "homicide",
        "status":         "unsolved",
        "summary": (
            "Aielah Saric-Auger, 14 years old, was found murdered along Highway "
            "16 near Prince George, BC in February 2006. She was a member of "
            "the Lheidli T'enneh First Nation. Aielah was the youngest of the "
            "original nine E-PANA cases. Her murder came just months after the "
            "2005 launch of Project E-PANA, yet the investigation failed to "
            "prevent her death — a fact her family has cited as evidence of "
            "systemic failure. Her murder remains unsolved."
        ),
        "city":           "Prince George",
        "state":          "DC",
        "lat":            53.9171,
        "lng":            -122.7497,
        "source_url":     "https://highwayoftears.org/highway-of-tears/",
        "source_name":    "Carrier Sekani Family Services / RCMP E-PANA",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2006-02-01",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MADELINE "MADDY" SCOTT — 2011, age 20
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "madeline_scott_bc_canada_2011",
        "violence_type":  "homicide",
        "status":         "unsolved",
        "summary": (
            "Madeline 'Maddy' Scott, 20, disappeared in May 2011 near Prince "
            "George, BC — after the official RCMP E-PANA list was closed in "
            "2006, demonstrating that violence along the highway did not end "
            "with the formal investigation. Maddy was last seen at a party "
            "in Prince George. Despite extensive searches, she has never been "
            "found. Her case remains open and unsolved. Her disappearance is "
            "among the cases cited by Indigenous advocates as proof that the "
            "RCMP's decision to stop adding cases after 2006 was a political "
            "decision, not a reflection of reality on the highway."
        ),
        "city":           "Prince George",
        "state":          "DC",
        "lat":            53.9171,
        "lng":            -122.7497,
        "source_url":     "https://www.ebsco.com/research-starters/law/highway-tears",
        "source_name":    "EBSCO Research Starters / RCMP",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2011-05-01",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # NATIONAL INQUIRY — Genocide finding, 2019
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "stat_mmiwg_national_inquiry_canada_2019",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "Canada's National Inquiry into Missing and Murdered Indigenous "
            "Women and Girls (MMIWG) released its final report, 'Reclaiming "
            "Power and Place,' in June 2019. Key findings: "
            "The violence against Indigenous women and girls in Canada amounts "
            "to genocide — a finding backed by legal analysis and testimony "
            "from over 2,380 family members, survivors, experts, and Knowledge "
            "Keepers. Indigenous women and girls are 12 times more likely to "
            "be murdered or go missing than non-Indigenous women. Indigenous "
            "women represent 16% of all female homicide victims in Canada "
            "despite being only 4% of the female population. The inquiry "
            "documented 231 individual calls for justice directed at governments, "
            "institutions, social service providers, industries, and all "
            "Canadians. As of 2026, the majority of those calls for justice "
            "remain unimplemented. The RCMP's own 2014 national data found "
            "1,017 Indigenous women murdered between 1980 and 2012 and 164 "
            "missing. Indigenous and family organizations estimate the true "
            "number of missing and murdered Indigenous women and girls across "
            "Canada since 1970 exceeds 4,000. "
            "Source: National Inquiry into MMIWG Final Report, June 2019."
        ),
        "city":           "Ottawa",
        "state":          "DC",
        "lat":            45.4215,
        "lng":            -75.6972,
        "source_url":     "https://www.mmiwg-ffada.ca/final-report/",
        "source_name":    "National Inquiry into MMIWG — Final Report 2019",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2019-06-03",
        "tab":            "global",
        "country":        "Canada",
    },

]


def main():
    print("\n  [Medusa] Seeding Highway of Tears...\n")
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
    print("  NOTE: All records use state='DC' as a placeholder for Canadian")
    print("  cases. Real coordinates are accurate. tab='global' and")
    print("  country='Canada' are set for frontend filtering.\n")


if __name__ == "__main__":
    main()
