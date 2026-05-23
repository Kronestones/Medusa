"""
seed_erasure_expanded.py — Medusa

Erasure tab expansion — 10 new records:
  - Gladys West — built the math behind GPS, erased for decades
  - Ada Lovelace — wrote first computer algorithm 1843, century before
    first computer, credit given to Babbage
  - Chien-Shiung Wu — proved parity violation 1957, Nobel given to
    two male theorists she proved right
  - Vera Rubin — discovered dark matter, nominated for Nobel repeatedly,
    died without one
  - Camille Claudel — brilliant sculptor institutionalized by her family
    while Rodin took credit for her work
  - Judith Leyster — Dutch master painter whose works were relabeled as
    Frans Hals after her death
  - Agent 355 — unnamed female spy critical to American Revolution,
    written entirely out of history
  - Sybil Ludington — rode twice as far as Paul Revere, never got the poem
  - Sister Rosetta Tharpe — invented rock and roll guitar, credited to men
  - Abigail Adams — "Remember the Ladies." He laughed.

Run:
    cd ~/medusa && python3 seed_erasure_expanded.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [

    # ══════════════════════════════════════════════════════════════════════════
    # GLADYS WEST — built the mathematical foundation of GPS
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_gladys_west_gps_mathematician",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Dr. Gladys Mae West (1930–2026) was a Black mathematician from "
            "rural Dinwiddie County, Virginia — a Jim Crow tobacco farm girl "
            "who became the person whose mathematical models made GPS possible. "
            "In 1956 she was hired at the Naval Surface Warfare Center in "
            "Dahlgren, Virginia, where she was only the second Black woman "
            "ever employed and one of only four Black employees total. "
            "Over her 42-year career she collected satellite data, calculated "
            "orbital trajectories, and — most critically — programmed an IBM "
            "computer to generate an extraordinarily precise mathematical model "
            "of the shape of the Earth, accounting for variations in gravity, "
            "tidal forces, and other distortions. That model became the "
            "geodetic foundation of the Global Positioning System. "
            "Every GPS device on Earth — every phone, every car, every aircraft, "
            "every military system — works because of Gladys West's math. "
            "When she retired, the world did not know her name. Her own children "
            "did not know the full scope of what she had done. Her contribution "
            "was rediscovered only when a member of her Alpha Kappa Alpha "
            "sorority chapter read a short biography she had submitted for an "
            "alumni function — and recognized what one line of it meant. "
            "She was finally inducted into the Air Force Space and Missile "
            "Pioneers Hall of Fame in 2018, at age 87. "
            "She died on January 17, 2026, at age 95. "
            "She described herself as 'a little farm girl' from Virginia. "
            "GPS is used by more than four billion people worldwide every day. "
            "Sources: NPR; AfroTech; Black History Month UK; Because of Them "
            "We Can; US Navy."
        ),
        "city":           "Dahlgren",
        "state":          "VA",
        "lat":            38.3340,
        "lng":            -77.0291,
        "source_url":     "https://www.npr.org/2026/01/23/nx-s1-5685027/gladys-west-gps-mathematician",
        "source_name":    "NPR / US Navy",
        "additional_sources": [
            {"url": "https://afrotech.com/black-history-dr-gladys-west-gps-technology",
             "name": "AfroTech"},
        ],
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1956-01-01",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ADA LOVELACE — wrote the first computer algorithm, 1843
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_ada_lovelace_first_algorithm",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Augusta Ada King, Countess of Lovelace (1815–1852) — known as "
            "Ada Lovelace — wrote the world's first computer algorithm in 1843, "
            "a full century before the first electronic computer was built. "
            "The daughter of poet Lord Byron, she was a mathematician who "
            "collaborated with inventor Charles Babbage on his proposed "
            "'Analytical Engine' — a mechanical general-purpose computing "
            "machine that was never built in his lifetime. "
            "When asked to translate an Italian article about the Analytical "
            "Engine from French, she added her own notes — which ended up "
            "three times longer than the original article. In those notes she "
            "described a method for the Engine to compute Bernoulli numbers: "
            "the first published algorithm ever designed for implementation "
            "on a computer. She also described concepts that would not be "
            "articulated again for over a century: that a computing machine "
            "could go beyond pure calculation to compose music, produce "
            "graphics, and perform any task that could be expressed in "
            "symbolic rules — essentially describing the modern computer. "
            "Babbage received credit for the vision of computing for most of "
            "history. Lovelace's role was marginalized or dismissed — with "
            "some male historians arguing well into the 20th century that "
            "her contributions were minimal and that Babbage had written the "
            "algorithm himself. This claim has been definitively disproven by "
            "historians of science. "
            "She died at age 36 of uterine cancer. "
            "The US Department of Defense named its Ada programming language "
            "after her in 1980. Ada Lovelace Day is celebrated annually on "
            "the second Tuesday of October. "
            "Sources: Britannica; Computer History Museum; National Women's "
            "History Museum."
        ),
        "city":           "London",
        "state":          "DC",
        "lat":            51.5074,
        "lng":            -0.1278,
        "source_url":     "https://www.womenshistory.org/education-resources/biographies/ada-lovelace",
        "source_name":    "National Women's History Museum / Computer History Museum",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1843-01-01",
        "tab":            "erasure",
        "country":        "United Kingdom",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # CHIEN-SHIUNG WU — proved parity violation, Nobel given to male theorists
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_chien_shiung_wu_parity_nobel",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Chien-Shiung Wu (1912–1997) was a Chinese-American experimental "
            "physicist at Columbia University, known as 'the First Lady of "
            "Physics' and 'the Chinese Marie Curie,' who in late 1956 designed "
            "and conducted one of the most important experiments in the history "
            "of physics — and was not given the Nobel Prize for it. "
            "In 1956, theoretical physicists Tsung-Dao Lee and Chen-Ning Yang "
            "proposed that the law of conservation of parity — a bedrock "
            "assumption of physics holding that physical systems behave "
            "symmetrically — might be violated in weak nuclear interactions. "
            "Most physicists, including Wolfgang Pauli, thought this was "
            "impossible. Lee and Yang sought Wu specifically because she was "
            "the world's foremost expert in beta decay. She cancelled a planned "
            "trip to Geneva and the Far East to pursue the experiment. "
            "Working at the National Bureau of Standards over the 1956–57 "
            "holiday season, Wu and her team cooled cobalt-60 nuclei to nearly "
            "absolute zero and observed their beta decay. The electrons were "
            "not emitted symmetrically — parity was violated. A law of physics "
            "that had been assumed universal for 30 years was overturned. "
            "The experiment was immediately reproduced in laboratories worldwide. "
            "It became known universally as 'the Wu Experiment.' "
            "In October 1957 — less than a year after Wu's experimental "
            "confirmation — Lee and Yang were awarded the Nobel Prize in Physics. "
            "Wu was not included. Nobel rules allow up to three recipients; "
            "the committee chose two. Lee and Yang acknowledged in their Nobel "
            "acceptance speeches that Wu's experimental work was indispensable. "
            "Wu was awarded the first Wolf Prize in Physics in 1978 — 21 years "
            "later. She was nominated for the Nobel Prize multiple additional "
            "times and never received it. She died in 1997. "
            "Sources: National Geographic; Grokipedia; JSTOR Daily; Gizmodo."
        ),
        "city":           "New York",
        "state":          "NY",
        "lat":            40.8075,
        "lng":            -73.9626,
        "source_url":     "https://www.nationalgeographic.com/premium/article/chien-shiung-wu-chinese-american-woman-physics-manhattan-project",
        "source_name":    "National Geographic / Columbia University",
        "additional_sources": [
            {"url": "https://grokipedia.com/page/Wu_experiment",
             "name": "Grokipedia — Wu Experiment"},
            {"url": "https://daily.jstor.org/chien-shiung-wu-the-first-lady-of-physics",
             "name": "JSTOR Daily"},
        ],
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1956-12-27",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # VERA RUBIN — discovered dark matter, never received Nobel
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_vera_rubin_dark_matter_nobel",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Vera Florence Rubin (1928–2016) was an American astronomer who "
            "in the 1970s, working with colleague W. Kent Ford, provided the "
            "first definitive observational evidence for dark matter — the "
            "invisible mass that makes up approximately 27% of the universe "
            "and without which galaxies could not hold together. "
            "By measuring the rotation curves of galaxies, Rubin found that "
            "stars at the outer edges of galaxies were rotating just as fast "
            "as those near the center — which was impossible unless there was "
            "far more mass in the galaxy than could be seen. The only "
            "explanation was that galaxies are embedded in vast halos of "
            "invisible matter. This was one of the most consequential "
            "discoveries in 20th century astronomy, reshaping our understanding "
            "of the structure and composition of the universe. "
            "Rubin was widely considered the leading candidate for the Nobel "
            "Prize in Physics for decades. She was nominated repeatedly. "
            "She died on December 25, 2016, at age 88, without receiving it. "
            "The Nobel Prize is not awarded posthumously. "
            "She had faced institutional barriers throughout her career: "
            "Princeton's graduate astronomy program did not accept women "
            "when she applied; she was initially denied access to Palomar "
            "Observatory's facilities because she was a woman. "
            "In 2020 the Vera C. Rubin Observatory in Chile — the most powerful "
            "survey telescope ever built — was named in her honor. "
            "Sources: Britannica; National Geographic; NASA."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://www.britannica.com/biography/Vera-Rubin",
        "source_name":    "Britannica / NASA",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1970-01-01",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # CAMILLE CLAUDEL — sculptor institutionalized, work stolen by Rodin
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_camille_claudel_sculptor_asylum",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Camille Claudel (1864–1943) was a French sculptor whose work "
            "critics described as equal to — and in some respects superior to "
            "— that of Auguste Rodin, her teacher, collaborator, and lover. "
            "Rodin is remembered as perhaps the greatest sculptor since "
            "Michelangelo. Claudel spent the last 30 years of her life in "
            "an asylum. "
            "Claudel began sculpting as a teenager and showed extraordinary "
            "talent recognized by other artists immediately. She became "
            "Rodin's student, then his collaborator, then his lover. She "
            "modeled hands and feet for his Burghers of Calais and posed for "
            "figures in his Gates of Hell. Evidence suggests Rodin exhibited "
            "and sold works that incorporated or directly used her ideas "
            "and techniques. When scholars have examined their work side by "
            "side, many of Rodin's most celebrated pieces closely mirror "
            "Claudel's innovations. "
            "After their relationship ended, Claudel worked in poverty and "
            "increasing isolation, convinced Rodin was stealing from her — "
            "a conviction her family and the art world used to pathologize "
            "her. She began destroying her own work, fearing he would take it. "
            "On March 10, 1913 — eight days after her beloved father died — "
            "her brother Paul Claudel had her involuntarily committed to a "
            "psychiatric hospital. She was diagnosed with 'systematized "
            "delusion of persecution.' Artists who knew her publicly "
            "criticized the commitment as the destruction of a genius. "
            "Rodin, who had said he would intercede on her behalf, did not. "
            "Claudel spent 30 years in the asylum, refused to sculpt, received "
            "almost no visitors, and was denied letters from most people. "
            "She died alone in 1943 at age 78 and was buried in the "
            "institution's mass grave. Her family never claimed her body. "
            "A museum dedicated to her work opened in Nogent-sur-Seine in 2017 "
            "— 74 years after her death. "
            "Sources: Britannica; The Art Story; Hyperallergic; Getty Museum; "
            "National Museum of Women in the Arts."
        ),
        "city":           "Paris",
        "state":          "DC",
        "lat":            48.8566,
        "lng":            2.3522,
        "source_url":     "https://www.britannica.com/biography/Camille-Claudel",
        "source_name":    "Britannica / The Art Story / Getty Museum",
        "additional_sources": [
            {"url": "https://hyperallergic.com/did-auguste-rodin-steal-from-camille-claudel/",
             "name": "Hyperallergic — Did Rodin Steal from Claudel?"},
            {"url": "https://nmwa.org/art/artists/camille-claudel/",
             "name": "National Museum of Women in the Arts"},
        ],
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1913-03-10",
        "tab":            "erasure",
        "country":        "France",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # JUDITH LEYSTER — Dutch master painter relabeled as Frans Hals
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_judith_leyster_paintings_relabeled",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Judith Leyster (1609–1660) was a Dutch Golden Age painter — "
            "one of only two women admitted to the Haarlem Guild of Saint "
            "Luke in the 17th century, and the first woman ever admitted to "
            "that guild. She was a master painter whose work in portraiture "
            "and genre scenes was celebrated in her lifetime. "
            "After her death, her name was systematically erased from her "
            "own paintings. Art dealers and collectors in the 18th and 19th "
            "centuries relabeled dozens of her works as paintings by Frans "
            "Hals — her male contemporary — because a Frans Hals commanded "
            "vastly higher prices. Her signature, a distinctive monogram of "
            "J and L with a star, was painted over or ignored. "
            "Her existence as an artist was almost entirely forgotten for "
            "over two centuries. "
            "She was rediscovered in 1893 when a Dutch art historian examining "
            "a painting attributed to Hals found Leyster's hidden signature "
            "beneath overpaint. The painting's owner — the Louvre — "
            "was informed. The attribution was corrected. "
            "The financial motivation was explicit and documented: her work "
            "was worth more labeled as a man's. Her erasure was profitable. "
            "Sources: Jungle Red Writers; National Museum of Women in the Arts; "
            "Rijksmuseum Amsterdam."
        ),
        "city":           "Haarlem",
        "state":          "DC",
        "lat":            52.3873,
        "lng":            4.6462,
        "source_url":     "https://nmwa.org/art/artists/judith-leyster/",
        "source_name":    "National Museum of Women in the Arts / Rijksmuseum",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1660-01-01",
        "tab":            "erasure",
        "country":        "Netherlands",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # AGENT 355 — unnamed female spy, American Revolution
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_agent_355_american_revolution",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Agent 355 was the code name of an unknown female spy who operated "
            "as part of the Culper Spy Ring — the most important intelligence "
            "network of the American Revolutionary War — in New York City "
            "during British occupation, approximately 1778–1780. "
            "In the Culper Ring's numeric code, '355' meant 'lady.' "
            "She moved in the highest circles of British-occupied New York "
            "society, gathering intelligence from British officers at social "
            "events and passing it to the network. Her intelligence was "
            "credited by ring leader Benjamin Tallmadge as instrumental in "
            "exposing British Major John André and unmasking the treason of "
            "Benedict Arnold — one of the most significant intelligence "
            "coups of the entire war. "
            "Her real identity has never been confirmed. Historians have "
            "proposed several candidates but no definitive identification "
            "has been made. She may have been captured by the British and "
            "died in captivity. "
            "She has no monument. No poem. No national holiday. "
            "Paul Revere — who rode 20 miles on a horse to warn two men — "
            "has a famous poem, a national landmark, and appears in every "
            "American history textbook. Agent 355 — who infiltrated British "
            "high command and helped prevent the loss of the war — "
            "does not have a confirmed name. "
            "Sources: CIA Historical Review; Smithsonian; George Washington's "
            "Mount Vernon archives."
        ),
        "city":           "New York",
        "state":          "NY",
        "lat":            40.7128,
        "lng":            -74.0060,
        "source_url":     "https://www.mountvernon.org/library/digitalhistory/digital-encyclopedia/article/culper-spy-ring/",
        "source_name":    "George Washington's Mount Vernon / CIA Historical Review",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1778-01-01",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SYBIL LUDINGTON — rode twice as far as Paul Revere, got no poem
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_sybil_ludington_midnight_ride",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "On the night of April 26, 1777 — two years after Paul Revere's "
            "famous ride — Sybil Ludington, 16 years old, rode approximately "
            "40 miles through Putnam County, New York, in the dark and rain, "
            "to muster her father's militia regiment after the British burned "
            "Danbury, Connecticut. "
            "Paul Revere rode approximately 20 miles. He was stopped by "
            "British troops before completing his route, warned two men, "
            "and was captured. He has a famous poem by Henry Wadsworth "
            "Longfellow, a national historic site, a US postage stamp, and "
            "a prominent place in every American history curriculum. "
            "Sybil Ludington rode twice as far, alone, at night, through "
            "unfamiliar terrain, at age 16, completing her route. She "
            "successfully mustered approximately 400 militia. General George "
            "Washington personally thanked her for her service. "
            "She has a small statue in Carmel, New York. She does not appear "
            "in most American history textbooks. No famous poem was written "
            "about her ride for almost 200 years — until 1940, when a local "
            "poet wrote one that remained largely unknown. "
            "Her erasure is not accidental. The story America chose to tell "
            "about its founding featured men. "
            "Sources: Smithsonian; Mental Floss; Connecticut Historical Society."
        ),
        "city":           "Carmel",
        "state":          "NY",
        "lat":            41.4351,
        "lng":            -73.6832,
        "source_url":     "https://www.smithsonianmag.com/smart-news/the-true-story-of-sybil-ludington-the-female-paul-revere-180971287/",
        "source_name":    "Smithsonian Magazine",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1777-04-26",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SISTER ROSETTA THARPE — invented rock and roll guitar, credited to men
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_sister_rosetta_tharpe_rock_guitar",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Sister Rosetta Tharpe (1915–1973) was a Black American gospel "
            "singer and guitarist who invented the electric guitar technique "
            "that became the foundation of rock and roll — a decade before "
            "rock and roll was named. "
            "Playing a Gibson SG with distortion and aggressive picking in "
            "the 1940s, Tharpe developed the sound and style — loud, driving, "
            "rhythmically powerful electric guitar — that Little Richard, "
            "Elvis Presley, Chuck Berry, Jerry Lee Lewis, Johnny Cash, and "
            "Keith Richards all directly learned from or cited as their "
            "primary influence. "
            "She was the first major gospel artist to perform at the Apollo "
            "Theatre and Carnegie Hall. She sold millions of records in the "
            "1940s. Elvis Presley cited her as a major influence. Keith "
            "Richards of the Rolling Stones has described seeing a film of "
            "her play as a revelation. "
            "Rock and roll history canonized Chuck Berry, Elvis, and Little "
            "Richard as the founders of the genre. Tharpe — a Black woman "
            "whose music preceded and directly influenced all of them — "
            "was categorized as a 'gospel singer' and excluded from the "
            "founding narrative. "
            "She was not inducted into the Rock and Roll Hall of Fame until "
            "2018 — 45 years after her death and 70+ years after she invented "
            "the guitar style that defines the genre. "
            "Sources: Rolling Stone; NPR; Rock and Roll Hall of Fame."
        ),
        "city":           "Cotton Plant",
        "state":          "AR",
        "lat":            35.0668,
        "lng":            -91.0337,
        "source_url":     "https://www.rockhall.com/inductees/sister-rosetta-tharpe",
        "source_name":    "Rock and Roll Hall of Fame / NPR / Rolling Stone",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1940-01-01",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ABIGAIL ADAMS — "Remember the Ladies." He laughed.
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_abigail_adams_remember_the_ladies",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "On March 31, 1776 — while John Adams was in Philadelphia helping "
            "draft the founding documents of the United States — his wife "
            "Abigail Adams wrote him a letter that contained one of the most "
            "famous and most ignored requests in American history: "
            "'Remember the Ladies, and be more generous and favorable to "
            "them than your ancestors. Do not put such unlimited power into "
            "the hands of the Husbands. Remember all Men would be tyrants "
            "if they could. If particular care and attention is not paid to "
            "the Ladies we are determined to foment a Rebellion, and will "
            "not hold ourselves bound by any Laws in which we have no voice, "
            "or Representation.' "
            "John Adams replied on April 14, 1776: 'As to your extraordinary "
            "Code of Laws, I cannot but laugh.' He told her that men knew "
            "better than to repeal their masculine systems. He was joking. "
            "He did not remember the ladies. "
            "The Declaration of Independence — 'all men are created equal' "
            "— was signed four months later. Women were not included. "
            "Women could not vote for another 144 years. "
            "Abigail Adams was one of the most politically sophisticated "
            "people in the founding generation. Her letters reveal a sharper "
            "political mind than many of the men celebrated as Founders. "
            "She has been remembered primarily as John Adams's wife. "
            "Sources: Massachusetts Historical Society — Adams Family Papers; "
            "Smithsonian; National Women's History Museum."
        ),
        "city":           "Braintree",
        "state":          "MA",
        "lat":            42.2182,
        "lng":            -71.0023,
        "source_url":     "https://www.masshist.org/digitaladams/archive/letter/",
        "source_name":    "Massachusetts Historical Society — Adams Family Papers",
        "additional_sources": [
            {"url": "https://www.womenshistory.org/education-resources/biographies/abigail-adams",
             "name": "National Women's History Museum"},
        ],
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1776-03-31",
        "tab":            "erasure",
    },

]


def main():
    print("\n  [Medusa] Seeding erasure expanded records...\n")
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
