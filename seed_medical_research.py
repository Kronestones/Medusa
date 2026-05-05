#!/usr/bin/env python3
"""
seed_medical_research.py — Women excluded from medical research, the male
default in medicine, toxic feminine hygiene products, and documented deaths
from medical knowledge gaps caused by female exclusion from clinical trials.

Sources: NIH, FDA, CDC, peer-reviewed journals, court records, investigative
journalism, congressional testimony.

Run: python3 seed_medical_research.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    # ── EXCLUSION FROM CLINICAL TRIALS ────────────────────────────────────────
    {
        "summary": (
            "Women Excluded from NIH Clinical Trials Until 1993 — Documented Deaths "
            "from Knowledge Gaps. For most of the 20th century, women were "
            "systematically excluded from federally funded medical research. The "
            "NIH Revitalization Act of 1993 was the first law requiring inclusion "
            "of women and minorities in clinical trials. Before 1993, the default "
            "research subject was a 70kg white male — and findings were applied to "
            "women without validation. The consequences are documented and lethal: "
            "drug dosages were calculated for male metabolism, side effects in women "
            "were unknown, and disease presentations in women were unrecognized. "
            "Eight drugs approved by the FDA between 1997 and 2000 were withdrawn "
            "from the market because of life-threatening side effects — effects that "
            "disproportionately or exclusively affected women and had not been "
            "detected in male-dominated trials. The exclusion was justified by "
            "concerns about hormone variability and liability — the cost was paid "
            "in women's lives."
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
    {
        "summary": (
            "Heart Disease in Women — Decades of Misdiagnosis Due to Male-Only "
            "Research. Heart disease is the leading cause of death for women in the "
            "US — killing more women than all cancers combined. Yet for decades, "
            "cardiac research was conducted almost exclusively on men. The classic "
            "heart attack symptoms — chest pain radiating to the left arm — are "
            "primarily male presentations. Women more commonly experience nausea, "
            "jaw pain, back pain, fatigue, and shortness of breath. Because these "
            "symptoms were not in the diagnostic literature, women presenting with "
            "heart attacks were systematically misdiagnosed, sent home, or told "
            "their symptoms were anxiety or gastrointestinal. A 2000 study found "
            "women were seven times more likely than men to be misdiagnosed during "
            "a heart attack. Women under 55 are twice as likely to die from a heart "
            "attack as men the same age — a gap directly attributable to diagnostic "
            "protocols developed without female research subjects."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2000-07-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.heart.org/en/health-topics/heart-attack/warning-signs-of-a-heart-attack/heart-attack-symptoms-in-women",
        "source_name": "American Heart Association — Heart Attack Symptoms in Women / JAMA Research",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Ambien (Zolpidem) — FDA Required Dose Cut in Half for Women in 2013, "
            "20 Years After Approval. Zolpidem (Ambien) was approved by the FDA "
            "in 1992 and prescribed at the same dose to men and women for two "
            "decades. In 2013, the FDA required the recommended dose for women "
            "to be cut in half — because women metabolize the drug more slowly "
            "and were waking up with dangerous levels still in their blood, "
            "impairing driving. Studies found women were significantly more likely "
            "to be involved in traffic accidents the morning after taking Ambien. "
            "This was not discovered during trials — because women were "
            "underrepresented. The FDA's own analysis found that of 500 drug "
            "studies submitted between 1995 and 2000, almost half had no sex-based "
            "analysis of results. Ambien is one of the most documented examples "
            "of the deadly consequences of the male research default."
        ),
        "city": "Silver Spring", "state": "MD",
        "lat": 38.9907, "lng": -77.0261,
        "date_incident": "2013-01-10",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.fda.gov/drugs/drug-safety-and-availability/fda-drug-safety-communication-fda-recommends-lower-doses-zolpidem",
        "source_name": "FDA Drug Safety Communication — Zolpidem Dosage 2013",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Aspirin and Heart Attack Prevention — Decades of Wrong Advice for Women. "
            "For years, doctors recommended daily low-dose aspirin to prevent heart "
            "attacks — based on a landmark 1988 study of 22,071 subjects. All of "
            "them were male physicians. The Physicians' Health Study results were "
            "applied universally to women — but aspirin's protective effects differ "
            "by sex. A 2005 Women's Health Study of 40,000 women found aspirin "
            "reduced stroke risk in women but did not reduce heart attack risk in "
            "women under 65 — the opposite of the male findings. Millions of women "
            "took daily aspirin for decades based on research that did not include "
            "them, with associated risks of gastrointestinal bleeding. The 2005 "
            "findings were a turning point — but it took nearly 20 years of applying "
            "male data to women before a women-specific study was conducted. "
            "The pattern repeats across dozens of drugs and treatments."
        ),
        "city": "Boston", "state": "MA",
        "lat": 42.3601, "lng": -71.0589,
        "date_incident": "2005-03-07",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.nejm.org/doi/full/10.1056/NEJMoa050613",
        "source_name": "New England Journal of Medicine — Women's Health Study: Aspirin 2005",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Autoimmune Disease — 80% of Patients Are Women, Vastly Underfunded. "
            "Autoimmune diseases — including lupus, rheumatoid arthritis, multiple "
            "sclerosis, Hashimoto's thyroiditis, and Sjögren's syndrome — affect "
            "approximately 50 million Americans. 80% are women. Despite this, "
            "autoimmune research receives a fraction of the NIH funding allocated "
            "to diseases that primarily affect men. Lupus receives less NIH funding "
            "per patient than almost any other disease of comparable prevalence. "
            "Women with autoimmune conditions wait an average of 4.6 years and see "
            "5 different doctors before receiving a correct diagnosis — a delay "
            "directly attributable to the historic exclusion of women from research "
            "and the resulting gaps in diagnostic criteria. The symptoms — fatigue, "
            "pain, brain fog — are the same symptoms routinely dismissed as "
            "psychosomatic in women."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.niaid.nih.gov/diseases-conditions/autoimmune-diseases",
        "source_name": "NIH NIAID — Autoimmune Diseases / American Autoimmune Related Diseases Association",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Pain Research — Women's Pain Systematically Undertreated Due to Male "
            "Research Default. A comprehensive 2001 review in the Journal of Pain "
            "found that women experience pain more frequently, more severely, and "
            "over longer durations than men across virtually every pain condition "
            "studied — yet receive less pain treatment. Women are more likely to "
            "be prescribed sedatives for pain; men receive analgesics. Women are "
            "more likely to be told their pain is psychological. The underlying "
            "cause: most foundational pain research was conducted on male subjects, "
            "male rodents, and male cell lines. The biological mechanisms of pain "
            "differ by sex — but because female subjects were excluded, these "
            "differences were unknown for decades. A 2016 NIH policy began "
            "requiring the inclusion of female animals in preclinical research — "
            "acknowledging that the prior all-male default had produced an "
            "incomplete and harmful scientific record."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2016-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.nih.gov/research-training/inclusion-women-minorities-research",
        "source_name": "NIH — Sex as Biological Variable Policy 2016 / Journal of Pain",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Stroke in Women — Misdiagnosed Because Research Was Done on Men. "
            "Women experience approximately 55,000 more strokes than men each year "
            "in the US and are more likely to die from stroke. Women have unique "
            "stroke risk factors — pregnancy, preeclampsia, oral contraceptive use, "
            "and migraine with aura — that were poorly understood because stroke "
            "research historically focused on men. Women present with atypical "
            "stroke symptoms — confusion, hiccups, nausea, face pain — more often "
            "than men. Emergency physicians trained on male symptom profiles "
            "consistently underdiagnose stroke in women. A 2019 study found women "
            "were 33% more likely than men to be initially misdiagnosed in the ER "
            "when presenting with stroke. Delayed diagnosis means delayed treatment "
            "— and stroke outcomes are directly time-dependent. Women die from "
            "strokes that men with the same presentation survive."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2019-02-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.ahajournals.org/doi/10.1161/STROKEAHA.118.023557",
        "source_name": "Stroke Journal — Sex Differences in Stroke Misdiagnosis 2019",
        "verified": True,
        "is_public_figure": False,
    },

    # ── TOXIC FEMININE PRODUCTS ───────────────────────────────────────────────
    {
        "summary": (
            "Toxic Shock Syndrome — Tampon Industry Concealed Risk. Toxic Shock "
            "Syndrome (TSS) killed at least 38 women and caused hundreds of "
            "serious illnesses in 1980 alone — linked to Rely brand superabsorbent "
            "tampons manufactured by Procter & Gamble. Internal P&G documents "
            "revealed in litigation showed the company had evidence of TSS risk "
            "before the outbreak and failed to warn consumers or the FDA. Rely "
            "was recalled in 1980. TSS is caused by Staphylococcus aureus bacteria "
            "proliferating in highly absorbent tampons left in place for extended "
            "periods. Despite the 1980 outbreak, TSS warnings on tampon packaging "
            "remain minimal. Cases continue to occur — predominantly in young women "
            "and girls unfamiliar with risk. The FDA classifies tampons as Class II "
            "medical devices but does not require manufacturers to disclose all "
            "ingredients or conduct long-term safety studies on internal use."
        ),
        "city": "Cincinnati", "state": "OH",
        "lat": 39.1031, "lng": -84.5120,
        "date_incident": "1980-09-22",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.fda.gov/medical-devices/tampons/toxic-shock-syndrome",
        "source_name": "FDA — Toxic Shock Syndrome and Tampons / P&G Rely Recall",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "PFAS in Menstrual Products — 'Forever Chemicals' Found in Period Underwear "
            "and Pads. PFAS (per- and polyfluoroalkyl substances) — synthetic chemicals "
            "linked to cancer, thyroid disruption, immune suppression, and reproductive "
            "harm — have been detected in multiple brands of period underwear, panty "
            "liners, and menstrual pads. A 2023 study by University of Notre Dame "
            "researchers found high levels of organic fluorine (a PFAS indicator) in "
            "Thinx period underwear and other brands. Thinx settled a class action "
            "lawsuit for $5 million in 2023. PFAS are absorbed through skin — and "
            "the vulvar and vaginal tissue where period products are worn is among "
            "the most permeable skin on the body. The FDA does not currently require "
            "PFAS testing for menstrual products. There are no federal standards "
            "limiting PFAS in products worn against genitalia. Women using these "
            "products for decades have had no way of knowing they were being exposed."
        ),
        "city": "South Bend", "state": "IN",
        "lat": 41.6764, "lng": -86.2520,
        "date_incident": "2023-01-17",
        "violence_type": "coercive_control",
        "status": "settled",
        "source_url": "https://pubs.acs.org/doi/10.1021/acs.estlett.3c00313",
        "source_name": "Environmental Science & Technology Letters — PFAS in Period Underwear 2023",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Dioxins in Tampons — Byproduct of Chlorine Bleaching Process. Dioxins "
            "are among the most toxic chemicals known — classified as human "
            "carcinogens by the WHO, with no safe level of exposure. Conventional "
            "tampons are made from cotton and rayon bleached with chlorine — a "
            "process that produces dioxin byproducts. The FDA acknowledged dioxin "
            "presence in tampons but has maintained that levels are 'below detectable "
            "limits' using current testing. Critics argue the testing methodology "
            "is inadequate and that cumulative lifetime exposure from internal use "
            "beginning at menarche has never been studied. Women use approximately "
            "11,000 tampons in a lifetime. The vaginal mucosa absorbs chemicals "
            "more efficiently than other skin. Independent researchers have called "
            "for comprehensive safety testing — the FDA has not mandated it. "
            "Organic cotton tampon manufacturers have pivoted to non-chlorine "
            "bleaching specifically because of dioxin concerns."
        ),
        "city": "Silver Spring", "state": "MD",
        "lat": 38.9907, "lng": -77.0261,
        "date_incident": "2019-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.fda.gov/medical-devices/tampons/ingredients-tampons",
        "source_name": "FDA — Tampon Ingredients and Safety / WHO Dioxin Classification",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Pesticide Residue in Tampons — 2024 Study Finds Glyphosate and Other "
            "Agrochemicals. A 2024 study published in Frontiers in Public Health "
            "tested 30 tampon brands — both conventional and organic — and found "
            "pesticide residues including glyphosate (the active ingredient in "
            "Roundup, classified as a probable human carcinogen by the WHO's "
            "International Agency for Research on Cancer) in the majority of "
            "products tested. Cotton is one of the most heavily pesticide-treated "
            "crops in the world. The FDA does not require pesticide testing for "
            "menstrual products. Manufacturers are not required to disclose "
            "pesticide residue levels. The study found pesticide residues in both "
            "conventional and some organic products. Internal exposure to "
            "glyphosate through vaginal mucosa has never been studied for "
            "long-term health effects. The researchers called for immediate "
            "FDA regulatory action — none had been taken as of 2024."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2024-07-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.frontiersin.org/articles/10.3389/fpubh.2024.1363716",
        "source_name": "Frontiers in Public Health — Pesticides in Tampons 2024",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Johnson & Johnson Talcum Powder — Ovarian Cancer Linked to Baby Powder, "
            "$2.1 Billion Verdict. Johnson & Johnson marketed talcum powder for "
            "feminine hygiene for decades — encouraging women to apply it to their "
            "genitals daily. Internal J&J documents revealed in litigation showed "
            "the company knew as early as the 1970s that its talc contained "
            "asbestos and that there were concerns about links to ovarian cancer. "
            "J&J continued marketing the product for genital use. In 2018, Reuters "
            "published an investigation revealing the asbestos contamination and "
            "internal concealment. In 2020, J&J discontinued talc-based baby powder "
            "in the US and Canada. A Missouri jury awarded $2.1 billion to 22 women "
            "with ovarian cancer in 2018. Tens of thousands of lawsuits were filed. "
            "J&J attempted to use bankruptcy to limit payouts — a legal maneuver "
            "courts repeatedly blocked. The company's continued marketing of a "
            "product it knew was contaminated, specifically to women for intimate "
            "use, represents one of the most documented cases of corporate harm "
            "targeting women's bodies."
        ),
        "city": "New Brunswick", "state": "NJ",
        "lat": 40.4870, "lng": -74.4453,
        "date_incident": "2018-07-12",
        "violence_type": "assault",
        "status": "settled",
        "source_url": "https://www.reuters.com/investigates/special-report/johnsonandjohnson-cancer/",
        "source_name": "Reuters — J&J Knew for Decades That Asbestos Lurked in Its Baby Powder",
        "verified": True,
        "is_public_figure": True,
    },
    {
        "summary": (
            "Douching Products — Marketed to Women for Decades Despite Documented "
            "Harm. Vaginal douching products were marketed to women throughout the "
            "20th century — often with messaging implying that the natural vaginal "
            "environment was unclean or odorous and required correction. Scientific "
            "consensus now firmly establishes that douching disrupts the vaginal "
            "microbiome, increases risk of bacterial vaginosis, pelvic inflammatory "
            "disease, and ectopic pregnancy, and is associated with increased "
            "STI transmission and cervical cancer risk. Despite this, douching "
            "products remained on the market and were actively advertised until "
            "the 1990s. Lysol — a disinfectant — was marketed as a feminine hygiene "
            "product and birth control method from the 1920s through the 1950s. "
            "The FDA has never required pre-market safety studies for douching "
            "products. Approximately 20% of American women still douche regularly "
            "— primarily women of color who are targeted by remaining marketing. "
            "The harm from decades of douching promotion is documented and ongoing."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.acog.org/clinical/clinical-guidance/committee-opinion/articles/2020/07/feminine-hygiene-products",
        "source_name": "American College of OB/GYN — Feminine Hygiene Products Committee Opinion 2020",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Essure — FDA-Approved Permanent Contraceptive Device Injured 30,000+ "
            "Women. Essure was a permanent contraceptive device — metal coils "
            "inserted into the fallopian tubes — approved by the FDA in 2002. "
            "By 2018, the FDA had received over 30,000 adverse event reports "
            "including device migration, organ perforation, chronic pain, "
            "autoimmune reactions, and unintended pregnancies. Bayer, the "
            "manufacturer, had conducted pre-approval trials that were later "
            "found to have significant methodological flaws and excluded women "
            "who experienced complications. Women who reported complications "
            "were dismissed by doctors trained to defend the device. Erin Brockovich "
            "organized affected women into a national advocacy group. The FDA "
            "restricted Essure's sale in 2018 and Bayer voluntarily withdrew "
            "it from the US market. Bayer settled approximately 90% of the "
            "pending US lawsuits for a reported $1.6 billion. The Essure case "
            "is a landmark in the failure of medical device regulation to "
            "protect women."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2018-07-20",
        "violence_type": "assault",
        "status": "settled",
        "source_url": "https://www.fda.gov/medical-devices/essure-permanent-birth-control/essure-benefits-and-risks",
        "source_name": "FDA — Essure Adverse Events / Bayer Settlement",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Mesh Implants — Transvaginal Mesh Injured Hundreds of Thousands of Women. "
            "Transvaginal surgical mesh was used to treat pelvic organ prolapse and "
            "stress urinary incontinence in hundreds of thousands of women from the "
            "1990s through 2010s. The mesh — made of polypropylene — was found to "
            "erode through vaginal tissue, causing chronic pain, infection, organ "
            "perforation, and permanent sexual dysfunction. The FDA issued safety "
            "warnings in 2008 and 2011. Several manufacturers — including Johnson & "
            "Johnson, Boston Scientific, and C.R. Bard — faced tens of thousands of "
            "lawsuits. J&J's Ethicon subsidiary settled for over $3 billion. The "
            "FDA reclassified the devices as high-risk in 2016 and ordered "
            "manufacturers to conduct post-market safety studies — studies that "
            "should have been required before approval. The mesh cases represent "
            "the largest medical device mass tort in US history — almost entirely "
            "affecting women, who were implanted with inadequately tested devices "
            "approved under a regulatory pathway that did not require clinical trials."
        ),
        "city": "New Brunswick", "state": "NJ",
        "lat": 40.4870, "lng": -74.4453,
        "date_incident": "2016-01-04",
        "violence_type": "assault",
        "status": "settled",
        "source_url": "https://www.fda.gov/medical-devices/implants-and-prosthetics/urogynecologic-surgical-mesh-implants",
        "source_name": "FDA — Urogynecologic Surgical Mesh / J&J Ethicon Settlement",
        "verified": True,
        "is_public_figure": False,
    },
]


def main():
    print("[Seed Medical Research] Seeding medical research exclusion and toxic product records...")
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
    print(f"[Seed Medical Research] {saved}/{len(RECORDS)} records saved.")
    print(f"Total in database: {get_case_count()}")


if __name__ == "__main__":
    main()
