"""
seed_honor_killings.py — Medusa

Honor killings — documented US cases and global statistics.
Includes the critical framing: the same dynamic (killing a woman
for perceived sexual autonomy or disobedience) is labeled
"honor killing" when perpetrated by MENA/South Asian immigrants
and "domestic violence" or "crime of passion" when perpetrated
by white American men. Medusa documents the pattern, not the label.

Cases:
  - Amina Said and Sarah Said — Irving TX, 2008 (convicted 2022)
  - Noor Almaleki — Peoria AZ, 2009
  - Romina Ashrafi — Iran, 2020 (Global)
  - Mona Heydari — Iran, 2022 (Global)
  - Statistics: US, global, UN data
  - The double standard in classification

Run:
    cd ~/medusa && python3 seed_honor_killings.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [

    # ══════════════════════════════════════════════════════════════════════════
    # HONOR KILLINGS — Systemic overview and double standard
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "stat_honor_killings_us_overview",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "An estimated 23–27 honor killings occur in the United States "
            "every year, according to DOJ-funded research — though the true "
            "number is believed to be significantly higher because honor killings "
            "are routinely misclassified by law enforcement as domestic violence "
            "or general homicide. Law enforcement has no standardized system "
            "to track or identify honor-motivated killings. "
            "Worldwide, an estimated 5,000 women and girls are murdered in "
            "honor killings every year, according to the UN. The average age "
            "of victims globally is 23. Two-thirds of honor killings are "
            "carried out by some form of family collaboration — not a single "
            "perpetrator but a coordinated group decision. "
            "Honor killings are not confined to any single religion or culture. "
            "They have been documented among Muslim, Hindu, Sikh, Christian, "
            "and Jewish communities. The common thread is not religion — it "
            "is patriarchal control of female sexuality and autonomy. "
            "A woman is killed for: refusing an arranged marriage; dating "
            "someone her family disapproves of; being raped (and therefore "
            "considered 'impure'); seeking divorce; leaving the family home; "
            "being perceived as 'too Western'; or any other act interpreted "
            "as threatening the family's male-defined honor. "
            "CRITICAL FRAMING: Research published in the Century Foundation "
            "documents that in the United States, killings motivated by the "
            "exact same logic — a man killing a woman to punish her for "
            "perceived sexual autonomy, disobedience, or departure — are "
            "classified as 'honor killings' almost exclusively when the "
            "perpetrator is an immigrant from the Middle East, North Africa, "
            "or South Asia. When the perpetrator is white and American, the "
            "identical dynamic is classified as 'domestic violence,' 'crime "
            "of passion,' or simply 'murder.' This classification difference "
            "is not based on the nature of the crime — it is based on the "
            "race and origin of the perpetrator. Medusa documents the pattern, "
            "not the label. The same logic that kills Amina Said kills women "
            "in towns across America every day. "
            "Sources: DOJ / BJS Exploratory Study on Honor Violence; "
            "Tahirih Justice Center; Century Foundation; UN Women; "
            "Journal of Criminal Law (Sage, 2024)."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://www.ojp.gov/pdffiles1/bjs/grants/248879.pdf",
        "source_name":    "DOJ / BJS Exploratory Study on Honor Violence",
        "additional_sources": [
            {"url": "https://www.tahirih.org/who-we-serve/forms-of-violence/honor-crimes/",
             "name": "Tahirih Justice Center"},
            {"url": "https://tcf.org/content/report/kuwait-america-gender-based-killings-considered-less-murder/",
             "name": "Century Foundation — From Kuwait to America"},
            {"url": "https://journals.sagepub.com/doi/10.1177/00111287221128482",
             "name": "Journal of Criminal Law — Honor Killings in the US 1990–2021 (2024)"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2008-01-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # AMINA SAID + SARAH SAID — Irving TX, killed Jan 1 2008, convicted 2022
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "amina_sarah_said_irving_tx_2008",
        "violence_type":  "homicide",
        "status":         "convicted",
        "summary": (
            "Amina Said, 18, and Sarah Said, 17, were shot and killed by their "
            "father Yaser Abdel Said in Irving, Texas on New Year's Day 2008. "
            "Their bodies were found slumped in their father's taxicab outside "
            "the Omni Hotel in Irving. Sarah was shot nine times. Amina was "
            "shot twice. As she lay dying, Sarah called 911: 'Help — my dad "
            "shot me! I'm dying! I'm dying!' "
            "Prosecutors said Yaser Said, an Egyptian-born US citizen, murdered "
            "his daughters because they had been dating non-Muslim boyfriends "
            "and embracing an independent American life — which he viewed as "
            "dishonorable. He had previously put a gun to Amina's head and "
            "threatened to kill her. He had been sexually and physically "
            "abusing both girls throughout their childhood. "
            "Ten days before her death, Amina emailed her history teacher: "
            "'He will, without any drama nor doubt, kill us.' "
            "Sarah had been forced to reject an arranged marriage with an "
            "older man she had never met. "
            "After the killings, Yaser Said fled. He was placed on the FBI's "
            "Ten Most Wanted list and evaded arrest for 12 years, hiding at "
            "a family property in Justin, Texas. He was arrested in August 2020. "
            "His son Islam Said and his brother Yassim Said were subsequently "
            "convicted of helping him evade arrest for over a decade. "
            "In August 2022, Yaser Said was convicted of capital murder and "
            "sentenced to life in prison without parole. "
            "Their mother Patricia Owens told Said in her impact statement: "
            "'You took my life. You took my family all in one night.' "
            "Sources: ABC News; Dallas Morning News; AP; Court TV."
        ),
        "city":           "Irving",
        "state":          "TX",
        "lat":            32.8140,
        "lng":            -96.9489,
        "source_url":     "https://abcnews.go.com/US/yaser-said-guilty-of-capital-murder/story?id=88110253",
        "source_name":    "ABC News / Dallas County Court Records",
        "additional_sources": [
            {"url": "https://www.courttv.com/news/man-going-on-trial-in-texas-in-2008-slaying-of-2-daughters/",
             "name": "Court TV"},
            {"url": "https://lawandcrime.com/crime/texas-man-convicted-of-fatally-shooting-his-daughters-in-obsessive-honor-killings/",
             "name": "Law & Crime"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2008-01-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # NOOR ALMALEKI — Peoria AZ, run over by father, 2009
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "noor_almaleki_peoria_az_2009",
        "violence_type":  "homicide",
        "status":         "convicted",
        "summary": (
            "Noor Almaleki, 20, an Iraqi-American young woman in Peoria, "
            "Arizona, died on November 2, 2009, two weeks after her father "
            "Faleh Hassan Almaleki, 48, deliberately ran her over with his "
            "Jeep Grand Cherokee in a parking lot. She was struck along with "
            "Amal Khalaf, 43 — the mother of Noor's boyfriend — who survived "
            "with serious injuries. "
            "Noor had been living independently, had a boyfriend, wore Western "
            "clothing, and had refused an arranged marriage in Iraq. Her father "
            "told investigators he had run her over because she had 'brought "
            "shame on the family' by abandoning traditional Iraqi and Islamic "
            "values. He fled to the UK after the attack and was extradited. "
            "Faleh Hassan Almaleki was convicted of second-degree murder and "
            "aggravated assault in 2011 and sentenced to 34.5 years in prison. "
            "Noor Almaleki had come to the United States as a child with her "
            "family seeking a better life. She was killed for living it. "
            "Sources: Arizona Republic; AP; Maricopa County Superior Court."
        ),
        "city":           "Peoria",
        "state":          "AZ",
        "lat":            33.5806,
        "lng":            -112.2374,
        "source_url":     "https://www.azcentral.com/story/news/local/peoria/2019/11/02/noor-almaleki-honor-killing-peoria-10-years-later/4122730002/",
        "source_name":    "Arizona Republic / Maricopa County Court Records",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2009-10-20",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ROMINA ASHRAFI — Iran, beheaded by father while sleeping, May 2020
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "romina_ashrafi_iran_2020",
        "violence_type":  "homicide",
        "status":         "convicted",
        "summary": (
            "Romina Ashrafi was a 14-year-old Iranian girl who was beheaded "
            "by her father, Reza Ashrafi, with a sickle while she slept in "
            "her home in Gilan Province, Iran, in May 2020. "
            "Romina had eloped with a 29-year-old man, Bahram Azimi, whom "
            "her family refused to let her marry. When police found them "
            "and returned her to her family, she begged officers not to send "
            "her home, reportedly saying she feared her father would kill her. "
            "Police returned her anyway. Her father killed her that night. "
            "Under Iranian law at the time, a father who kills his own child "
            "faces a maximum sentence of 3 to 10 years — not the death penalty "
            "that applies to other murders — because under Iranian penal code "
            "a parent cannot be executed for killing their own child. "
            "Reza Ashrafi was sentenced to 9 years in prison. "
            "Romina's death sparked outrage in Iran and briefly reignited "
            "debate about amending the law protecting fathers who kill children. "
            "No legislative change was made. "
            "Bahram Azimi, the man she had eloped with, was charged and "
            "sentenced to prison for 'inciting' the situation. "
            "Romina Ashrafi was 14 years old. She asked for protection "
            "and was sent home to die. "
            "Sources: BBC Persian; The Guardian; Wikipedia — List of honor "
            "killings in Iran."
        ),
        "city":           "Tehran",
        "state":          "DC",
        "lat":            37.2809,
        "lng":            49.5832,
        "source_url":     "https://www.theguardian.com/global-development/2020/jun/05/iran-fury-at-14-year-old-girls-beheading-by-her-father",
        "source_name":    "The Guardian / BBC Persian",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2020-05-01",
        "tab":            "global",
        "country":        "Iran",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MONA HEYDARI — Iran, beheaded by husband, head paraded through streets
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "mona_heydari_iran_2022",
        "violence_type":  "homicide",
        "status":         "convicted",
        "summary": (
            "Mona Heydari, 17 years old, was beheaded by her husband Sajjad "
            "Heydari, 21, in Ahvaz, Khuzestan Province, Iran, in February 2022. "
            "Mona had briefly left the family home with their toddler son and "
            "had been in contact with another man. Her husband and his brother "
            "lured her back, killed her, and then Sajjad walked through the "
            "streets of Ahvaz holding her severed head — photographed and "
            "filmed. The images spread on social media. "
            "Mona had been married at age 12 or 13 in a child marriage. "
            "Under Iranian law, her husband faced a reduced sentence because "
            "she was his wife and the killing was framed as an 'honor' matter. "
            "Sajjad Heydari was sentenced to 8 years in prison. "
            "The case triggered international outrage and renewed calls to "
            "reform Iranian laws that provide legal protection and reduced "
            "sentences for men who kill female family members. "
            "Mona Heydari was 17 years old. She had been married for years "
            "before she was legally old enough to drive. "
            "Sources: BBC; The Guardian; Wikipedia — List of honor killings "
            "in Iran."
        ),
        "city":           "Ahvaz",
        "state":          "DC",
        "lat":            31.3183,
        "lng":            48.6706,
        "source_url":     "https://www.theguardian.com/world/2022/feb/06/iran-man-parades-wifes-severed-head-through-streets-after-honour-killing",
        "source_name":    "The Guardian / BBC",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2022-02-01",
        "tab":            "global",
        "country":        "Iran",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # GLOBAL STAT: Countries where honor killing carries reduced sentences
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "stat_honor_killing_legal_protections_global",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "In multiple countries, men who kill female family members in "
            "the name of honor face reduced legal penalties or explicit legal "
            "protection — codified in national law: "
            "Iran: Article 630 of the Iranian Penal Code provides that a "
            "husband who kills his wife upon finding her in the act of adultery "
            "is exempt from prosecution. A father who kills his child faces "
            "a maximum of 3–10 years, not the death penalty. "
            "Jordan: Article 98 of the Jordanian Penal Code historically "
            "allowed 'fit of fury' as a mitigating circumstance — applied "
            "almost exclusively to men who killed female relatives. Jordan "
            "amended this law in 2017 under international pressure, though "
            "enforcement gaps remain. "
            "Pakistan: The Qisas and Diyat Ordinance allows the victim's "
            "family — often the same family that ordered the killing — to "
            "pardon the perpetrator, effectively providing legal impunity "
            "for honor killings within families. Pakistan passed the Anti- "
            "Honor Killing Laws Act in 2016 but implementation remains weak. "
            "Libya: Article 375 of the Libyan Penal Code reduces sentences "
            "for men who kill in defense of family honor. "
            "Iraq, Syria, Yemen: Similar legal mitigations exist in various "
            "forms in law or in judicial practice. "
            "These are not cultural customs operating outside the law — "
            "they are the law. The state itself provides legal cover for "
            "the murder of women who exercise autonomy. "
            "Sources: Century Foundation; UN Women; Tahirih Justice Center; "
            "Human Rights Watch."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://tcf.org/content/report/kuwait-america-gender-based-killings-considered-less-murder/",
        "source_name":    "Century Foundation / UN Women / Human Rights Watch",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2020-01-01",
        "tab":            "global",
        "country":        "Global",
    },

]


def main():
    print("\n  [Medusa] Seeding honor killings...\n")
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
