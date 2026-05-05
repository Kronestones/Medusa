#!/usr/bin/env python3
"""
seed_technology_abuse.py — Technology-facilitated abuse: AI-generated
deepfake pornography, stalkerware, sextortion, non-consensual intimate
image sharing (revenge porn), and online harassment campaigns.

Sources: FBI, FTC, Cyber Civil Rights Initiative, court records,
congressional testimony, investigative journalism.

Run: python3 seed_technology_abuse.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    # ── AI DEEPFAKE ABUSE ─────────────────────────────────────────────────────
    {
        "summary": (
            "AI-Generated Deepfake Pornography — Epidemic Against Women and Girls. "
            "AI image generation tools have enabled the mass production of "
            "non-consensual synthetic pornographic images of real women. A 2023 "
            "report by Home Security Heroes found that deepfake pornography "
            "videos online increased 464% between 2019 and 2023 — with 98% of "
            "deepfake videos being pornographic and 99% of targets being women. "
            "Tools to create deepfake pornography are freely available online, "
            "require no technical skill, and can generate realistic explicit images "
            "from a single clothed photograph in minutes. Victims include celebrities, "
            "politicians, journalists, teachers, and schoolgirls. In 2024, explicit "
            "AI-generated images of Taylor Swift were viewed hundreds of millions "
            "of times before platforms removed them — drawing national attention "
            "to the lack of federal law. As of 2024, no comprehensive federal law "
            "criminalizes AI-generated non-consensual intimate images. Fewer than "
            "half of US states have laws covering synthetic NCII. The technology "
            "is advancing faster than legislation in every jurisdiction."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2024-01-25",
        "violence_type": "harassment",
        "status": "documented",
        "source_url": "https://www.homesecurityheroes.com/state-of-deepfakes/",
        "source_name": "Home Security Heroes — State of Deepfakes 2023 / Cyber Civil Rights Initiative",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Deepfake Pornography in Schools — Girls as Young as 11 Targeted. "
            "In 2023 and 2024, multiple incidents were documented in US middle "
            "and high schools in which male students used AI tools to generate "
            "explicit fake images of female classmates and distribute them. "
            "Documented cases occurred in New Jersey, Washington state, Texas, "
            "California, and Florida — and these are only the reported incidents. "
            "In Westfield, New Jersey, approximately 30 girls aged 14-15 were "
            "targeted. In Beverly Hills, explicit AI images of female students "
            "were shared in group chats. In most cases, school administrators "
            "had no policy to address the conduct, police said no crime had been "
            "committed under existing law, and the girls were left without recourse. "
            "The psychological harm — equivalent to having real intimate images "
            "distributed — is severe and documented. Congress introduced the "
            "DEFIANCE Act (2024) to address AI-generated NCII, but as of 2024 "
            "it had not passed into law."
        ),
        "city": "Westfield", "state": "NJ",
        "lat": 40.6590, "lng": -74.3474,
        "date_incident": "2023-10-20",
        "violence_type": "harassment",
        "status": "documented",
        "source_url": "https://www.nytimes.com/2024/04/08/technology/deepfake-ai-images-schools.html",
        "source_name": "NYT — Deepfake AI Images in Schools 2024",
        "verified": True,
        "is_public_figure": False,
    },

    # ── STALKERWARE ───────────────────────────────────────────────────────────
    {
        "summary": (
            "Stalkerware — Commercial Spyware Sold to Abusers. Stalkerware refers "
            "to commercially available surveillance applications marketed as "
            "parental monitoring tools or employee trackers — but used by intimate "
            "partners to covertly monitor victims. These apps hide from the victim's "
            "phone screen, transmit location, messages, calls, photos, and keystrokes "
            "to the abuser in real time. The Coalition Against Stalkerware documented "
            "a 93% increase in stalkerware detections between 2019 and 2020. "
            "The FTC took action against SpyFone and Support King (2021) — the "
            "first FTC enforcement action against a stalkerware company — requiring "
            "the company to delete illegally collected data and banning its CEO "
            "from the surveillance business. But hundreds of stalkerware apps "
            "remain available. The apps are legal to sell in most US states. "
            "DV advocates document that stalkerware is found on victims' phones "
            "in the majority of technology-facilitated DV cases — and that "
            "abusers use the information to intercept escape plans, find shelter "
            "locations, and track victims who have fled."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2021-09-01",
        "violence_type": "stalking",
        "status": "documented",
        "source_url": "https://www.ftc.gov/news-events/news/press-releases/2021/09/ftc-bans-spyfone-support-king-surveillance-business",
        "source_name": "FTC — SpyFone Action 2021 / Coalition Against Stalkerware",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Stalkerware and Domestic Violence Shelters — Location Tracking Puts "
            "Survivors at Risk. The National Domestic Violence Hotline and shelter "
            "networks across the US have documented cases in which abusers used "
            "stalkerware to locate survivors who had fled to confidential shelter "
            "locations. When a survivor takes their phone to a shelter, any "
            "stalkerware installed by the abuser continues transmitting location "
            "data — compromising not just the survivor but all residents of the "
            "shelter. DV advocates recommend survivors leave their devices behind "
            "or undergo device screening — but many survivors cannot afford "
            "replacement phones and are not aware their device is compromised. "
            "Tech safety programs at organizations including the Safety Net "
            "Project have trained thousands of advocates in device screening — "
            "but the programs reach only a fraction of those at risk. Stalkerware "
            "developers face no legal obligation to prevent domestic abuse use cases "
            "despite documented harm."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-01-01",
        "violence_type": "stalking",
        "status": "documented",
        "source_url": "https://www.techsafety.org/stalkerware",
        "source_name": "Safety Net Project — Stalkerware and DV / NNEDV",
        "verified": True,
        "is_public_figure": False,
    },

    # ── SEXTORTION ────────────────────────────────────────────────────────────
    {
        "summary": (
            "Sextortion — FBI Documents Explosive Growth, Girls Primary Targets. "
            "Sextortion — using intimate images or the threat of their release to "
            "coerce money or additional sexual content — has grown dramatically "
            "with the proliferation of social media and messaging apps. The FBI "
            "reported a 322% increase in sextortion reports between 2021 and 2023. "
            "The National Center for Missing and Exploited Children documented "
            "over 26,700 sextortion reports in 2023. Girls and young women are "
            "the primary targets of relationship-based sextortion — where an "
            "intimate partner or someone posing as one obtains intimate images "
            "and then uses them for control or profit. Financial sextortion — "
            "in which strangers extort money using images obtained through hacking, "
            "catfishing, or AI generation — primarily targets boys. At least "
            "20 minors have died by suicide in the US following sextortion "
            "campaigns. The FBI has issued multiple national alerts about "
            "sextortion targeting minors. Federal prosecution is possible under "
            "existing statutes but requires extensive investigation."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-06-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.fbi.gov/news/stories/sextortion-a-growing-threat",
        "source_name": "FBI — Sextortion Alert / NCMEC 2023",
        "verified": True,
        "is_public_figure": False,
    },

    # ── NON-CONSENSUAL INTIMATE IMAGES ────────────────────────────────────────
    {
        "summary": (
            "Non-Consensual Intimate Image Sharing (Revenge Porn) — Legal Patchwork "
            "Leaves Most Victims Without Recourse. Non-consensual intimate image "
            "sharing (NCII) — commonly called revenge porn — involves distributing "
            "intimate images of a person without their consent, typically by a "
            "former partner. The Cyber Civil Rights Initiative estimates that "
            "1 in 8 social media users has been threatened with or experienced "
            "NCII. 90% of victims are women. Victims report job loss, depression, "
            "PTSD, and suicidal ideation at high rates. As of 2024, 48 states "
            "have NCII laws — but the laws vary enormously in scope, penalties, "
            "and whether they cover images obtained consensually and later shared "
            "non-consensually. Section 230 of the Communications Decency Act has "
            "historically shielded platforms from liability for hosting NCII. "
            "The SHIELD Act — which would create a federal NCII crime — has been "
            "introduced in Congress repeatedly without passing. Platforms including "
            "Meta, Google, and Twitter/X have implemented reporting tools but "
            "removal is inconsistent and re-uploading is common."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2024-01-01",
        "violence_type": "harassment",
        "status": "documented",
        "source_url": "https://cybercivilrights.org/ncii-statistics/",
        "source_name": "Cyber Civil Rights Initiative — NCII Statistics / SHIELD Act",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Holly Jacobs — Founded Cyber Civil Rights Initiative After NCII "
            "Destroyed Her Career. Holly Jacobs, a PhD student in Florida, "
            "discovered in 2009 that explicit images her ex-partner had taken "
            "were posted online without her consent. They spread to dozens of "
            "sites. Her name, employer, and contact information were posted "
            "alongside the images — leading to harassment, threats, and job loss. "
            "She spent years trying to get images removed and to convince law "
            "enforcement to act — finding no legal recourse and no platform "
            "accountability. In 2012 she founded the Cyber Civil Rights Initiative, "
            "which has since assisted over 10,000 survivors and advocated "
            "successfully for NCII laws in dozens of states. Her case illustrates "
            "the gap that existed — and in many jurisdictions still exists — "
            "between the severity of harm caused by NCII and the legal tools "
            "available to survivors. She testified before Congress multiple times."
        ),
        "city": "Miami", "state": "FL",
        "lat": 25.7617, "lng": -80.1918,
        "date_incident": "2009-01-01",
        "violence_type": "harassment",
        "status": "documented",
        "source_url": "https://cybercivilrights.org/about/",
        "source_name": "Cyber Civil Rights Initiative — Founder Story",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Online Harassment and Gamergate — Coordinated Campaigns Against Women. "
            "Gamergate (2014) was a coordinated harassment campaign targeting women "
            "in gaming — particularly game developers and critics Zoe Quinn, Anita "
            "Sarkeesian, and Brianna Wu. Targets received thousands of death threats, "
            "rape threats, doxxing (publication of home addresses and personal "
            "information), and swatting (false emergency calls to send armed police "
            "to their homes). Multiple women were driven from their homes. Law "
            "enforcement largely failed to act. Gamergate became a template for "
            "subsequent coordinated online harassment campaigns against women "
            "journalists, politicians, scientists, and public figures. The tactics "
            "— organized on platforms including 4chan, 8chan, and Reddit — were "
            "later adopted by political extremist movements. Research documents "
            "that women receive the majority of severe online harassment including "
            "sexual threats. Online harassment causes women to self-censor, "
            "withdraw from public life, and leave fields — a documented chilling "
            "effect on women's participation in public discourse."
        ),
        "city": "San Francisco", "state": "CA",
        "lat": 37.7749, "lng": -122.4194,
        "date_incident": "2014-08-16",
        "violence_type": "harassment",
        "status": "documented",
        "source_url": "https://www.pewresearch.org/internet/2017/07/11/online-harassment-2017/",
        "source_name": "Pew Research — Online Harassment 2017 / ADL Gamergate Report",
        "verified": True,
        "is_public_figure": False,
    },
]


def main():
    print("[Seed Technology Abuse] Seeding deepfakes, stalkerware, sextortion, and NCII records...")
    init_db()
    saved = 0
    for rec in RECORDS:
        normalized = normalize_record(rec)
        if normalized:
            if save_case(normalized):
                saved += 1
            else:
                print(f"  Already exists: {normalized.get('case_id', '?')}")
        else:
            print(f"  Skipped: {rec.get('summary','')[:60]}")

    from medusa.database import get_case_count
    print(f"[Seed Technology Abuse] {saved}/{len(RECORDS)} records saved.")
    print(f"Total in database: {get_case_count()}")


if __name__ == "__main__":
    main()
