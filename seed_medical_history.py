#!/usr/bin/env python3
"""
seed_medical_history.py — Historical medical laws, practices, and inventions
that treated women's bodies as problems to be managed, controlled, or experimented on.

Sources: Medical history scholarship, FDA, NIH, peer-reviewed journals,
court records, congressional testimony.

Run: python3 seed_medical_history.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    # ── CHAINSAW / SYMPHYSIOTOMY ───────────────────────────────────────────────
    {
        "summary": (
            "The Chainsaw Was Invented to Cut Women Open During Childbirth. "
            "The chainsaw was invented in 1780 by Scottish surgeons John Aitken "
            "and James Jeffray — not for lumber, but for symphysiotomy: a "
            "procedure to widen a woman's pelvis during obstructed childbirth "
            "by sawing through the cartilage and bone of the pubic symphysis. "
            "Women were awake during the procedure. Anesthesia did not yet exist. "
            "The hand-cranked chain saw with serrated teeth was designed to make "
            "the cutting faster because surgeons found manual knives too slow. "
            "Symphysiotomy was performed on women in Ireland by the Catholic "
            "Church-controlled medical system well into the 1980s — long after "
            "safe cesarean sections were available — because the Church opposed "
            "C-sections on the grounds they might lead to contraception. "
            "An estimated 1,500 Irish women were subjected to symphysiotomy "
            "between 1944 and 1987. Survivors suffered lifelong disability — "
            "chronic pain, incontinence, and difficulty walking. Ireland's "
            "government paid redress to survivors beginning in 2014."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1780-01-01",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1376979/",
        "source_name": "NIH — History of Symphysiotomy / Irish Redress Scheme",
        "verified": True,
        "is_public_figure": False,
    },

    # ── HYSTERIA ──────────────────────────────────────────────────────────────
    {
        "summary": (
            "Hysteria — The Medical Diagnosis Used to Imprison and Experiment "
            "on Women for 2,000 Years. 'Hysteria' — from the Greek 'hystera' "
            "meaning uterus — was a medical diagnosis applied almost exclusively "
            "to women from ancient Greece through the late 20th century. "
            "Symptoms included: anxiety, fainting, nervousness, sexual desire, "
            "insomnia, irritability, and 'a tendency to cause trouble.' "
            "Treatment included pelvic massage by physicians to induce 'hysterical "
            "paroxysm' — orgasm — which was not recognized as such. The vibrator "
            "was invented in the 1880s as a medical device to relieve physician "
            "fatigue from performing these treatments. Women diagnosed with "
            "hysteria were committed to asylums, subjected to clitoridectomy "
            "(surgical removal of the clitoris), hysterectomy, and other "
            "procedures. Sigmund Freud's entire psychoanalytic framework was "
            "built largely on hysterical female patients. Hysteria was not "
            "removed from the DSM until 1980. Researchers have since identified "
            "that many 'hysterical' women were likely experiencing epilepsy, "
            "PTSD, endometriosis, or other conditions that medicine was not "
            "equipped to diagnose because it refused to take women's symptoms seriously."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1980-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3480686/",
        "source_name": "NIH — History of Hysteria Diagnosis / DSM History",
        "verified": True,
        "is_public_figure": False,
    },

    # ── LOBOTOMY ──────────────────────────────────────────────────────────────
    {
        "summary": (
            "Lobotomy — Primarily Performed on Women Who Were 'Difficult.' "
            "The prefrontal lobotomy — severing connections in the brain's "
            "frontal lobe — was performed on approximately 40,000 Americans "
            "between 1936 and the 1970s. The majority were women. Walter "
            "Freeman, who pioneered the 'ice pick' transorbital lobotomy "
            "in the US, performed over 3,400 procedures — driving from state "
            "to state in his 'lobotomobile.' Women were lobotomized for "
            "depression, anxiety, 'excessive emotionality,' homosexuality, "
            "and being 'difficult' or 'unmanageable.' Husbands could commit "
            "wives for lobotomy without their consent. Rosemary Kennedy, "
            "sister of President John F. Kennedy, was lobotomized at age 23 "
            "by her father without her knowledge or consent because she was "
            "'moody' and had begun to sneak out at night. She spent the rest "
            "of her life institutionalized, unable to walk or speak clearly. "
            "Freeman was eventually stripped of his medical license in 1967 "
            "after a patient died — but faced no criminal charges for the "
            "thousands of women he had permanently brain-damaged."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1967-01-01",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3549470/",
        "source_name": "NIH — History of Lobotomy / Walter Freeman Medical Records",
        "verified": True,
        "is_public_figure": False,
    },

    # ── THALIDOMIDE ───────────────────────────────────────────────────────────
    {
        "summary": (
            "Thalidomide — Prescribed to Pregnant Women, Caused 10,000 Birth "
            "Defects. Thalidomide was marketed from 1957 as a sedative and "
            "treatment for morning sickness in pregnant women. It had never "
            "been tested on pregnant animals. Between 1957 and 1962, it caused "
            "an estimated 10,000 children worldwide to be born with severe limb "
            "deformities — missing or shortened arms and legs. Thousands more "
            "died. FDA reviewer Frances Oldham Kelsey blocked thalidomide's "
            "US approval in 1960 because she was not satisfied with the safety "
            "data — saving thousands of American children. The manufacturer, "
            "Chemie Grünenthal, had suppressed evidence of neurological side "
            "effects. No executives were ever imprisoned. Thalidomide is still "
            "used today for certain conditions — with strict controls. The "
            "disaster led directly to the 1962 Kefauver-Harris Amendment "
            "requiring proof of drug efficacy and safety before approval — "
            "but it did not require testing in pregnant women, a gap that "
            "persists in drug development today."
        ),
        "city": "Silver Spring", "state": "MD",
        "lat": 38.9907, "lng": -77.0261,
        "date_incident": "1962-10-10",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://www.fda.gov/drugs/historyfdaapproveddrugproducts/thalidomide-story",
        "source_name": "FDA — Thalidomide History / Kefauver-Harris Amendment",
        "verified": True,
        "is_public_figure": False,
    },

    # ── DES ───────────────────────────────────────────────────────────────────
    {
        "summary": (
            "DES (Diethylstilbestrol) — Synthetic Estrogen Given to Pregnant "
            "Women Caused Cancer in Their Daughters. DES was prescribed to "
            "an estimated 5–10 million pregnant women in the US between 1940 "
            "and 1971 to prevent miscarriage — despite evidence as early as "
            "1953 that it did not work. In 1971, researchers discovered that "
            "daughters of women who took DES had dramatically elevated rates "
            "of a rare vaginal cancer — clear cell adenocarcinoma — as well "
            "as reproductive abnormalities, higher rates of breast cancer, "
            "and fertility problems. DES sons had elevated rates of testicular "
            "abnormalities. DES grandchildren may also be affected. The FDA "
            "banned DES for use in pregnancy in 1971. No manufacturer was "
            "ever held criminally liable. Lawsuits were complicated by the "
            "fact that multiple companies made DES and victims could not "
            "identify which manufacturer their mother had used. DES Daughters "
            "continue to be monitored for health effects decades later — "
            "a generation of women harmed before birth by a drug their "
            "mothers were told was safe."
        ),
        "city": "Silver Spring", "state": "MD",
        "lat": 38.9907, "lng": -77.0261,
        "date_incident": "1971-11-01",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://www.fda.gov/drugs/specific-populations/des-exposure",
        "source_name": "FDA — DES History and Health Effects",
        "verified": True,
        "is_public_figure": False,
    },

    # ── TWILIGHT SLEEP ────────────────────────────────────────────────────────
    {
        "summary": (
            "Twilight Sleep — Women Restrained, Drugged, and Made to Forget "
            "Childbirth. 'Twilight sleep' was a combination of morphine and "
            "scopolamine used in childbirth from the 1910s through the 1970s. "
            "Scopolamine caused amnesia — women felt pain but would not "
            "remember it. Because they thrashed and screamed during labor "
            "they were strapped to their beds in darkened rooms, sometimes "
            "with their hands bound, helmets on their heads to prevent "
            "injury, and padded walls. The procedure was promoted as "
            "humane — giving women 'painless' childbirth — when in reality "
            "it gave doctors convenient, compliant patients who could not "
            "remember what was done to them. Women were separated from their "
            "newborns for hours or days. Twilight sleep caused neonatal "
            "respiratory depression — babies born sedated and sometimes "
            "failing to breathe. The practice was widely used in the US "
            "for six decades before patient advocacy finally ended it. "
            "It is one of the clearest examples of obstetric medicine "
            "prioritizing physician convenience over women's autonomy and safety."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1970-01-01",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1376979/",
        "source_name": "NIH — History of Obstetric Anesthesia / Twilight Sleep",
        "verified": True,
        "is_public_figure": False,
    },

    # ── J. MARION SIMS ────────────────────────────────────────────────────────
    {
        "summary": (
            "J. Marion Sims — 'Father of Modern Gynecology' Experimented on "
            "Enslaved Black Women Without Anesthesia. J. Marion Sims, "
            "celebrated as the father of modern gynecology, developed surgical "
            "techniques for vesico-vaginal fistula repair by operating "
            "repeatedly on enslaved Black women in Montgomery, Alabama "
            "between 1845 and 1849 — without anesthesia. He operated on "
            "one woman, Anarcha, at least 30 times. He justified withholding "
            "anesthesia — which was available — on the racist belief that "
            "Black people did not feel pain the same way white people did. "
            "This belief — documented as influencing medical treatment of "
            "Black patients into the 21st century — is directly traceable "
            "to the Sims era. Statues of Sims in New York and Alabama were "
            "removed following protests in 2018. The techniques he developed "
            "through non-consensual experimentation on enslaved women are "
            "still used in gynecological surgery today — with no acknowledgment "
            "of the women whose suffering produced them."
        ),
        "city": "Montgomery", "state": "AL",
        "lat": 32.3668, "lng": -86.2999,
        "date_incident": "1849-01-01",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1376979/",
        "source_name": "NIH — J. Marion Sims History / Medical Ethics Scholarship",
        "verified": True,
        "is_public_figure": True,
    },

    # ── FEMININE PRODUCTS NOT TESTED WITH BLOOD ───────────────────────────────
    {
        "summary": (
            "Menstrual Products Tested with Blue Liquid — Not Blood. For "
            "decades, menstrual pad and tampon advertisements used blue "
            "liquid in product demonstrations instead of blood — a practice "
            "so universal it became the standard. More significantly, "
            "the absorbency testing standards used by the FDA and industry "
            "for menstrual products were developed using saline solution, "
            "not menstrual blood. Research has documented that menstrual "
            "blood has significantly different viscosity, clotting properties, "
            "and composition than saline — meaning absorbency ratings on "
            "product packaging may not accurately reflect real-world "
            "performance. A 2023 study found significant discrepancies "
            "between labeled and actual absorbency. The FDA has acknowledged "
            "the limitation but has not updated testing standards to use "
            "actual blood or a biologically accurate substitute. Women "
            "have been making purchasing decisions based on absorbency "
            "ratings calculated with a liquid that does not behave like "
            "menstrual blood — contributing to both leakage and to the "
            "over-insertion of tampons that elevates TSS risk."
        ),
        "city": "Silver Spring", "state": "MD",
        "lat": 38.9907, "lng": -77.0261,
        "date_incident": "2023-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.fda.gov/medical-devices/tampons/absorbency",
        "source_name": "FDA — Tampon Absorbency Standards / BMJ Research on Menstrual Product Testing",
        "verified": True,
        "is_public_figure": False,
    },

    # ── CLITORIDECTOMY ────────────────────────────────────────────────────────
    {
        "summary": (
            "Clitoridectomy — Surgical Removal of the Clitoris Performed "
            "by American Doctors as 'Treatment.' Clitoridectomy — the "
            "surgical removal of the clitoris — was performed by American "
            "and British physicians from the 1860s through the 1930s as "
            "treatment for masturbation, hysteria, epilepsy, and 'excessive "
            "sexual desire' in women and girls. Isaac Baker Brown, a "
            "prominent British gynecologist, performed clitoridectomies "
            "on women without their consent — including women brought in "
            "by husbands who found them 'difficult.' He was eventually "
            "expelled from the Obstetrical Society of London in 1867 — "
            "not for harming women, but for performing the procedure "
            "without husbands' consent. In the US, Dr. Mary Dixon Jones "
            "performed oophorectomies (removal of ovaries) and other "
            "procedures on women for similar indications into the 1890s. "
            "These procedures were legal, medically endorsed, and performed "
            "on women who had no legal recourse. Female genital mutilation "
            "performed by Western physicians on Western women is rarely "
            "discussed in the context of FGM — but it was the same act."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1867-01-01",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1376979/",
        "source_name": "NIH — History of Clitoridectomy in Western Medicine",
        "verified": True,
        "is_public_figure": False,
    },

    # ── RADIATION EXPERIMENTS ─────────────────────────────────────────────────
    {
        "summary": (
            "US Government Radiation Experiments on Women — Cold War Era. "
            "Between the 1940s and 1970s, the US government and military "
            "conducted radiation experiments on thousands of unwitting "
            "Americans — a disproportionate number of them women, prisoners, "
            "poor patients, and people of color. Women with cervical cancer "
            "were given experimental radiation doses without full informed "
            "consent. Pregnant women were given radioactive iodine to "
            "study fetal thyroid development. Women at a Tennessee prenatal "
            "clinic were given radioactive iron without being told. A 1994 "
            "Advisory Committee on Human Radiation Experiments, commissioned "
            "by President Clinton, documented over 4,000 radiation experiments "
            "conducted on Americans without proper consent. The committee "
            "found that women and minority patients were disproportionately "
            "used as subjects. No one was criminally prosecuted. The "
            "experiments were classified for decades — victims and their "
            "families were never told what had been done to them."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1994-10-03",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://ehss.energy.gov/ohre/roadmap/achre/report.html",
        "source_name": "Advisory Committee on Human Radiation Experiments — Final Report 1994",
        "verified": True,
        "is_public_figure": False,
    },

    # ── BIRTH CONTROL TRIALS ON WOMEN OF COLOR ────────────────────────────────
    {
        "summary": (
            "Birth Control Pill Trials — First Tested on Poor Puerto Rican "
            "Women Without Full Disclosure. The first large-scale trials of "
            "the birth control pill were conducted in Puerto Rico beginning "
            "in 1956 by Gregory Pincus and John Rock — funded by Katharine "
            "McCormick and Margaret Sanger. Poor Puerto Rican women were "
            "recruited as subjects. They were not told they were in a trial "
            "— they were told they were taking a pill to prevent pregnancy. "
            "They were not told the pill was experimental. They were not "
            "told about side effects. Three women died during the trials; "
            "their deaths were not investigated. Women who reported side "
            "effects — nausea, headaches, blood clots — were told the "
            "symptoms were psychosomatic. The pill was approved by the FDA "
            "in 1960. Puerto Rico was chosen specifically because the "
            "researchers believed they could conduct trials there that "
            "would not be permitted on the US mainland — exploiting "
            "colonial status and poverty to use women's bodies as "
            "testing grounds for a drug that would primarily benefit "
            "white middle-class American women."
        ),
        "city": "San Juan", "state": "PR",
        "lat": 18.4655, "lng": -66.1057,
        "date_incident": "1956-01-01",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1550885/",
        "source_name": "NIH — Birth Control Pill Trials Puerto Rico / FDA History",
        "verified": True,
        "is_public_figure": False,
    },

    # ── MEDICAL RESEARCH EXCLUSION ────────────────────────────────────────────
    {
        "summary": (
            "Women Excluded from Medical Research — The Male Default That Kills. "
            "For most of the 20th century, the default human research subject "
            "was a 70kg white male. Women were excluded from clinical trials "
            "citing concerns about hormonal variability and potential pregnancy — "
            "but the real cost was paid in women's lives. The NIH Revitalization "
            "Act of 1993 was the first law requiring inclusion of women in "
            "federally funded research. Before 1993: drug dosages were calculated "
            "for male metabolism; disease presentations in women were unknown; "
            "eight drugs approved by the FDA between 1997-2000 were withdrawn "
            "because of life-threatening side effects that appeared primarily "
            "in women and had not been detected in male-dominated trials. "
            "Even after 1993, female animals were excluded from most preclinical "
            "research until a 2016 NIH policy change. The biological mechanisms "
            "of pain, cardiovascular disease, stroke, and autoimmune conditions "
            "differ significantly by sex — but because female subjects were "
            "excluded, these differences were unknown for decades and women "
            "were treated with protocols developed without them."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1993-06-10",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://orwh.od.nih.gov/research/inclusion/women-and-minorities",
        "source_name": "NIH Office of Research on Women's Health — History of Inclusion Policy",
        "verified": True,
        "is_public_figure": False,
    },

    # ── PERIOD POVERTY AND PRISONS ────────────────────────────────────────────
    {
        "summary": (
            "Menstrual Products Withheld in Prisons — Used as Punishment "
            "and Control. Incarcerated women across the United States have "
            "documented being denied adequate menstrual products — forced "
            "to use socks, toilet paper, or torn clothing during their "
            "periods. In some facilities, pads were rationed to fewer than "
            "needed, or women were required to exchange used products to "
            "receive new ones. The ACLU and multiple journalists have "
            "documented menstrual product denial in federal, state, and "
            "county facilities across the country. The First Step Act (2018) "
            "required the federal Bureau of Prisons to provide free menstrual "
            "products — but state and county facilities were not covered. "
            "As of 2023, fewer than half of states had laws guaranteeing "
            "adequate menstrual products in correctional facilities. "
            "The withholding of menstrual products is a form of bodily "
            "control and humiliation disproportionately affecting women "
            "of color, who are overrepresented in the incarcerated population."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.aclu.org/issues/prisoners-rights/women-prison",
        "source_name": "ACLU — Menstrual Equity in Prisons / First Step Act 2018",
        "verified": True,
        "is_public_figure": False,
    },
]


def main():
    print("[Seed Medical History] Seeding historical medical laws and practices that harmed women...")
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
    print(f"[Seed Medical History] {saved}/{len(RECORDS)} records saved.")
    print(f"Total in database: {get_case_count()}")


if __name__ == "__main__":
    main()
