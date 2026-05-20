"""
seed_new_cases_may2026.py — Medusa

New cases May 2026:
  - Dr. Eric Raul Valladares — Miami plastic surgeon, rape under anesthesia
    allegation, charges declined (May 2026)
  - Dr. Eric Andrew Salata — Naples cosmetic doctor, rape under anesthesia,
    multiple victims (2022)
  - Benjamin O. Gleason — TikTok influencer, 7 victims, decade of abuse,
    arrested March 20, 2026
  - Four Baltimore Police Officers — SF hotel gang rape, charges declined
    May 2026
  - William Monroe Palmer II — SF Sheriff Oversight Commissioner, charges
    dropped April 2024
  - SFPD Officer Simon Chan — rape/DV arrest, charges declined 2020

Run:
    cd ~/medusa && python3 seed_new_cases_may2026.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [

    # ══════════════════════════════════════════════════════════════════════════
    # DR. ERIC RAUL VALLADARES — Miami, rape under anesthesia allegation
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "eric_valladares_miami_fl_2025",
        "violence_type":  "sexual_assault",
        "status":         "credible_allegation",
        "summary": (
            "In September 2025, a patient identified publicly as Elegance Monroe "
            "(also referred to as Ms. Watts) underwent a cosmetic procedure at "
            "Vixen Plastic Surgery in Miami, Florida, performed by Dr. Eric Raul "
            "Valladares, a board-certified plastic surgeon. She alleges she was "
            "raped while sedated under anesthesia. "
            "Within four hours of waking from surgery she went to Jackson Memorial "
            "Hospital, where she says a rape kit was performed and came back "
            "positive — with semen found in her cervix. She also alleges her "
            "uvula was partially detached due to oral sexual trauma sustained "
            "while she was unconscious, and that doctors were forced to surgically "
            "remove it within 72 hours. She says she documented every interaction "
            "with detectives and recorded conversations with investigators. "
            "A second patient also came forward with a similar allegation, "
            "according to NBC 6 South Florida (April 2026). "
            "Miami-Dade police investigated for approximately eight months. "
            "A follow-up rape kit screening conducted by the Miami-Dade Sheriff's "
            "Office found no indication of assault, according to the State "
            "Attorney's closeout memo. In May 2026, the Miami-Dade State "
            "Attorney's Office declined to file criminal charges, citing "
            "insufficient evidence to prove the case beyond a reasonable doubt. "
            "No charges were filed. Valladares' attorney called the allegations "
            "'outrageous' and 'false.' "
            "This case follows a documented national pattern of patients — "
            "primarily women — being sexually assaulted while under anesthesia "
            "by medical personnel. The case gained national attention after "
            "going viral on TikTok and Instagram. "
            "Sources: Miami New Times; The Mary Sue; Court Magazine; NBC 6 "
            "South Florida."
        ),
        "city":           "Miami",
        "state":          "FL",
        "lat":            25.7617,
        "lng":            -80.1918,
        "source_url":     "https://www.miaminewtimes.com/news/how-a-viral-tiktok-ignited-a-firestorm-against-a-miami-plastic-surgery-clinic-40545191/",
        "source_name":    "Miami New Times",
        "additional_sources": [
            {"url": "https://www.themarysue.com/plastic-surgery-allegation-miami/",
             "name": "The Mary Sue"},
            {"url": "https://www.nbcmiami.com/video/nbc-6-news/second-woman-accuses-miami-doctor-of-sexual-assault/3789699/",
             "name": "NBC 6 South Florida"},
        ],
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "2025-09-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # DR. ERIC ANDREW SALATA — Naples FL, rape under anesthesia, 3+ victims
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "eric_salata_naples_fl_2022",
        "violence_type":  "sexual_assault",
        "status":         "charged",
        "summary": (
            "Dr. Eric Andrew Salata, 54, a board-certified physician at Pura Vida "
            "Medical Spa on 5th Avenue in Naples, Florida, was accused by multiple "
            "women of raping them while they were under anesthesia during cosmetic "
            "procedures at his spa. The Naples Police Department confirmed two "
            "women's allegations on November 22, 2022, and stated additional "
            "victims may exist. "
            "The first victim told police that Salata had administered nitrous "
            "oxide; as the sedation wore off, she found Salata performing sexual "
            "intercourse on her. She immediately contacted police and submitted "
            "to a sexual assault examination. A second victim described an "
            "identical pattern. A third woman also came forward. Evidence was "
            "collected and submitted to a lab in all cases. "
            "Salata was arrested by the Collier County Sheriff's Office. "
            "This case is part of a documented and growing pattern of patients — "
            "overwhelmingly women — being sexually assaulted by male medical "
            "professionals while incapacitated under anesthesia or sedation. "
            "Sources: Fox News; NBC2 News Naples; Naples Police Department."
        ),
        "city":           "Naples",
        "state":          "FL",
        "lat":            26.1420,
        "lng":            -81.7948,
        "source_url":     "https://foxnews.com/us/florida-doctor-accused-sexually-assaulting-multiple-women-under-anesthesia-ritzy-cosmetic-studio.amp",
        "source_name":    "Fox News / Naples Police Department",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "2022-11-22",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # BENJAMIN O. GLEASON — TikTok influencer, 7 victims, NY, arrested 2026
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "benjamin_gleason_chatham_ny_2026",
        "violence_type":  "sexual_assault",
        "status":         "charged",
        "summary": (
            "Benjamin O. Gleason, 39, of Chatham, New York — a TikTok influencer "
            "with over one million followers whose bio read 'your girlfriend's "
            "favorite influencer' — was arrested on March 20, 2026 by the New "
            "York State Police Bureau of Criminal Investigation following a "
            "multi-victim sexual abuse investigation. "
            "The investigation began in February 2026 after authorities received "
            "information about incidents of sexual abuse. As the investigation "
            "progressed, police determined the abuse had spanned approximately "
            "a decade — from 2011 to 2021 — and involved at least seven victims "
            "ranging in age from approximately 17 to 27 years old. "
            "A 17-count grand jury indictment was sealed on March 20 and unsealed "
            "March 23, 2026. Charges include three counts of predatory sexual "
            "assault (class A-II felony); three counts of first-degree rape by "
            "forcible compulsion (class B felony); three counts of first-degree "
            "rape of a physically helpless victim (class B felony); four counts "
            "of criminal sexual act in the first degree (class B felony); one "
            "count of second-degree aggravated sexual abuse (class C felony); "
            "one count of first-degree sexual abuse by forcible compulsion "
            "(class D felony); and one count of third-degree rape (class E "
            "felony). He pleaded not guilty. "
            "Gleason was known for sharing content about mental health, "
            "borderline personality disorder, and sobriety with a predominantly "
            "young, female audience. In a recent TikTok he said: 'I'm aware "
            "that most of my following are from the younger generation — mostly "
            "girls.' Authorities believe there may be additional victims. "
            "The Columbia County District Attorney's Office, the Reach Center "
            "of the Mental Health Association of Columbia and Greene County, "
            "and the Child Advocacy Center assisted in the investigation. "
            "Sources: NY State Police; Daily Gazette; CBS6 Albany; TMZ."
        ),
        "city":           "Chatham",
        "state":          "NY",
        "lat":            42.3637,
        "lng":            -73.5954,
        "source_url":     "https://troopers.ny.gov/news/state-police-arrest-chatham-man-following-multi-victim-sexual-abuse-investigation",
        "source_name":    "New York State Police",
        "additional_sources": [
            {"url": "https://www.dailygazette.com/spotlightnews/hv360/news/police_fire_courts/benjamin-gleason-arrest-tiktok/article_8e9a6fd1-ee39-4427-980f-1fc32518ee01.html",
             "name": "Daily Gazette"},
            {"url": "https://cbs6albany.com/news/local/tiktok-influencer-with-1m-followers-arraigned-on-multiple-rape-sexual-assault-charges",
             "name": "CBS6 Albany"},
            {"url": "https://www.tmz.com/2026/03/22/tiktoker-benjamin-gleason-arrested/",
             "name": "TMZ"},
        ],
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "2011-01-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # FOUR BALTIMORE POLICE OFFICERS — SF hotel gang rape, charges declined
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "baltimore_officers_sf_hotel_rape_2026",
        "violence_type":  "sexual_assault",
        "status":         "charges_declined",
        "summary": (
            "In May 2026, the San Francisco District Attorney's Office declined "
            "to press charges against four off-duty Baltimore Police Department "
            "officers who were accused of sexually assaulting a Bay Area woman "
            "at a hotel in San Francisco. The SFPD had initially sought to arrest "
            "two of the four officers on suspicion of rape, indicating investigators "
            "believed they had probable cause. However, the San Francisco District "
            "Attorney's office stated they had insufficient evidence to prove the "
            "case beyond a reasonable doubt at trial, and declined to file charges. "
            "No officers were charged. The victim's identity has not been publicly "
            "disclosed. The case is among a documented national pattern of law "
            "enforcement officers accused of sexual assault who are shielded from "
            "prosecution by prosecutorial deference to police, qualified immunity "
            "culture, and evidentiary standards that consistently disadvantage "
            "sexual assault complainants. "
            "Source: Google AI Overview / SF DA's Office, May 2026."
        ),
        "city":           "San Francisco",
        "state":          "CA",
        "lat":            37.7749,
        "lng":            -122.4194,
        "source_url":     "https://www.sfchronicle.com",
        "source_name":    "San Francisco DA's Office / SF Chronicle",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "2026-05-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # WILLIAM MONROE PALMER II — SF Sheriff Oversight Commissioner
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "william_palmer_sf_sheriff_oversight_2024",
        "violence_type":  "sexual_assault",
        "status":         "charges_declined",
        "summary": (
            "In April 2024, sexual assault charges were dropped against William "
            "Monroe Palmer II, a member of the San Francisco Sheriff's Department "
            "Oversight Board — the civilian body responsible for oversight of the "
            "Sheriff's Department. Prosecutors requested the dismissal, citing a "
            "lack of evidence and raising issues with the alleged victim's "
            "credibility. No conviction was obtained. "
            "The case is notable because it involves a member of a civilian "
            "oversight board — an individual whose role was specifically to "
            "provide accountability for law enforcement — who himself faced "
            "sexual assault charges that were ultimately dropped. "
            "Source: Google AI Overview / SF DA records, 2024."
        ),
        "city":           "San Francisco",
        "state":          "CA",
        "lat":            37.7749,
        "lng":            -122.4194,
        "source_url":     "https://www.sfchronicle.com",
        "source_name":    "San Francisco DA's Office",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "2024-04-01",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SFPD OFFICER SIMON CHAN — rape/DV arrest, charges declined 2020
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "sfpd_simon_chan_rape_dv_2020",
        "violence_type":  "sexual_assault",
        "status":         "charges_declined",
        "summary": (
            "In 2020, SFPD Officer Simon Chan was arrested by local authorities "
            "on suspicion of rape and domestic violence. San Mateo County "
            "prosecutors subsequently declined to press charges against Chan, "
            "citing a lack of evidence sufficient to meet the burden of proof "
            "at trial. Chan was not convicted. "
            "This case is part of a broader pattern documented in San Francisco "
            "and nationally in which police officers accused of sexual assault "
            "and domestic violence face a significantly lower rate of prosecution "
            "and conviction than civilian defendants charged with the same "
            "offenses — a pattern that reflects both prosecutorial reliance on "
            "police as witnesses and institutional protection of officers within "
            "the criminal justice system. "
            "Source: Google AI Overview / San Mateo County DA records, 2020."
        ),
        "city":           "San Francisco",
        "state":          "CA",
        "lat":            37.7749,
        "lng":            -122.4194,
        "source_url":     "https://www.sfchronicle.com",
        "source_name":    "San Mateo County DA's Office",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "2020-01-01",
    },

]


def main():
    print("\n  [Medusa] Seeding new cases May 2026...\n")
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
