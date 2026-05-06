#!/usr/bin/env python3
"""
seed_medical_trials.py — Birth control trials, medical experimentation
on women of color, and other documented cases of women used as test subjects.

Sources: NIH, FDA, peer-reviewed journals, congressional testimony.

Run: python3 seed_medical_trials.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    {
        "summary": (
            "Birth Control Pill Trials — First Tested on Poor Puerto Rican "
            "Women Without Full Disclosure, 1956. The first large-scale trials "
            "of the birth control pill were conducted in Puerto Rico beginning "
            "in 1956 by Gregory Pincus and John Rock — funded by Katharine "
            "McCormick and Margaret Sanger. Poor Puerto Rican women were "
            "recruited as subjects. They were not told they were in a clinical "
            "trial. They were not told the pill was experimental. They were "
            "not told about potential side effects. Three women died during "
            "the trials and their deaths were not investigated. Women who "
            "reported side effects — nausea, headaches, blood clots — were "
            "told the symptoms were psychosomatic. The pill was approved by "
            "the FDA in 1960. Puerto Rico was chosen specifically because "
            "researchers believed trials could be conducted there that would "
            "not be permitted on the US mainland — deliberately exploiting "
            "colonial status and poverty to use women's bodies as testing "
            "grounds for a drug that would primarily benefit white middle-class "
            "American women. The women who were experimented on never received "
            "acknowledgment, compensation, or apology."
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
    {
        "summary": (
            "Norplant Trials — Implantable Contraceptive Tested on Poor Women "
            "of Color, Then Coerced on Women in the US. Norplant, a "
            "long-acting implantable contraceptive, was tested extensively "
            "in developing countries — including Bangladesh, Egypt, and "
            "Indonesia — on poor women who had limited ability to refuse "
            "or have it removed. After FDA approval in 1990, judges in "
            "the US began ordering Norplant implantation as a condition "
            "of probation for women convicted of child abuse — coerced "
            "contraception as criminal punishment. At least 13 judges "
            "issued such orders. Legislators in Kansas, Louisiana, and "
            "other states proposed bills to pay welfare recipients to use "
            "Norplant. A Philadelphia Inquirer editorial suggested Norplant "
            "for poor Black women as a solution to poverty. The ACLU "
            "challenged coerced Norplant orders as unconstitutional. "
            "The pattern — testing contraception on poor women of color "
            "internationally, then coercing its use on poor women of "
            "color domestically — is a continuous thread in reproductive "
            "medicine that connects the birth control pill trials to "
            "contemporary reproductive coercion."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1991-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.aclu.org/report/norplant-bad-medicine",
        "source_name": "ACLU — Norplant: Bad Medicine / NEJM Coerced Contraception Research",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Tuskegee Syphilis Study — Impact on Black Women and Families. "
            "The US Public Health Service conducted the Tuskegee Syphilis "
            "Study from 1932 to 1972 — withholding treatment from 399 Black "
            "men with syphilis to study disease progression. While the men "
            "are the documented subjects, the impact on Black women is "
            "rarely discussed: wives and partners of the men were infected "
            "with syphilis through sexual contact — some unknowingly. "
            "Children were born with congenital syphilis. Women were not "
            "notified, not treated, and not considered in the study design. "
            "The study — exposed by journalist Jean Heller in 1972 — "
            "destroyed trust in the US medical system among Black Americans "
            "for generations. This documented distrust has been measured "
            "as a factor in lower rates of preventive care, clinical trial "
            "participation, and COVID-19 vaccination among Black Americans. "
            "The women and children harmed as collateral damage of Tuskegee "
            "have never received acknowledgment or compensation."
        ),
        "city": "Tuskegee", "state": "AL",
        "lat": 32.4299, "lng": -85.6946,
        "date_incident": "1972-07-25",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://www.cdc.gov/tuskegee/timeline.htm",
        "source_name": "CDC — Tuskegee Study Timeline / Impact on Women and Families",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Depo-Provera — Injectable Contraceptive Tested on Poor Women "
            "and Prisoners Before US Approval. Depo-Provera, an injectable "
            "contraceptive given every three months, was tested on women "
            "in developing countries and on female prisoners in the US "
            "before FDA approval. In 1978, the FDA rejected Depo-Provera "
            "citing cancer concerns in animal studies. The manufacturer, "
            "Upjohn, continued distributing it internationally — primarily "
            "in developing countries where regulatory oversight was limited. "
            "An estimated 3.5 million women in 80 countries received it "
            "during this period. The FDA finally approved Depo-Provera "
            "in 1992. Studies subsequently found it caused significant bone "
            "density loss — particularly concerning for adolescents. "
            "The FDA added a black box warning in 2004. Like Norplant, "
            "Depo-Provera was subsequently promoted for use in low-income "
            "women and women involved in the criminal justice system — "
            "continuing the pattern of testing contraception on poor women "
            "internationally, then deploying it coercively on poor women domestically."
        ),
        "city": "Silver Spring", "state": "MD",
        "lat": 38.9907, "lng": -77.0261,
        "date_incident": "1992-10-29",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.fda.gov/drugs/postmarket-drug-safety-information-patients-and-providers/depo-provera-medroxyprogesterone-acetate",
        "source_name": "FDA — Depo-Provera History / NEJM International Testing Research",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Henrietta Lacks — Black Woman's Cancer Cells Taken Without Consent, "
            "Used for Decades. Henrietta Lacks, a Black woman from Baltimore, "
            "was treated for cervical cancer at Johns Hopkins Hospital in 1951. "
            "Without her knowledge or consent, her cancer cells were harvested "
            "by researcher George Gey and distributed to laboratories worldwide. "
            "Her cells — known as HeLa cells — proved uniquely immortal in "
            "laboratory conditions and became one of the most important tools "
            "in medical research. HeLa cells have been used in the development "
            "of the polio vaccine, cancer research, HIV research, and COVID-19 "
            "vaccines. The cell line has generated billions of dollars in "
            "commercial value. Her family was never compensated, never informed "
            "for decades, and had no health insurance. She died at 31. Her "
            "case — exposed by Rebecca Skloot in 2010 — became a landmark "
            "in discussions of medical consent, racial exploitation in research, "
            "and the commercialization of human biological material. "
            "As of 2023, no legal framework requires compensation to families "
            "when biological material is commercialized."
        ),
        "city": "Baltimore", "state": "MD",
        "lat": 39.2904, "lng": -76.6122,
        "date_incident": "1951-02-08",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.hopkinsmedicine.org/henrietta-lacks",
        "source_name": "Johns Hopkins Medicine — Henrietta Lacks / The Immortal Life of Henrietta Lacks",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Vaginal Rejuvenation and Cosmetic Gynecology — Unregulated "
            "Procedures Marketed to Women. A growing industry of cosmetic "
            "gynecological procedures — including labiaplasty, vaginal "
            "rejuvenation, G-spot amplification, and laser vaginal "
            "tightening — has expanded dramatically since 2010 with "
            "minimal FDA regulation and limited evidence of safety or "
            "efficacy. The FDA has warned that energy-based devices "
            "marketed for vaginal rejuvenation have not been approved "
            "for these uses and carry risks of burns, scarring, and "
            "chronic pain. Labiaplasty — the surgical reduction of the "
            "labia — is now one of the fastest-growing cosmetic procedures "
            "in the US, with procedures increasing 217% between 2012 and "
            "2017. The majority of women seeking labiaplasty have normal "
            "anatomy. Researchers have documented that the procedures are "
            "driven by pornography-influenced beauty standards and shame "
            "about normal genital appearance. The patients are getting "
            "younger — some procedures are performed on teenagers. "
            "These are unregulated surgeries on healthy tissue, driven "
            "by manufactured insecurity about women's bodies."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2018-07-30",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.fda.gov/consumers/consumer-updates/fda-warns-against-use-energy-based-devices-perform-vaginal-rejuvenation",
        "source_name": "FDA — Warning on Vaginal Rejuvenation Devices 2018 / ACOG Statement",
        "verified": True,
        "is_public_figure": False,
    },
]


def main():
    print("[Seed Medical Trials] Seeding birth control trials and medical experimentation records...")
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
    print(f"[Seed Medical Trials] {saved}/{len(RECORDS)} records saved.")
    print(f"Total in database: {get_case_count()}")


if __name__ == "__main__":
    main()
