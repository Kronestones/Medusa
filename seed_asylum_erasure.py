"""
seed_asylum_erasure.py — Medusa

Women institutionalized by men — the legal, medical, and psychiatric
systems used to imprison women who were inconvenient, independent,
or simply in the way.

Records:
  - Nellie Bly — Ten Days in a Mad-House (1887), Blackwell's Island
  - Elizabeth Packard — committed by husband for disagreeing with him,
    fought back and changed the law (1860–1870s)
  - Husband's Certificate Laws — legal overview, how men committed wives
  - Reasons women were committed — documented admission records
  - The Erasure of Women from Asylum Administration — men took over

All flagged tab='erasure' — this belongs in the Erasure tab as the
institutional mechanism of manufactured dependency and silencing.

Run:
    cd ~/medusa && python3 seed_asylum_erasure.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [

    # ══════════════════════════════════════════════════════════════════════════
    # NELLIE BLY — Ten Days in a Mad-House, Blackwell's Island, 1887
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_nellie_bly_ten_days_mad_house_1887",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "In September 1887, Elizabeth Jane Cochrane — 23 years old, "
            "writing under the pen name Nellie Bly — had herself voluntarily "
            "committed to the Women's Lunatic Asylum on Blackwell's Island "
            "in New York City, on assignment for Joseph Pulitzer's New York "
            "World. For ten days she lived as a patient inside the asylum "
            "to document conditions that public officials had been dismissing "
            "for years. What she found was a human warehouse for women who "
            "were inconvenient, poor, foreign, or simply female. "
            "To gain admission, Bly checked into a boarding house for working "
            "women, acted strangely, refused to sleep, and was summoned before "
            "a judge within days. She was committed with what she described as "
            "disconcerting speed. Once inside, she stopped pretending to be "
            "unwell and behaved entirely normally — and found that the more "
            "sanely she behaved, the crazier the staff believed her to be. "
            "She wrote: 'From the moment I entered the insane ward on the "
            "Island, I made no attempt to keep up the assumed role of insanity. "
            "I talked and acted just as I do in ordinary life. Yet strange to "
            "say, the more sanely I talked and acted, the crazier I was thought "
            "to be.' "
            "The conditions she documented: women were awakened at 5:30 a.m. "
            "and forced to sit on hard wooden benches in a freezing room in "
            "complete silence until 8 p.m. They were given spoiled, rotten, "
            "and moldy food. They were stripped and thrown into baths of "
            "ice-cold, filthy water — multiple buckets poured over their heads "
            "simultaneously. Towels were shared and unwashed. Women were beaten "
            "by nurses when they cried out. Patients were tied with ropes. "
            "She interviewed women who had been committed for poverty, physical "
            "exhaustion from overwork, and inability to speak English. "
            "One woman had been committed by her husband because he wanted her "
            "gone. Several women, Bly concluded, showed no evidence of mental "
            "illness whatsoever. 'The insane asylum on Blackwell's Island,' "
            "she wrote, 'is a human rat-trap. It is easy to get in, but once "
            "there it is impossible to get out.' "
            "The asylum held 1,600 women in a facility built for 1,000. "
            "Her ten-part series, published in the New York World and collected "
            "into the book Ten Days in a Mad-House (1887), triggered a grand "
            "jury investigation. The city of New York immediately allocated "
            "an additional $1 million to the Department of Public Charities "
            "and Corrections to improve conditions. Staff were dismissed. "
            "New oversight procedures were implemented. "
            "Nellie Bly is remembered primarily as a 'stunt journalist' — "
            "a diminishing label applied almost exclusively to women reporters "
            "doing dangerous undercover work that their male colleagues would "
            "not or could not do. Her reporting directly changed the law and "
            "saved lives. She is not in most American history textbooks. "
            "Sources: Skeptical Inquirer; Biography.com; NY Historical Society; "
            "Project Gutenberg — Ten Days in a Mad-House (full text); "
            "The Quack Doctor."
        ),
        "city":           "New York",
        "state":          "NY",
        "lat":            40.7614,
        "lng":            -73.9512,
        "source_url":     "https://www.gutenberg.org/ebooks/59899",
        "source_name":    "Ten Days in a Mad-House — Nellie Bly (1887, Project Gutenberg)",
        "additional_sources": [
            {"url": "https://skepticalinquirer.org/2022/12/undercover-in-a-madhouse-the-extraordinary-story-of-nellie-bly/",
             "name": "Skeptical Inquirer"},
            {"url": "https://www.nyhistory.org/blogs/nellie-blys-ten-days-in-a-mad-house-and-the-rise-of-girl-stunt-reporting",
             "name": "New York Historical Society"},
            {"url": "https://www.biography.com/authors-writers/inside-nelly-bly-10-days-madhouse",
             "name": "Biography.com"},
        ],
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1887-09-22",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ELIZABETH PACKARD — committed by husband for disagreeing with him, 1860
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_elizabeth_packard_illinois_asylum_1860",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "On June 18, 1860, Elizabeth Parsons Ware Packard — 44 years old, "
            "a mother of six children — was forcibly removed from her home in "
            "Manteno, Illinois, by her husband Theophilus Packard, a strict "
            "Calvinist minister, and committed to the Illinois State Hospital "
            "for the Insane in Jacksonville. She had not been examined by a "
            "doctor. No evidence of mental illness was presented. "
            "Under Illinois law at the time, a husband could have his wife "
            "committed to an insane asylum without any proof of insanity — "
            "no medical examination, no judicial review, no hearing. "
            "A married woman had virtually no legal standing to contest it. "
            "Her crime: she had begun attending a different church, held her "
            "own religious views that differed from her husband's Calvinist "
            "doctrine, spoke her mind at Sunday school, and insisted she had "
            "the right to her own thoughts and biblical interpretations. "
            "Theophilus found her independence intolerable. He had her "
            "institutionalized. "
            "Elizabeth was held for three years. While inside she documented "
            "everything — keeping secret journals, writing letters, observing "
            "and recording the conditions. She was eventually released only "
            "because her attending physician concluded she was sane. "
            "Theophilus then locked her in her own bedroom and prepared to "
            "have her recommitted. "
            "She escaped when neighbors helped her get a writ of habeas corpus. "
            "In January 1864 — a jury trial convened in her living room — "
            "she was found sane in seven minutes. "
            "She then spent the next decade campaigning across the United "
            "States for legislative reform. She wrote and self-published "
            "multiple books documenting her experience. She lobbied state "
            "legislatures personally — coast to coast. She drafted model "
            "commitment reform bills herself. "
            "'A bill drawn by a woman,' contemporaries noted with surprise. "
            "She successfully passed commitment reform laws requiring personal "
            "hearings before commitment in Illinois, Iowa, Maine, Massachusetts, "
            "Connecticut, and multiple other states. She also passed laws "
            "giving married women greater rights in child custody, property, "
            "and earnings. "
            "She was opposed at every turn by the psychiatric profession, "
            "which viewed her as a threat to medical authority. She won anyway. "
            "Elizabeth Packard is almost entirely absent from American history "
            "textbooks. The husband who imprisoned her for holding her own "
            "religious opinions is not remembered at all. "
            "Sources: Indiana State Library; Johns Hopkins University Press — "
            "Mrs. Packard on the Asylum (Elizabeth Packard biography); "
            "University of Wisconsin Oshkosh research."
        ),
        "city":           "Manteno",
        "state":          "IL",
        "lat":            41.2514,
        "lng":            -87.8320,
        "source_url":     "https://blog.library.in.gov/a-bill-drawn-by-a-woman-mrs-packard-and-rights-for-the-insane/",
        "source_name":    "Indiana State Library / Johns Hopkins University Press",
        "additional_sources": [
            {"url": "https://muse.jhu.edu/book/18439",
             "name": "Johns Hopkins University Press — Mrs. Packard on the Asylum"},
        ],
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1860-06-18",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # HUSBAND'S CERTIFICATE LAWS — legal overview
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_husbands_certificate_commitment_laws",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Throughout the 19th century in the United States and Britain, "
            "the law gave husbands extraordinary — and largely unchecked — "
            "power to have their wives institutionalized in insane asylums. "
            "In Illinois until the 1860s, no medical examination or judicial "
            "review was required. A husband's word was sufficient. "
            "In England under the Lunacy Acts, a married woman could be "
            "committed on the petition of her husband accompanied by two "
            "medical certificates — certificates that, as legal historians "
            "have documented, were granted with alarming ease and minimal "
            "investigation. The woman herself had no right to contest the "
            "commitment, no right to call witnesses, and no access to "
            "legal counsel. Once inside, her property reverted entirely "
            "to her husband under coverture law. She could not sign contracts, "
            "could not access her own money, could not leave. "
            "The reasons women were committed — drawn from actual 19th century "
            "asylum admission records documented by University of Wisconsin "
            "researchers — included: 'religious excitement'; 'suppressed "
            "menstruation'; 'domestic trouble'; 'reading too many novels'; "
            "'masturbation'; 'grief'; 'desertion by husband'; 'over-action "
            "of the mind'; 'political excitement'; 'epilepsy'; 'imaginary "
            "female trouble'; and 'moral insanity' — a diagnosis applied "
            "almost exclusively to women who violated social norms. "
            "Women who had been raped were sometimes committed for 'moral "
            "corruption.' Women who refused to submit to their husbands "
            "were committed for 'domestic trouble.' Women who expressed "
            "strong opinions were committed for 'over-action of the mind.' "
            "The asylum system did not exist to treat illness. It existed "
            "to remove inconvenient women from society and place their "
            "persons and property under male control — either a husband's "
            "or the state's. "
            "As legal historian Carol Smart has documented, by the mid-19th "
            "century the male medical profession had completely taken over "
            "asylum administration from women — who had previously run them "
            "as cottage industries — further concentrating power over "
            "institutionalized women in male hands. "
            "Elizabeth Packard's legal campaigns in the 1860s and 1870s "
            "began dismantling these laws state by state. The process took "
            "over a century. "
            "Sources: University of Wisconsin Oshkosh — Lunacy in the 19th "
            "Century; University of New Brunswick Law Journal — Property, "
            "Lunacy and Divorce Laws; NIH Historical Medical Records."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://minds.wisc.edu/items/b4dd3aef-c6b3-4315-a855-0ef762916cf5",
        "source_name":    "University of Wisconsin Oshkosh — Lunacy in the 19th Century",
        "additional_sources": [
            {"url": "https://journals.lib.unb.ca/index.php/unblj/article/download/29152/1882524333/1882523887",
             "name": "University of New Brunswick Law Journal — Property, Lunacy and Divorce Laws"},
            {"url": "https://www.ncbi.nlm.ca/pmc/articles/PMC5090733/",
             "name": "NIH — Medical Certificates in Lunacy (1863)"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1850-01-01",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # WOMEN ERASED FROM ASYLUM ADMINISTRATION — men took over in 19th century
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_women_removed_asylum_administration",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "For centuries, women had administered asylums and cared for the "
            "mentally ill as a natural extension of domestic caretaking — "
            "running facilities as what legal historians have called 'a sort "
            "of cottage industry.' Matrons ran madhouses. Women were the "
            "primary caregivers. They held institutional authority. "
            "In the 19th century, as the male medical profession professionalized "
            "and consolidated power, men systematically displaced women from "
            "these roles. Between 1854 and 1870, female administrators were "
            "removed from leadership positions in asylums across England and "
            "the United States. Male physicians and superintendents took control. "
            "The stated justification was that medical expertise — held "
            "exclusively by men, who controlled all medical licensing — was "
            "required to run an asylum properly. "
            "The result: by the mid-19th century, women had been removed from "
            "almost every capacity in the asylum except that of patient. "
            "They went from running institutions to being imprisoned in them. "
            "This transition is directly parallel to the elimination of female "
            "healers and midwives from medicine in the 14th–17th centuries: "
            "in both cases, men used institutional credentialing — which they "
            "controlled exclusively — to remove women from roles they had "
            "held for generations, and then used those same institutions "
            "to confine and control women who resisted male authority. "
            "The asylum became, in the words of Nellie Bly, 'a human rat-trap' "
            "— easy to enter, impossible to leave — administered entirely by "
            "the men who had the most to gain from women's silence. "
            "Sources: University of New Brunswick Law Journal — Property, "
            "Lunacy and Divorce Laws; Carol Smart, Women, Crime and Criminology "
            "(1976); Elaine Showalter, The Female Malady (1985)."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://journals.lib.unb.ca/index.php/unblj/article/download/29152/1882524333/1882523887",
        "source_name":    "University of New Brunswick Law Journal / Elaine Showalter — The Female Malady",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1854-01-01",
        "tab":            "erasure",
    },

]


def main():
    print("\n  [Medusa] Seeding asylum erasure records...\n")
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
