"""
seed_erasure.py — Medusa

The Erasure Tab — Women deliberately removed from history, science,
medicine, and power by coordinated institutional action.

Central argument: Men and their laws, religions, and institutions have
never been protectors and providers. They have used power to limit
women's access to resources, knowledge, income, and autonomy —
making women dependent on men by design, not by nature.

Sections:
  1. The Witch Trials as Medical Campaign (14th–17th century)
  2. Jacoba Felicie — prosecuted for healing
  3. The Malleus Maleficarum — the manual
  4. The Matilda Effect — named pattern of scientific erasure
  5. Rosalind Franklin — DNA stolen
  6. Nettie Stevens — sex chromosomes stolen
  7. Alice Ball — leprosy cure stolen
  8. Cecilia Payne-Gaposchkin — stellar composition stolen
  9. Eunice Newton Foote — climate science stolen
  10. Jocelyn Bell Burnell — pulsars stolen
  11. Lise Meitner — nuclear fission stolen
  12. Hedy Lamarr — WiFi/Bluetooth foundation stolen
  13. Katherine Johnson / Hidden Figures — NASA erased
  14. Margaret Knight — patent stolen by man who said she couldn't
      understand her own machine
  15. Hypatia of Alexandria — murdered by Christian mob
  16. The Coverture Laws — legal erasure of married women
  17. Women banned from universities — timeline

Run:
    cd ~/medusa && python3 seed_erasure.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [

    # ══════════════════════════════════════════════════════════════════════════
    # THE WITCH TRIALS AS MEDICAL CAMPAIGN — Systemic overview
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_witch_trials_medical_campaign_overview",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "Between the 14th and 17th centuries, the Catholic and Protestant "
            "churches, the newly forming male medical profession, and the state "
            "ran a coordinated four-century campaign that: "
            "(1) declared healing without a license a crime punishable by death, "
            "(2) made it illegal for women to obtain a license, and "
            "(3) used the witch trial as the legal mechanism to eliminate female "
            "healers, midwives, and herbalists — transferring their knowledge, "
            "income, and social authority to university-trained male physicians. "
            "Women had been the primary healers of Europe for centuries — "
            "serving peasant communities, attending births, treating illness "
            "with plant medicine, and passing knowledge through generations. "
            "They charged what people could afford. They were effective. "
            "The male medical establishment wanted their patients and their power. "
            "Since the Church controlled all medical schooling, it exclusively "
            "certified male physicians. By the 14th century English physicians "
            "had sent a petition to Parliament demanding fines and 'long "
            "imprisonment' for any woman who attempted to 'use the practyse "
            "of Fisyk.' By the late 1500s, women were accused of witchcraft "
            "specifically for successfully healing patients — because success "
            "without a male license was evidence of diabolical assistance. "
            "The male physician served as the 'expert witness' at witch trials, "
            "lending scientific authority to the proceedings. The trial in one "
            "stroke placed the male doctor on the side of God, Law, and reason — "
            "and placed the female healer on the side of darkness and magic. "
            "He owed his new status not to medical or scientific achievements "
            "of his own, but to the Church and State he served. "
            "Estimates of those killed range widely, but the latest scholarship "
            "puts the number at approximately 100,000 people executed as witches "
            "across Europe, 80–85% of them women. In some villages, all but one "
            "woman had been killed by the mid-16th century. "
            "This was not superstition. It was a professional and legal campaign "
            "to eliminate female economic and medical power. "
            "The women's health movement of the 20th century has direct roots "
            "in the knowledge these women carried. "
            "Source: Barbara Ehrenreich and Deirdre English, Witches, Midwives "
            "and Nurses: A History of Women Healers (Feminist Press, 1972/2010); "
            "Salon; IMSS Medical History Collections."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://www.marxists.org/subject/women/authors/ehrenreich-barbara/witches.htm",
        "source_name":    "Ehrenreich & English — Witches, Midwives and Nurses (1972)",
        "additional_sources": [
            {"url": "https://www.salon.com/2013/10/31/what_witches_have_to_do_with_womens_health/",
             "name": "Salon — What Witches Have to Do With Women's Health"},
            {"url": "https://imss.org/2019/12/a-note-from-the-collections-midwives-and-healers-in-the-european-witch-trials/",
             "name": "IMSS Medical History Collections"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1322-01-01",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # JACOBA FELICIE — prosecuted by Faculty of Medicine, Paris, 1322
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_jacoba_felicie_paris_1322",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Jacoba Felicie was brought to trial in Paris in 1322 by the "
            "Faculty of Medicine at the University of Paris for practicing "
            "medicine without a license. She was an educated woman who had "
            "been treating patients — including patients whom university-trained "
            "male physicians had failed to cure. Witnesses testified on her "
            "behalf that she had healed them when male doctors could not. "
            "The Faculty of Medicine prosecuted her anyway. "
            "Her case established a critical precedent: the male physician's "
            "authority was not based on outcomes or skill, but on institutional "
            "certification from which women were categorically excluded. "
            "A woman could heal better than a man and still be prosecuted for "
            "healing. The trial placed the male physician on a moral and "
            "intellectual plane above the female healer — not through superior "
            "results, but through the power of the Church and the State to "
            "define who was legitimate. Jacoba Felicie was convicted and fined. "
            "Her case is documented in Barbara Ehrenreich and Deirdre English's "
            "Witches, Midwives and Nurses (1972) and in multiple medical "
            "history sources. "
            "Source: Ehrenreich & English, Witches, Midwives and Nurses; "
            "University of Paris Faculty of Medicine records, 1322."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            48.8566,
        "lng":            2.3522,
        "source_url":     "https://www.marxists.org/subject/women/authors/ehrenreich-barbara/witches.htm",
        "source_name":    "Ehrenreich & English — Witches, Midwives and Nurses",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1322-01-01",
        "tab":            "erasure",
        "country":        "France",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MALLEUS MALEFICARUM — the manual for witch hunting, 1487
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_malleus_maleficarum_1487",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "The Malleus Maleficarum ('Hammer of Witches') was published in "
            "1487 by two Dominican Inquisitors, Heinrich Kramer and Jacob "
            "Sprenger, with the approval of Pope Innocent VIII. It became "
            "the definitive manual for identifying, prosecuting, and executing "
            "witches — and it was explicitly and obsessively focused on women. "
            "The text argued that women were inherently more susceptible to "
            "diabolical influence due to their weaker intellect and moral "
            "character, that female sexuality was inherently dangerous, and "
            "that midwives in particular were agents of the Devil — using "
            "their access to newborns and birthing women to commit harm. "
            "It provided detailed instructions for torture to extract "
            "confessions, identification of 'witch's marks,' and prosecution "
            "procedures. It went through at least 28 editions between 1487 "
            "and 1600 — one of the most widely printed books in Europe in the "
            "century after the Gutenberg press, second only to the Bible. "
            "The Malleus Maleficarum was not a fringe document. It was "
            "the official, institutionally endorsed, mass-produced manual "
            "for the systematic torture and murder of women. "
            "It specifically targeted the knowledge women held — healing, "
            "midwifery, herbalism — as evidence of diabolical power rather "
            "than skill. It was used by both Catholic and Protestant courts. "
            "Sources: Britannica; IMSS Medical History; multiple historical "
            "academic sources."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            47.5596,
        "lng":            7.5886,
        "source_url":     "https://imss.org/2019/12/a-note-from-the-collections-midwives-and-healers-in-the-european-witch-trials/",
        "source_name":    "IMSS Medical History Collections / Britannica",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1487-01-01",
        "tab":            "erasure",
        "country":        "Germany / Europe",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # THE MATILDA EFFECT — named pattern of scientific erasure
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_matilda_effect_pattern",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "The Matilda Effect is the documented, systematic pattern in which "
            "women's scientific contributions are attributed to their male "
            "colleagues, collaborators, or supervisors — either during their "
            "lifetime or after their death. "
            "The term was coined by Cornell University science historian "
            "Margaret W. Rossiter in 1993, named for American suffragist and "
            "abolitionist Matilda Joslyn Gage, who first identified the pattern "
            "in her 1883 essay 'Woman as Inventor,' which documented women "
            "inventors whose work had been credited to men. "
            "The Matilda Effect is not a historical relic. It has been "
            "documented in 20th and 21st century science, medicine, and "
            "technology. Studies show that women's papers in science are "
            "cited less frequently than men's papers of equivalent quality; "
            "that women are less likely to be listed as first author even "
            "when they led the research; that grant panels rate identical "
            "proposals lower when the applicant's name is female; and that "
            "women's inventions are patented at lower rates not because "
            "they invent less, but because they face systemic barriers in "
            "the patent system. "
            "The effect compounds over time: less citation means less "
            "recognition means less funding means less opportunity — "
            "creating a structural cycle that removes women from the "
            "historical record of human knowledge. "
            "Sources: Cornell University Science History; National Geographic; "
            "Apollo Thirteen — The Matilda Effect (2025)."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://www.apollothirteen.com/article/the-matilda-effect-women-erased-from-science",
        "source_name":    "Apollo Thirteen / Cornell University Science History",
        "additional_sources": [
            {"url": "https://www.nationalgeographic.com/culture/article/130519-women-scientists-overlooked-dna-history-science",
             "name": "National Geographic — Women Scientists Overlooked"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1883-01-01",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ROSALIND FRANKLIN — Photo 51 stolen, DNA structure credited to Watson/Crick
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_rosalind_franklin_dna_photo51",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Rosalind Elsie Franklin (1920–1958) was a British chemist and "
            "X-ray crystallographer who in 1952 produced Photo 51 — the "
            "clearest X-ray diffraction image of DNA ever captured, providing "
            "definitive evidence for the double-helix structure of DNA. "
            "Without Franklin's knowledge or consent, her colleague Maurice "
            "Wilkins showed Photo 51 to James Watson. Watson and Francis Crick "
            "used her image — and data from her unpublished report, shared "
            "without her permission by a member of the Medical Research Council "
            "— to publish their landmark 1953 paper on the double-helix "
            "structure of DNA in Nature. They did not credit Franklin. "
            "Franklin published her own independent confirmation of the "
            "double-helix structure shortly after. "
            "In 1962 — four years after Franklin died of ovarian cancer at "
            "age 37 — Watson, Crick, and Wilkins were awarded the Nobel Prize "
            "in Physiology or Medicine for the discovery of the structure of "
            "DNA. Nobel Prizes are not awarded posthumously. Franklin received "
            "no Nobel, no credit, and died never knowing her data had been "
            "used without her consent. "
            "Watson later wrote in his memoir The Double Helix (1968) that he "
            "had been unimpressed by Franklin when he first met her, describing "
            "her appearance in detail and noting she did not wear lipstick. "
            "He has never fully acknowledged the extent to which Photo 51 "
            "was the foundation of his Nobel-winning work. "
            "Sources: National Geographic; Biography.com; Mental Floss; "
            "National Women's History Museum."
        ),
        "city":           "London",
        "state":          "DC",
        "lat":            51.5074,
        "lng":            -0.1278,
        "source_url":     "https://www.nationalgeographic.com/culture/article/130519-women-scientists-overlooked-dna-history-science",
        "source_name":    "National Geographic / National Women's History Museum",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1952-01-01",
        "tab":            "erasure",
        "country":        "United Kingdom",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # NETTIE STEVENS — discovered sex chromosomes, Nobel given to male colleague
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_nettie_stevens_sex_chromosomes",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Nettie Maria Stevens (1861–1912) was an American geneticist who "
            "in 1905 made one of the most fundamental discoveries in biology: "
            "that sex is determined by chromosomes. Working with mealworms at "
            "Bryn Mawr College, she observed that male organisms produced two "
            "types of sperm — one carrying a large X chromosome, one carrying "
            "a small Y chromosome — and determined that the Y chromosome "
            "determines male sex. She had discovered the XY sex determination "
            "system. "
            "Her male contemporary Edmund Beecher Wilson was working on similar "
            "research but reached the same conclusion later than Stevens. "
            "Because Stevens was female, she was discriminated against and "
            "Wilson received the credit. Her doctoral advisor Thomas Hunt Morgan "
            "also took partial credit for her work and went on to win the Nobel "
            "Prize in 1933 'for his discoveries concerning the role played by "
            "the chromosome in heredity' — despite not accepting the theory "
            "of chromosomal sex determination until decades after Stevens had "
            "proven it. Stevens was not invited to speak at conferences where "
            "Wilson and Morgan presented work built on her foundation. "
            "Stevens died of breast cancer in 1912 at age 50, without "
            "recognition for her discovery. Without her work, research on "
            "Turner Syndrome, Down Syndrome, and countless conditions linked "
            "to chromosomal inheritance would have been delayed by decades. "
            "Sources: National Women's History Museum; Biography.com; "
            "National Geographic."
        ),
        "city":           "Bryn Mawr",
        "state":          "PA",
        "lat":            40.0209,
        "lng":            -75.3097,
        "source_url":     "https://www.womenshistory.org/education-resources/biographies/nettie-stevens",
        "source_name":    "National Women's History Museum",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1905-01-01",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ALICE BALL — leprosy cure stolen after her death
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_alice_ball_leprosy_cure",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Alice Augusta Ball (1892–1916) was an African American chemist "
            "and the first woman and first Black person to graduate with a "
            "Master's degree from the University of Hawaii. At age 23, she "
            "developed the first effective treatment for leprosy (Hansen's "
            "disease) — a water-soluble injectable extract of chaulmoogra oil "
            "that could be absorbed by the body, ending the suffering caused "
            "by the ineffective oral administration then in use. "
            "Ball died at age 24, likely from chlorine gas exposure during a "
            "chemistry demonstration. After her death, Dr. Arthur L. Dean — "
            "president of the University of Hawaii — took her research, "
            "continued using her method without modification, published it "
            "under his own name, and called it the 'Dean Method.' "
            "He did not credit Ball. Her name disappeared from the medical "
            "record for decades. "
            "It was not until 1922 that a colleague, Dr. Harry T. Hollmann, "
            "published a paper explicitly crediting Ball with the discovery. "
            "Even then, recognition was slow. It was only through the work "
            "of community historians and retired researchers piecing together "
            "scattered departmental files that Ball's story was fully recovered "
            "in the late 20th century. The University of Hawaii eventually "
            "dedicated a plaque in her honor and named February 28 Alice Ball "
            "Day. She received no recognition during her lifetime for saving "
            "the lives of tens of thousands of leprosy patients. "
            "Sources: Apollo Thirteen; Biography.com; University of Hawaii."
        ),
        "city":           "Honolulu",
        "state":          "HI",
        "lat":            21.3069,
        "lng":            -157.8583,
        "source_url":     "https://www.apollothirteen.com/article/the-matilda-effect-women-erased-from-science",
        "source_name":    "Apollo Thirteen / University of Hawaii Archives",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1915-01-01",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # CECILIA PAYNE-GAPOSCHKIN — discovered stars are made of hydrogen/helium
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_cecilia_payne_stellar_composition",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Cecilia Payne-Gaposchkin (1900–1979) was a British-American "
            "astronomer who in 1925 wrote a doctoral dissertation at Radcliffe "
            "College — later described by astronomer Otto Struve as 'the most "
            "brilliant PhD thesis ever written in astronomy' — in which she "
            "discovered that stars are composed primarily of hydrogen and helium, "
            "not of heavy elements like Earth as most scientists then believed. "
            "Before she could publish, her dissertation was reviewed by "
            "Henry Norris Russell, director of the Princeton Observatory, "
            "who told her her conclusion was 'clearly impossible' and pressured "
            "her to add a note calling her own finding 'spurious.' She complied. "
            "Four years later, Russell independently reached the same conclusion "
            "through different means, published his findings, and received full "
            "credit for the discovery. He included a brief note acknowledging "
            "Payne's prior work, but the discovery was credited to him for "
            "decades. "
            "Payne spent her career at Harvard, where she was not allowed to "
            "be listed in the course catalog, was paid less than technical staff, "
            "and was not given a faculty appointment until 1956 — only after "
            "male colleagues of lesser accomplishment had been promoted around "
            "her. She eventually became the first woman to be appointed full "
            "professor at Harvard's Faculty of Arts and Sciences. "
            "Her discovery is now understood as one of the most important in "
            "the history of astrophysics. "
            "Sources: The Noosphere; HuffPost Women; Apollo Thirteen."
        ),
        "city":           "Cambridge",
        "state":          "MA",
        "lat":            42.3736,
        "lng":            -71.1097,
        "source_url":     "https://thenoosphere.substack.com/p/how-the-matilda-effect-explains-why",
        "source_name":    "The Noosphere / Harvard University History",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1925-01-01",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # EUNICE NEWTON FOOTE — discovered greenhouse effect 1856, erased
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_eunice_newton_foote_greenhouse_effect",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Eunice Newton Foote (1819–1888) was an American scientist and "
            "women's rights activist who in 1856 published experiments "
            "demonstrating that carbon dioxide traps heat — the foundational "
            "discovery of what we now call the greenhouse effect and the "
            "scientific basis for our understanding of climate change. "
            "She filled glass cylinders with different gases, exposed them "
            "to sunlight, and measured the temperature. Carbon dioxide heated "
            "the most and retained heat longest. She concluded that periods "
            "of high atmospheric CO2 would be associated with higher global "
            "temperatures. "
            "When her paper was presented at the American Association for the "
            "Advancement of Science in 1856, a male scientist read it on her "
            "behalf — women were not permitted to present their own papers. "
            "Contemporary accounts described her as a 'lady experimenter.' "
            "Three years later, Irish physicist John Tyndall published "
            "experiments on the same phenomenon and was credited as the "
            "founder of climate science — Foote's prior discovery was unknown "
            "to him, but also unknown to history for over 150 years. "
            "Foote was rediscovered only in 2011 by geologist Raymond Sorenson "
            "searching historical archives. Her name now appears in the "
            "prehistory of climate science rather than as a marginal curiosity. "
            "The woman who first identified the mechanism of climate change "
            "was erased from the history of climate science for 155 years. "
            "Sources: Apollo Thirteen — The Matilda Effect (2025); "
            "AAAS historical archives."
        ),
        "city":           "Seneca Falls",
        "state":          "NY",
        "lat":            42.9106,
        "lng":            -76.7997,
        "source_url":     "https://www.apollothirteen.com/article/the-matilda-effect-women-erased-from-science",
        "source_name":    "Apollo Thirteen / AAAS Archives",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1856-01-01",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # JOCELYN BELL BURNELL — discovered pulsars, Nobel given to male supervisor
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_jocelyn_bell_burnell_pulsars",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Dame Jocelyn Bell Burnell (born 1943) was a postgraduate student "
            "at Cambridge University in 1967 when she discovered the first "
            "radio pulsars — rapidly rotating neutron stars that emit regular "
            "pulses of radio waves, one of the most significant astronomical "
            "discoveries of the 20th century, with applications in everything "
            "from testing general relativity to GPS calibration. "
            "Bell Burnell discovered the signal while manually scanning miles "
            "of chart recorder paper from a radio telescope she had helped "
            "build. Her supervisor, Antony Hewish, initially dismissed the "
            "signal as interference. She persisted. The discovery was confirmed. "
            "In 1974, Hewish and radio astronomer Martin Ryle were awarded "
            "the Nobel Prize in Physics for the discovery of pulsars. "
            "Bell Burnell was not included. "
            "Astronomer Fred Hoyle publicly called the omission 'an insult.' "
            "Bell Burnell herself has been characteristically gracious about "
            "the exclusion for decades, though she has also noted that "
            "postgraduate students were typically not included in Nobel "
            "nominations at the time — a convention that applied differently "
            "across genders in practice. "
            "In 2018, Bell Burnell was awarded the Breakthrough Prize in "
            "Fundamental Physics — with a prize of $3 million — which she "
            "donated entirely to fund scholarships for underrepresented groups "
            "in physics. "
            "Sources: Apollo Thirteen; National Geographic; BBC."
        ),
        "city":           "Cambridge",
        "state":          "DC",
        "lat":            52.2053,
        "lng":            0.1218,
        "source_url":     "https://www.apollothirteen.com/article/the-matilda-effect-women-erased-from-science",
        "source_name":    "Apollo Thirteen / BBC / National Geographic",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1967-01-01",
        "tab":            "erasure",
        "country":        "United Kingdom",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # LISE MEITNER — co-discovered nuclear fission, Nobel given to male partner
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_lise_meitner_nuclear_fission",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Lise Meitner (1878–1968) was an Austrian-Swedish physicist who, "
            "along with her long-time collaborator Otto Hahn, co-discovered "
            "nuclear fission in 1938 — the process of splitting the atomic "
            "nucleus that became the scientific foundation of both nuclear "
            "power and nuclear weapons. "
            "Meitner had fled Nazi Germany in 1938 as a Jewish woman. Working "
            "from exile in Stockholm, she and her nephew Otto Frisch provided "
            "the theoretical explanation for the phenomenon Hahn had observed "
            "in his laboratory — she coined the term 'fission.' "
            "In 1944, Otto Hahn alone was awarded the Nobel Prize in Chemistry "
            "for the discovery of nuclear fission. Meitner was not included. "
            "She was nominated for the Nobel Prize 48 times over her career "
            "without winning. "
            "Albert Einstein called her 'the German Marie Curie.' She is "
            "widely considered one of the most egregious cases of Nobel "
            "Prize exclusion in history. "
            "In 1997, element 109 was named Meitnerium in her honor — "
            "making her one of only a handful of non-mythological people "
            "to have an element named after them. "
            "Hahn, in his Nobel acceptance speech, did not mention Meitner. "
            "Sources: Apollo Thirteen; National Geographic; Mental Floss."
        ),
        "city":           "Stockholm",
        "state":          "DC",
        "lat":            59.3293,
        "lng":            18.0686,
        "source_url":     "https://www.apollothirteen.com/article/the-matilda-effect-women-erased-from-science",
        "source_name":    "Apollo Thirteen / Nobel Foundation records",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1938-01-01",
        "tab":            "erasure",
        "country":        "Sweden / Germany",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # HEDY LAMARR — invented spread spectrum (WiFi/Bluetooth foundation)
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_hedy_lamarr_spread_spectrum",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Hedy Lamarr (1914–2000) was an Austrian-American actress and "
            "inventor who in 1942, together with composer George Antheil, "
            "patented a frequency-hopping spread spectrum communication system "
            "designed to make radio-guided torpedoes harder for enemies to "
            "detect or jam during World War II. The technology was ahead of "
            "its time — the US Navy did not adopt it until 1962, after "
            "Lamarr's patent had expired. She received no royalties. "
            "Frequency-hopping spread spectrum is the foundational technology "
            "behind modern WiFi, Bluetooth, and GPS — technologies worth "
            "trillions of dollars globally. "
            "For most of her life Lamarr was known exclusively as a beautiful "
            "actress — described by MGM as 'the most beautiful woman in "
            "Europe' — and her invention was unknown to the public. "
            "She was not recognized for it until 1997, when she received the "
            "Electronic Frontier Foundation Pioneer Award at age 82. "
            "She said: 'It's about time.' She died three years later. "
            "The concealment of her contribution was not accidental: the "
            "entertainment industry and the culture around it had spent "
            "decades defining her entirely by her appearance, making it "
            "structurally impossible for her scientific work to be taken "
            "seriously during her lifetime. "
            "Sources: Mental Floss; EFF; Biography.com."
        ),
        "city":           "Los Angeles",
        "state":          "CA",
        "lat":            34.0522,
        "lng":            -118.2437,
        "source_url":     "https://www.mentalfloss.com/history/women-who-were-written-out-of-history-books",
        "source_name":    "Mental Floss / Electronic Frontier Foundation",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1942-01-01",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # KATHERINE JOHNSON / HIDDEN FIGURES — NASA computers erased
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_katherine_johnson_nasa_hidden_figures",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Katherine Johnson (1918–2020), Dorothy Vaughan (1910–2008), and "
            "Mary Jackson (1921–2005) were among dozens of Black women who "
            "worked as human 'computers' at NASA's Langley Research Center "
            "in Virginia from the 1940s through the 1960s, performing the "
            "complex mathematical calculations that made American spaceflight "
            "possible — including the trajectory calculations for John Glenn's "
            "1962 orbital flight and the Apollo 11 Moon landing. "
            "Glenn himself refused to fly unless Katherine Johnson personally "
            "verified the electronic computer's calculations. "
            "These women worked in a segregated unit, were forced to use "
            "separate bathrooms and cafeteria facilities, and were paid "
            "significantly less than their white male counterparts. Their "
            "contributions were not publicly acknowledged for decades. "
            "The story was largely unknown outside NASA until Margot Lee "
            "Shetterly published Hidden Figures in 2016, later adapted into "
            "an Academy Award-nominated film. "
            "Katherine Johnson was awarded the Presidential Medal of Freedom "
            "in 2015 at age 97. NASA renamed its Washington headquarters the "
            "Mary W. Jackson NASA Headquarters in 2020. "
            "The erasure of these women was not incidental — it was structural: "
            "racism and sexism working together to make their contributions "
            "invisible while their labor made the Space Race possible. "
            "Sources: NASA; National Women's History Museum; Hidden Figures "
            "(Shetterly, 2016)."
        ),
        "city":           "Hampton",
        "state":          "VA",
        "lat":            37.0299,
        "lng":            -76.3452,
        "source_url":     "https://www.nasa.gov/centers/langley/news/researchernews/rn_kjohnson.html",
        "source_name":    "NASA / National Women's History Museum",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1953-01-01",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MARGARET KNIGHT — patent stolen, judge said she couldn't understand her
    # own machine
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_margaret_knight_patent_stolen",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Margaret Knight (1838–1914) was a self-taught American inventor "
            "who in the late 1860s invented a machine that enabled the mass "
            "manufacture of flat-bottomed paper bags — the kind still used "
            "in grocery stores today. She had first demonstrated mechanical "
            "aptitude at age 12, inventing a safety device for textile looms "
            "after a child worker was injured near her. "
            "While having her bag-making machine built by a machinist, a man "
            "named Charles Annan observed the design, made detailed drawings "
            "of it, and filed a patent for it himself before Knight could. "
            "Knight sued him for patent interference. "
            "Annan's defense was that Knight — as a woman — could not possibly "
            "understand the mechanical complexities of the machine and therefore "
            "could not have invented it. The implication was that the invention's "
            "very sophistication proved a woman hadn't made it. "
            "Knight won the lawsuit, produced her original notebooks, drawings, "
            "and witnesses, and was granted the patent in 1871. "
            "She went on to receive at least 87 patents over her lifetime, "
            "inventing machines related to shoes, engines, and manufacturing. "
            "She was sometimes called 'the female Edison' — a framing that "
            "itself reveals the problem: Edison needed no modifier. "
            "Sources: The Noosphere; HuffPost Women; USPTO records."
        ),
        "city":           "Boston",
        "state":          "MA",
        "lat":            42.3601,
        "lng":            -71.0589,
        "source_url":     "https://thenoosphere.substack.com/p/how-the-matilda-effect-explains-why",
        "source_name":    "The Noosphere / USPTO Patent Records",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "1869-01-01",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # HYPATIA OF ALEXANDRIA — murdered by Christian mob, 415 AD
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_hypatia_alexandria_415ad",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "Hypatia of Alexandria (c. 360–415 AD) was a Greek mathematician, "
            "astronomer, and philosopher — the head of the Neoplatonist school "
            "in Alexandria, Egypt, and the first woman whose mathematical "
            "contributions are well documented in history. She wrote commentaries "
            "on advanced mathematics and astronomy, built scientific instruments, "
            "and taught students of all backgrounds including pagans and Christians. "
            "She was also politically influential, advising the Roman prefect "
            "Orestes during a power struggle with Bishop Cyril of Alexandria. "
            "In March 415 AD, a mob of Christian parabalani — lay monks "
            "associated with Bishop Cyril — dragged Hypatia from her chariot "
            "on a public street, stripped her, murdered her with roofing tiles "
            "or oyster shells, tore her body apart, and burned the pieces. "
            "She was killed because she was a woman with intellectual authority, "
            "political influence, and pagan associations in a city undergoing "
            "violent religious consolidation. "
            "Bishop Cyril was later declared a saint and Doctor of the Church "
            "by the Catholic Church. He was never prosecuted. "
            "Hypatia's death is widely regarded as a symbolic end to the "
            "intellectual tradition of the ancient world. "
            "Her story was largely suppressed for centuries. She was recovered "
            "by Enlightenment thinkers as a symbol of reason destroyed by "
            "religious fanaticism. "
            "Sources: Britannica; Mental Floss; historical records."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            31.2001,
        "lng":            29.9187,
        "source_url":     "https://www.mentalfloss.com/history/women-who-were-written-out-of-history-books",
        "source_name":    "Britannica / Mental Floss / Historical Records",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "0415-03-01",
        "tab":            "erasure",
        "country":        "Egypt (Roman Empire)",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # COVERTURE LAWS — legal erasure of married women
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_coverture_laws_married_women",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "Coverture was a legal doctrine inherited from English common law "
            "and adopted across the United States in which a married woman "
            "had no separate legal identity from her husband. Upon marriage, "
            "a woman's legal existence was entirely 'covered' — subsumed — "
            "by her husband's. Under coverture: "
            "A married woman could not own property in her own name. "
            "A married woman could not sign contracts. "
            "A married woman could not sue or be sued. "
            "A married woman could not keep her own wages. "
            "A married woman could not control her own children. "
            "A married woman could not vote (predating suffrage, but also "
            "underlying it — married women were legally non-persons). "
            "A husband could legally beat his wife under the 'rule of thumb' "
            "doctrine — provided the stick was no wider than his thumb. "
            "Coverture was not a medieval relic. It was the law of the United "
            "States. Married Women's Property Acts were passed state by state "
            "beginning in 1839 (Mississippi) and 1848 (New York), but "
            "full legal personhood for married women was achieved only gradually. "
            "Women could not get a credit card in their own name until the "
            "Equal Credit Opportunity Act of 1974. "
            "Women could not be guaranteed the right to keep their own last "
            "name in all US states until the 1970s and 1980s. "
            "Marital rape was not a crime in all 50 US states until 1993. "
            "The argument that men have historically been 'providers and "
            "protectors' of women cannot be separated from the fact that "
            "the law made women's independent economic existence illegal — "
            "creating dependency by force, not by nature or consent. "
            "Sources: Legal Information Institute; National Women's History "
            "Museum; ACLU."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://www.womenshistory.org/resources/general/coverture",
        "source_name":    "National Women's History Museum / Legal Information Institute",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1765-01-01",
        "tab":            "erasure",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # WOMEN BANNED FROM UNIVERSITIES — timeline of exclusion
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "erasure_women_banned_universities_timeline",
        "violence_type":  "coercive_control",
        "status":         "congressional_record",
        "summary": (
            "The exclusion of women from formal higher education was not a "
            "natural condition — it was an actively enforced legal and "
            "institutional policy that persisted well into the 20th century. "
            "Key dates: "
            "1322 — Jacoba Felicie prosecuted by Paris Faculty of Medicine "
            "for practicing medicine without a license she was legally "
            "forbidden from obtaining. "
            "1405 — Christine de Pizan, one of the first professional women "
            "writers in Europe, wrote The Book of the City of Ladies "
            "specifically to counter male scholars' claims that women were "
            "intellectually inferior by nature. "
            "1869 — Harvard Medical School rejected its first female applicants. "
            "Women were not fully admitted to Harvard Medical School until 1945. "
            "1870 — Sophia Jex-Blake led a group of women (The Edinburgh Seven) "
            "who enrolled in medicine at the University of Edinburgh. They were "
            "physically attacked by a male mob at their anatomy exam (the Surgeons' "
            "Hall Riot). The university eventually cancelled their degrees. "
            "1882 — Cambridge University allowed women to sit exams but would "
            "not grant them degrees. Women's colleges (Girton, Newnham) were "
            "established but their students received only certificates. "
            "1920 — Oxford University first granted degrees to women. "
            "1948 — Cambridge University first granted full degrees to women. "
            "Until 1972, Title IX did not require equal access to education "
            "in the United States. Many law schools, medical schools, and "
            "business schools maintained explicit female admission quotas — "
            "or bans — well into the 1960s. "
            "The same institutions that excluded women from licensing and "
            "education then pointed to women's lack of credentials as proof "
            "of their intellectual inferiority. This is the architecture of "
            "manufactured dependency: create the barrier, then cite the "
            "barrier as evidence of natural limitation. "
            "Sources: National Women's History Museum; Oxford University "
            "history; Cambridge University history; Edinburgh University "
            "records; Title IX legislative history."
        ),
        "city":           "Washington",
        "state":          "DC",
        "lat":            38.9072,
        "lng":            -77.0369,
        "source_url":     "https://www.womenshistory.org/resources/general/education",
        "source_name":    "National Women's History Museum / University Historical Records",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1322-01-01",
        "tab":            "erasure",
    },

]


def main():
    print("\n  [Medusa] Seeding Erasure tab...\n")
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
    print("  NOTE: All erasure records use tab='erasure'.")
    print("  Non-US records use state='DC' as placeholder with")
    print("  country field set for frontend filtering.\n")


if __name__ == "__main__":
    main()
