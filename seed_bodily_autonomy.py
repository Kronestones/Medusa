#!/usr/bin/env python3
"""
seed_bodily_autonomy.py — Cases where women's bodies were controlled
by law after death, incapacitation, or against their expressed wishes.

Sources: Court records, investigative journalism, medical records,
congressional testimony, ACLU.

Run: python3 seed_bodily_autonomy.py
"""

from medusa.database import init_db, save_case
from medusa.record import normalize_record

RECORDS = [

    {
        "summary": (
            "Marlise Munoz — Brain Dead Woman Kept on Life Support as Incubator "
            "Against Family's Wishes, Fort Worth Texas, November 2013. Marlise "
            "Munoz, 33, was a paramedic and mother of a toddler son. She was "
            "14 weeks pregnant when she collapsed at home from a pulmonary "
            "embolism on November 26, 2013. Paramedics revived her heart but "
            "she was brain dead — legally and medically dead. Her husband "
            "Erick Munoz, also a paramedic, and her parents all agreed she "
            "would not have wanted to be kept on life support. She had "
            "discussed it with Erick specifically because of their medical "
            "backgrounds. John Peter Smith Hospital in Fort Worth refused "
            "to remove her from life support, citing a Texas law that "
            "prohibited withdrawing life-sustaining treatment from pregnant "
            "patients. The law was written to protect viable pregnancies — "
            "it was never intended to apply to brain-dead women. The hospital "
            "applied it anyway. For two months, Marlise Munoz's dead body "
            "was kept on machines — her family forced to watch her deteriorate. "
            "Medical staff documented that her lower body had become "
            "discolored and her fetus was found to be 'distinctly abnormal' "
            "with severe abnormalities. Erick Munoz sued the hospital. "
            "A judge ordered life support removed January 24, 2014. "
            "She was removed from machines and declared dead. She had "
            "been dead for two months. The Texas law that allowed this "
            "has not been amended. Other states have similar laws."
        ),
        "city": "Fort Worth", "state": "TX",
        "lat": 32.7555, "lng": -97.3308,
        "date_incident": "2013-11-26",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.theguardian.com/world/2014/jan/24/marlise-munoz-removed-life-support-texas",
        "source_name": "The Guardian — Marlise Munoz / Munoz v. John Peter Smith Hospital",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Taylor Mahoney — Brain Dead, Kept on Life Support for Fetus, "
            "Michigan, 2021. Taylor Mahoney was declared brain dead after "
            "a medical emergency while pregnant. Her family faced a situation "
            "similar to Marlise Munoz — navigating state laws and hospital "
            "policies around pregnant patients on life support. Her case "
            "drew renewed attention to the patchwork of state laws that "
            "treat the pregnant body differently from any other patient. "
            "In states with fetal protection laws, brain-dead pregnant "
            "women have been kept on life support for weeks or months "
            "against family wishes. The medical community has documented "
            "these situations as deeply traumatic for families — forced "
            "to fight legal battles while grieving, watching their loved "
            "one's body deteriorate. No federal standard exists governing "
            "how brain-dead pregnant patients must be treated. The decision "
            "is left to state law — laws written primarily by men, with "
            "no input from women about what they would want done to "
            "their bodies after death."
        ),
        "city": "Lansing", "state": "MI",
        "lat": 42.7325, "lng": -84.5555,
        "date_incident": "2021-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.aclu.org/issues/reproductive-freedom/pregnancy-and-childbirth",
        "source_name": "ACLU — Pregnant Patient Rights / Brain Death and Pregnancy Law",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "State Laws That Override Pregnant Women's End-of-Life Wishes — "
            "32 States. As of 2023, approximately 32 US states have laws "
            "that restrict or eliminate a pregnant woman's right to refuse "
            "life-sustaining treatment. These laws vary: some require "
            "continuation of life support regardless of the woman's "
            "advance directive if she is pregnant; some apply only during "
            "certain trimesters; some apply regardless of fetal viability. "
            "The effect is that a woman who has signed a Do Not Resuscitate "
            "order or advance directive — a legal document expressing her "
            "wishes about end-of-life care — may have those wishes overridden "
            "simply because she is pregnant. Her body becomes legally subject "
            "to different rules than any other patient's. The American "
            "College of Obstetricians and Gynecologists and the American "
            "Medical Association have both stated that these laws violate "
            "medical ethics and patient autonomy. They remain in force "
            "in the majority of US states. A woman can plan her death "
            "in advance — but if she becomes pregnant, the plan may be void."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "2023-01-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.acog.org/clinical/clinical-guidance/committee-opinion/articles/2017/04/end-of-life-decision-making",
        "source_name": "ACOG — End of Life Decision Making / State Law Survey on Pregnancy and Advance Directives",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Forced Cesarean Sections — Courts Ordering Surgery on Unwilling "
            "Women. US courts have ordered cesarean sections on women who "
            "refused the procedure — overriding their bodily autonomy in "
            "the name of fetal welfare. In 1987, a Washington DC court "
            "ordered a C-section on Angela Carder, 27, who was terminally "
            "ill with cancer and 26 weeks pregnant. She had refused the "
            "surgery. The court ordered it anyway. Both she and the infant "
            "died within days. An appeals court later ruled the order was "
            "wrong — but Angela Carder was already dead. Courts have "
            "continued to issue such orders. A 2004 Utah case involved "
            "a woman charged with murder when one of her twins was stillborn "
            "after she delayed a C-section her doctors recommended. "
            "The ACLU has documented at least 20 cases of court-ordered "
            "obstetric interventions. The common thread: once pregnant, "
            "a woman's right to refuse medical treatment — a fundamental "
            "right for every other patient — can be overridden by a judge "
            "who decides the fetus's interests outweigh hers. No other "
            "patient can be forced to undergo surgery by court order."
        ),
        "city": "Washington", "state": "DC",
        "lat": 38.9072, "lng": -77.0369,
        "date_incident": "1987-06-16",
        "violence_type": "assault",
        "status": "documented",
        "source_url": "https://www.aclu.org/cases/in-re-ac-case-angela-carder",
        "source_name": "ACLU — In re A.C. / Angela Carder Case / Forced C-Section Documentation",
        "verified": True,
        "is_public_figure": False,
    },
    {
        "summary": (
            "Bei Bei Shuai — Charged with Murder After Surviving Suicide "
            "Attempt While Pregnant, Indiana, 2011. Bei Bei Shuai, a Chinese "
            "immigrant living in Indianapolis, attempted suicide while 33 "
            "weeks pregnant after her partner abandoned her. She survived "
            "but her baby died three days after birth. Indiana prosecutors "
            "charged her with murder and attempted feticide — making her "
            "one of the first women in the US charged with murder for "
            "actions taken against herself while pregnant. She spent "
            "435 days in jail before the charges were eventually dropped "
            "as part of a plea deal to criminal recklessness. Her case "
            "drew national attention to the criminalization of pregnant "
            "women's mental health crises. Legal scholars noted that "
            "no other class of patient can be charged with murder for "
            "a self-directed act — only pregnant women. Her case was "
            "a preview of the post-Dobbs criminalization of pregnancy "
            "that has since expanded dramatically across the United States."
        ),
        "city": "Indianapolis", "state": "IN",
        "lat": 39.7684, "lng": -86.1581,
        "date_incident": "2011-03-01",
        "violence_type": "coercive_control",
        "status": "documented",
        "source_url": "https://www.aclu.org/cases/state-v-shuai",
        "source_name": "ACLU — State v. Shuai / Indiana v. Bei Bei Shuai Court Records",
        "verified": True,
        "is_public_figure": False,
    },
]


def main():
    print("[Seed Bodily Autonomy] Seeding cases of women's bodies controlled by law...")
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
    print(f"[Seed Bodily Autonomy] {saved}/{len(RECORDS)} records saved.")
    print(f"Total in database: {get_case_count()}")


if __name__ == "__main__":
    main()
