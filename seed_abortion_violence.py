#!/usr/bin/env python3
"""
seed_abortion_violence.py — Documented murders, bombings, arsons, and
domestic terrorism targeting abortion providers and clinics in the US.
Sources: NAF Violence and Disruption Statistics, DOJ, FBI, court records.

Run: python3 seed_abortion_violence.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    # ── MURDERS ───────────────────────────────────────────────────────────────
    {
        "summary": (
            "Murder of Dr. George Tiller — Scott Roeder, Wichita, Kansas, May 31, "
            "2009. Dr. George Tiller, one of only a handful of physicians in the US "
            "who performed late-term abortions, was shot and killed by Scott Roeder "
            "while serving as an usher at his church — Reformation Lutheran Church "
            "in Wichita. Tiller had survived a previous assassination attempt in "
            "1993 when anti-abortion extremist Rachelle Shannon shot him in both "
            "arms. He was shot five times in the clinic over the years. His clinic, "
            "Women's Health Care Services, had been bombed, blockaded, and subjected "
            "to years of harassment campaigns by Operation Rescue. Roeder was "
            "convicted of first-degree murder and sentenced to life without parole "
            "for 50 years. After Tiller's murder, no other doctor stepped in to "
            "provide the same services in Kansas — leaving women with wanted "
            "pregnancies facing fatal fetal anomalies or life-threatening conditions "
            "with no local provider. His murder was the culmination of decades of "
            "targeted domestic terrorism against abortion providers."
        ),
        "city": "Wichita", "state": "KS",
        "lat": 37.6872, "lng": -97.3301,
        "date_incident": "2009-05-31",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.courtlistener.com/?q=scott+roeder&type=r",
        "source_name": "Kansas v. Scott Roeder — Court Records / NAF",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Murder of Dr. David Gunn — Michael Griffin, Pensacola, Florida, "
            "March 10, 1993. Dr. David Gunn was shot three times in the back and "
            "killed outside the Pensacola Women's Medical Services clinic by Michael "
            "Griffin. Gunn was one of very few abortion providers serving rural "
            "areas of Florida, Georgia, and Alabama — traveling a circuit to reach "
            "women without local access. Griffin was convicted of first-degree murder "
            "and sentenced to life in prison. His murder was the first assassination "
            "of an abortion provider in US history and marked a turning point in "
            "anti-abortion extremism — demonstrating that violence could succeed "
            "in eliminating providers. The National Abortion Federation has "
            "documented that Dr. Gunn's murder directly inspired subsequent attacks. "
            "The year 1993 alone saw 1 murder, 1 attempted murder, 70 death threats, "
            "and 188 incidents of stalking against abortion providers."
        ),
        "city": "Pensacola", "state": "FL",
        "lat": 30.4213, "lng": -87.2169,
        "date_incident": "1993-03-10",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://prochoice.org/education-and-advocacy/violence/violence-statistics-and-history/",
        "source_name": "NAF — Violence Statistics and History / Florida v. Griffin",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Murder of Dr. John Britton and James Barrett — Paul Hill, Pensacola, "
            "Florida, July 29, 1994. Paul Hill shot and killed Dr. John Britton and "
            "his escort James Barrett outside the Ladies Center clinic in Pensacola "
            "— the same clinic where Dr. Gunn had been murdered 16 months earlier. "
            "Barrett's wife June was also shot and wounded. Hill was a former "
            "Presbyterian minister who had publicly advocated for killing abortion "
            "providers. He was convicted of first-degree murder and executed by "
            "the state of Florida in 2003. Hill stated he had 'no regrets' and "
            "expected 'a great reward in heaven.' He became a martyr figure in "
            "violent anti-abortion networks. The Army of God — a domestic terrorist "
            "organization — maintains a 'Hall of Heroes' on its website honoring "
            "abortion provider murderers including Hill, Roeder, and others."
        ),
        "city": "Pensacola", "state": "FL",
        "lat": 30.4213, "lng": -87.2169,
        "date_incident": "1994-07-29",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://prochoice.org/education-and-advocacy/violence/violence-statistics-and-history/",
        "source_name": "NAF Violence Statistics / Florida v. Hill — Court Records",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Murder of Shannon Lowney and Leanne Nichols — John Salvi, Brookline, "
            "Massachusetts, December 30, 1994. John Salvi opened fire at two "
            "abortion clinics in Brookline — Planned Parenthood and Preterm Health "
            "Services — killing receptionists Shannon Lowney, 25, and Leanne "
            "Nichols, 38, and wounding five others. Both victims were clinic staff "
            "— not providers — who were killed simply for working at reproductive "
            "health facilities. Salvi drove to Norfolk, Virginia the next day and "
            "fired into a third clinic without killing anyone. He was convicted of "
            "first-degree murder and died in prison in 1996 in what was ruled a "
            "suicide. The murders drew attention to the danger faced by all clinic "
            "staff — not just physicians — and to the failure of law enforcement "
            "to treat anti-abortion violence as domestic terrorism prior to the "
            "Freedom of Access to Clinic Entrances Act (FACE Act, 1994)."
        ),
        "city": "Brookline", "state": "MA",
        "lat": 42.3318, "lng": -71.1212,
        "date_incident": "1994-12-30",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://prochoice.org/education-and-advocacy/violence/violence-statistics-and-history/",
        "source_name": "NAF Violence Statistics / Massachusetts v. Salvi",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Murder of Dr. Barnett Slepian — James Kopp, Amherst, New York, "
            "October 23, 1998. Dr. Barnett Slepian was shot and killed by a "
            "sniper through the window of his home in Amherst, New York — in "
            "front of his wife and children. James Kopp, an anti-abortion extremist "
            "connected to the Army of God, fired a high-powered rifle through the "
            "kitchen window. Kopp fled the country and was placed on the FBI's "
            "Ten Most Wanted list. He was captured in France in 2001 and extradited. "
            "He was convicted of second-degree murder in 2003 and sentenced to "
            "25 years to life. Kopp was also charged with four other sniper attacks "
            "on abortion providers in Canada and the US — part of a coordinated "
            "campaign in which providers were shot in their homes during the same "
            "weeks of October across multiple years. The pattern indicated "
            "organized coordination that was never fully prosecuted."
        ),
        "city": "Amherst", "state": "NY",
        "lat": 42.9784, "lng": -78.7948,
        "date_incident": "1998-10-23",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.fbi.gov/history/famous-cases/barnett-slepian-murder",
        "source_name": "FBI — Barnett Slepian Murder / New York v. Kopp",
        "verified": True,
        "is_public_figure": True,
    },

    # ── BOMBINGS AND ARSONS ───────────────────────────────────────────────────
    {
        "summary": (
            "Eric Rudolph — Olympic Park Bombing and Abortion Clinic Bombings, "
            "1996–1998. Eric Rudolph carried out a series of bombings targeting "
            "abortion clinics and a lesbian nightclub, as well as the 1996 Atlanta "
            "Olympic Games bombing that killed 2 and injured 111. In January 1997, "
            "he bombed an Atlanta abortion clinic and then bombed a nearby bar "
            "when emergency responders arrived — a secondary device designed to "
            "maximize casualties. In January 1998, he bombed a Birmingham, Alabama "
            "abortion clinic — killing off-duty police officer Robert Sanderson "
            "and critically wounding nurse Emily Lyons, who lost an eye and "
            "suffered over 100 shrapnel wounds. Rudolph was on the FBI's Most "
            "Wanted list for five years. He was captured in 2003 living in the "
            "woods of North Carolina. He pleaded guilty and was sentenced to four "
            "consecutive life sentences. He expressed no remorse and stated his "
            "bombings were justified as resistance to abortion."
        ),
        "city": "Birmingham", "state": "AL",
        "lat": 33.5186, "lng": -86.8104,
        "date_incident": "1998-01-29",
        "violence_type": "assault",
        "status": "convicted",
        "source_url": "https://www.fbi.gov/history/famous-cases/eric-robert-rudolph",
        "source_name": "FBI — Eric Rudolph / US v. Rudolph Court Records",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Colorado Springs Planned Parenthood Shooting — Robert Dear, "
            "November 27, 2015. Robert Dear opened fire at a Planned Parenthood "
            "clinic in Colorado Springs, killing three people — including a police "
            "officer — and wounding nine others in a five-hour standoff. After his "
            "arrest, Dear told investigators 'no more baby parts' — referencing "
            "deceptively edited undercover videos released by the Center for Medical "
            "Progress that falsely claimed Planned Parenthood sold fetal tissue. "
            "Republican politicians including Carly Fiorina had repeated the false "
            "claims in the weeks before the shooting. Dear was found incompetent "
            "to stand trial and committed to a state mental health facility. "
            "Advocacy organizations documented that inflammatory rhetoric about "
            "abortion providers — including false 'baby parts' claims — directly "
            "preceded a spike in threats and violence against clinics in 2015."
        ),
        "city": "Colorado Springs", "state": "CO",
        "lat": 38.8339, "lng": -104.8214,
        "date_incident": "2015-11-27",
        "violence_type": "homicide",
        "status": "documented",
        "source_url": "https://www.nytimes.com/2015/11/29/us/planned-parenthood-shooting.html",
        "source_name": "NYT — Colorado Springs Planned Parenthood Shooting / Court Records",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "National Abortion Federation — Scale of Anti-Abortion Violence 1977–2024. "
            "The National Abortion Federation has tracked violence against abortion "
            "providers since 1977. Documented incidents include: 11 murders, "
            "26 attempted murders, 42 bombings, 185 arsons, 100 butyric acid attacks, "
            "663 anthrax threats, 13 attempted bombings, 655 bioterrorism threats, "
            "4 kidnappings, 428 death threats, 1,630 cases of stalking, and over "
            "26,000 incidents of obstruction. The FACE Act (Freedom of Access to "
            "Clinic Entrances, 1994) made blocking clinic access a federal crime — "
            "but enforcement has been inconsistent. In 2022, the Biden DOJ prosecuted "
            "multiple FACE Act violations for the first time in years. The Trump "
            "administration has signaled it will not enforce the FACE Act. "
            "Post-Dobbs, clinic closures have accelerated and remaining providers "
            "face intensified targeting. The NAF documents that violence against "
            "providers increases measurably following inflammatory political rhetoric."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2024-01-01",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://prochoice.org/education-and-advocacy/violence/violence-statistics-and-history/",
        "source_name": "National Abortion Federation — Violence and Disruption Statistics 2024",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Army of God — Domestic Terrorist Network Targeting Abortion Providers. "
            "The Army of God is a loosely organized domestic terrorist network "
            "that has claimed responsibility for or celebrated murders, bombings, "
            "and arsons targeting abortion providers since the 1980s. Its manual — "
            "the Army of God Manual — provides instructions for clinic bombings, "
            "butyric acid attacks, and other violent tactics. The manual has been "
            "found in the possession of convicted clinic bombers and murderers "
            "including Eric Rudolph, James Kopp, and Clayton Waagner — who sent "
            "anthrax threat letters to 554 abortion clinics in 2001. The Army of "
            "God website maintains a 'Hall of Heroes' celebrating convicted "
            "murderers of abortion providers. The FBI has classified the group "
            "as a domestic terrorist organization. Despite this, prosecutions of "
            "network members for conspiracy — rather than individual acts — have "
            "been rare. The organization continues to operate openly online."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2001-10-01",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://www.splcenter.org/fighting-hate/extremist-files/group/army-god",
        "source_name": "SPLC — Army of God / FBI Domestic Terrorism Classification",
        "verified": True,
        "is_public_figure": False,
    },
]


def main():
    print("[Seed Abortion Violence] Seeding abortion provider murders, bombings, and domestic terrorism records...")
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
    print(f"[Seed Abortion Violence] {saved}/{len(RECORDS)} records saved.")
    print(f"Total in database: {get_case_count()}")


if __name__ == "__main__":
    main()
