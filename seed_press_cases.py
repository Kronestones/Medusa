#!/usr/bin/env python3
"""
seed_press_cases.py — Renee Nicole Good (ICE killing, 2026) and
MindGeek/Pornhub (monetization of rape, child abuse, trafficking).

Sources: CNN, NYT, The Advocate, New Republic, Wikipedia, court records,
NCMEC, congressional testimony.

Run: python3 seed_press_cases.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    # ── RENEE NICOLE GOOD ─────────────────────────────────────────────────────
    {
        "summary": (
            "Killing of Renee Nicole Good — ICE Agent Jonathan Ross, Minneapolis, "
            "January 8, 2026. Renee Nicole Good, 37, was a mother of three, married "
            "to her wife Becca, and a member of her south Minneapolis community who "
            "had been peacefully observing and documenting ICE operations in her "
            "neighborhood — a legal act. That morning she stopped her maroon Honda "
            "Pilot during Operation Metro Surge to check on neighbors. ICE agents "
            "surrounded her vehicle, pulled on the doors, and demanded she exit. "
            "When she attempted to drive away, agent Jonathan Ross — who was in "
            "front of the vehicle — fired three shots. Good was shot in the face. "
            "She died from a gunshot wound to the head. Her last words to Ross: "
            "'That's fine dude. I'm not mad at you.' "
            "Ross's own cellphone footage, analyzed by the New York Times, captured "
            "him muttering 'fucking bitch' as Good's vehicle crashed. Good was "
            "barred from receiving medical aid for 15 minutes. A bystander who "
            "rushed to help was told by an agent: 'No, back up now.' Becca Good "
            "was present, covered in blood, crying: 'You guys just killed my wife.' "
            "Video analysis by the NYT shows Ross was stepping clear of the SUV's "
            "path when he fired — directly contradicting the Trump administration's "
            "claim of self-defense. Trump claimed Good 'ran the officer over.' "
            "Minneapolis mayor Jacob Frey called that 'bullshit.' DHS Secretary "
            "Kristi Noem smiled during a CNN interview when asked about the "
            "'fucking bitch' remark. ICE agents subsequently used Good's death "
            "as a threat: 'Stop following us — that's why that lesbian bitch is dead.' "
            "Minnesota Governor Tim Walz proclaimed January 9 'Renee Good Day.' "
            "Minneapolis police chief Brian O'Hara called her killing 'predictable "
            "and preventable.' Bruce Springsteen dedicated a song to her and released "
            "'Streets of Minneapolis' — which charted number one in 19 countries. "
            "As of May 2026, ICE agent Jonathan Ross has faced no criminal charges."
        ),
        "city": "Minneapolis", "state": "MN",
        "lat": 44.9375, "lng": -93.2694,
        "date_incident": "2026-01-08",
        "violence_type": "homicide",
        "status": "reported",
        "source_url": "https://en.wikipedia.org/wiki/Killing_of_Ren%C3%A9e_Good",
        "source_name": "Wikipedia — Killing of Renee Good / CNN / NYT / The Advocate / New Republic",
        "verified": True,
        "is_public_figure": False,
    },

    # ── MINDGEEK / PORNHUB ────────────────────────────────────────────────────
    {
        "summary": (
            "MindGeek / Pornhub — Monetization of Rape, Child Abuse, and Trafficking. "
            "MindGeek (now rebranded Aylo), a Montreal-based corporation, owns "
            "Pornhub and over 100 pornography websites. A December 2020 New York "
            "Times investigation by Nicholas Kristof — 'The Children of Pornhub' — "
            "documented that the site hosted videos of child rape, sex trafficking, "
            "nonconsensual recordings, spy cam footage of women showering, and women "
            "being asphyxiated. A search for 'girls under 18' on the site returned "
            "over 100,000 videos. The National Center for Missing and Exploited "
            "Children reported receiving 69.2 million reports of child sexual "
            "exploitation content in 2019 alone — up from 6.5 million in 2015. "
            "A CNN investigation found that 62 million people — mostly men — visited "
            "an illicit website hosting rape content in a single month. "
            "Internal MindGeek emails revealed a backlog of 706,425 videos reported "
            "as possible rape or child abuse — which MindGeek deliberately chose "
            "not to review. MindGeek had reported zero cases of child sexual abuse "
            "material to Canadian authorities — as required by law — until 2020. "
            "Only 80 moderators reviewed content for a platform generating 1.39 "
            "million hours of uploads per year. A former employee said the goal "
            "was to 'let as much content as possible go through.' A MindGeek "
            "technical manager was caught on undercover video admitting rapists and "
            "traffickers exploit a verification loophole — and the company had not "
            "fixed it because doing so would cost money. Under pressure from the "
            "investigation, Visa and Mastercard suspended payment processing. "
            "Pornhub removed 10 million videos overnight. Multiple class action "
            "lawsuits followed, including a $600 million Canadian class action and "
            "an $80 million US suit by 40 trafficking survivors. Serena Fleites — "
            "who was 13 when her rape video was uploaded to Pornhub, received "
            "millions of views, and could not get it removed for years — sued "
            "MindGeek and Visa. Judge Cormac Carney ruled Visa was not an innocent "
            "party. The case is ongoing."
        ),
        "city": "Los Angeles", "state": "CA",
        "lat": 34.0522, "lng": -118.2437,
        "date_incident": "2020-12-04",
        "violence_type": "trafficking",
        "status": "investigated",
        "source_url": "https://www.nytimes.com/2020/12/04/opinion/sunday/pornhub-rape-trafficking.html",
        "source_name": "NYT — The Children of Pornhub, Kristof 2020 / CNN Investigation / Court Records",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Serena Fleites — Raped at 13, Video on Pornhub for Years. Serena "
            "Fleites was 13 years old when her boyfriend convinced her to make a "
            "sexual video. He posted it online without her consent. It was uploaded "
            "to Pornhub — where it received millions of views. Fleites found it, "
            "reported it, and begged for its removal. Pornhub did not remove it. "
            "It was re-uploaded repeatedly. Her school discovered the videos. She "
            "was bullied out of school, became homeless, developed addiction, and "
            "attempted suicide multiple times. The video continued circulating for "
            "years. She was one of the survivors whose story Nicholas Kristof "
            "documented in the 2020 New York Times investigation that finally forced "
            "Pornhub to act. She subsequently sued MindGeek and Visa. Her case — "
            "Fleites v. MindGeek — became a landmark. Judge Carney ruled Visa "
            "was not an innocent party in the monetization of child rape material. "
            "Serena Fleites's story is the story of thousands of girls and women "
            "whose abuse was uploaded, monetized, and watched by millions — while "
            "every removal request was ignored."
        ),
        "city": "Stockton", "state": "CA",
        "lat": 37.9577, "lng": -121.2908,
        "date_incident": "2020-12-04",
        "violence_type": "child_abuse",
        "status": "investigated",
        "source_url": "https://www.nytimes.com/2020/12/04/opinion/sunday/pornhub-rape-trafficking.html",
        "source_name": "NYT — The Children of Pornhub / Fleites v. MindGeek Court Records",
        "verified": True,
        "is_public_figure": False,
    },
]


def main():
    print("[Seed Press Cases] Seeding Renee Nicole Good and MindGeek/Pornhub records...")
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
    print(f"[Seed Press Cases] {saved}/{len(RECORDS)} records saved.")
    print(f"Total in database: {get_case_count()}")


if __name__ == "__main__":
    main()
