"""
seed_global.py — Documented cases of male violence against women and children
internationally. All from public record, court documents, and verified
investigative journalism.
"""
import os
import sys
sys.path.insert(0, os.path.expanduser("~/medusa"))

from medusa.database import init_db, save_case
from medusa.record import normalize_record, make_case_id

CASES = [
    {
        "summary": "École Polytechnique Massacre — Montreal, Canada, December 6, 1989. Marc Lépine entered the École Polytechnique engineering school in Montreal and systematically murdered 14 women, injuring 10 more women and 4 men. Before opening fire he separated the men from the women, shouting 'I hate feminists.' He left a suicide note blaming feminists for ruining his life. The massacre is the deadliest mass killing of women in Canadian history and is commemorated annually as the National Day of Remembrance and Action on Violence Against Women.",
        "city": "Montreal, Canada", "state": "DC",
        "date_incident": "1989-12-06",
        "violence_type": "homicide",
        "status": "reported",
        "source_url": "https://www.thecanadianencyclopedia.ca/en/article/ecole-polytechnique-massacre",
        "source_name": "Canadian Encyclopedia — École Polytechnique Massacre",
        "verified": True,
    },
    {
        "summary": "Delhi Gang Rape — India, December 16, 2012. Jyoti Singh, 23, a medical student, was gang raped and fatally assaulted on a bus in New Delhi by six men. She died from her injuries 13 days later. The case triggered massive protests across India and internationally. Four men were convicted and executed. The case led to significant reforms in Indian rape law. The brutal nature of the attack and the victim's death sparked a global conversation about violence against women.",
        "city": "New Delhi, India", "state": "DC",
        "date_incident": "2012-12-16",
        "violence_type": "rape",
        "status": "convicted",
        "source_url": "https://www.bbc.com/news/world-asia-india-16698860",
        "source_name": "BBC — Delhi Gang Rape / Indian Supreme Court Records",
        "verified": True,
    },
    {
        "summary": "Savita Halappanavar — Ireland, October 28, 2012. Savita Halappanavar, 31, died of sepsis at University Hospital Galway after being denied a life-saving abortion while miscarrying. Doctors cited Ireland's constitutional ban on abortion as the reason for refusal. Her death triggered international outrage and a decade-long campaign that led to the repeal of Ireland's Eighth Amendment in 2018. Her case is one of the most documented examples of how abortion bans directly kill women.",
        "city": "Galway, Ireland", "state": "DC",
        "date_incident": "2012-10-28",
        "violence_type": "homicide",
        "status": "reported",
        "source_url": "https://www.bbc.com/news/world-europe-20522567",
        "source_name": "BBC — Savita Halappanavar / Irish Coroner's Inquest",
        "verified": True,
    },
    {
        "summary": "Sophie Lancaster — UK, August 11, 2007. Sophie Lancaster, 20, and her boyfriend Robert Maltby were attacked in a park in Stupalee, Lancashire, England by a gang of teenagers who targeted them because of their gothic appearance. Sophie died from her injuries 13 days later. Two teenagers were convicted of murder. The Sophie Lancaster Foundation was established to combat hate crime against people from alternative subcultures. Her case led to changes in UK hate crime legislation.",
        "city": "Stupalee, England", "state": "DC",
        "date_incident": "2007-08-11",
        "violence_type": "homicide",
        "status": "convicted",
        "source_url": "https://www.sophielancasterfoundation.com/about/sophies-story/",
        "source_name": "Sophie Lancaster Foundation — Sophie Lancaster Murder 2007",
        "verified": True,
    },
    {
        "summary": "Ciudad Juárez Femicides — Mexico, 1993–present. Since 1993, hundreds of women and girls have been murdered in Ciudad Juárez, Mexico in what became known as the first internationally recognized femicide crisis. Victims were predominantly young, poor women working in maquiladoras. Mexican authorities failed systematically to investigate. The Inter-American Court of Human Rights ruled against Mexico in 2009 in the landmark Cotton Field case, finding the state responsible for failing to protect women. The crisis drew international attention to the concept of femicide as a human rights violation.",
        "city": "Ciudad Juarez, Mexico", "state": "DC",
        "date_incident": "1993-01-01",
        "violence_type": "homicide",
        "status": "reported",
        "source_url": "https://www.corteidh.or.cr/docs/casos/articulos/seriec_205_ing.pdf",
        "source_name": "Inter-American Court of Human Rights — Cotton Field Case v. Mexico 2009",
        "verified": True,
    },
    {
        "summary": "Chibok School Girls — Nigeria, April 14, 2014. Boko Haram militants abducted 276 schoolgirls from the Government Girls Secondary School in Chibok, Borno State, Nigeria. The girls were taken in the night and many were forced into marriage with militants or converted to Islam under duress. As of 2023, over 100 girls remain missing. The abduction sparked the global #BringBackOurGirls campaign and highlighted Boko Haram's systematic targeting of girls seeking education.",
        "city": "Chibok, Nigeria", "state": "DC",
        "date_incident": "2014-04-14",
        "violence_type": "trafficking",
        "status": "reported",
        "source_url": "https://www.amnesty.org/en/latest/news/2014/05/nigeria-abducted-girls-boko-haram/",
        "source_name": "Amnesty International — Chibok Girls Abduction Nigeria 2014",
        "verified": True,
    },
    {
        "summary": "UK Femicide Census 2009–2023. The UK Femicide Census documents every woman killed by a man in the United Kingdom. Between 2009 and 2023, at least 1,723 women were killed by men in the UK. On average, one woman is killed by a man every three days. The majority are killed by current or former intimate partners. The Census was established by Karen Ingala Smith and Clarissa Penfold after finding no official government record of femicide existed.",
        "city": "London, England", "state": "DC",
        "date_incident": "2023-01-01",
        "violence_type": "homicide",
        "status": "reported",
        "source_url": "https://www.femicidecensus.org",
        "source_name": "UK Femicide Census 2009–2023",
        "verified": True,
    },
    {
        "summary": "Australia's National Plan to End Violence Against Women 2022–2032. Australian Institute of Health and Welfare data shows one woman is killed by a current or former partner every 9 days in Australia. Aboriginal and Torres Strait Islander women are killed at 11 times the rate of non-Indigenous women. Australia's Royal Commission into Family Violence (2016) made 227 recommendations following documented systemic failures to protect women from lethal domestic violence.",
        "city": "Canberra, Australia", "state": "DC",
        "date_incident": "2022-01-01",
        "violence_type": "homicide",
        "status": "reported",
        "source_url": "https://www.aihw.gov.au/family-domestic-and-sexual-violence",
        "source_name": "Australian Institute of Health and Welfare — Family Violence Statistics 2022",
        "verified": True,
    },
    {
        "summary": "Comfort Women — WWII Sexual Slavery by Imperial Japan. An estimated 200,000 women and girls — predominantly Korean, Chinese, Filipino, and Dutch — were forced into sexual slavery by the Imperial Japanese Army during World War II. Survivors were euphemistically called 'comfort women.' Japan's 2015 agreement with South Korea was widely criticized by survivors as inadequate. The United Nations has repeatedly called for full accountability. Surviving comfort women have testified before international tribunals documenting systematic rape as a weapon of war.",
        "city": "Seoul, South Korea", "state": "DC",
        "date_incident": "1945-09-02",
        "violence_type": "trafficking",
        "status": "reported",
        "source_url": "https://www.ohchr.org/en/special-procedures/sr-violence-against-women/comfort-women",
        "source_name": "UN Human Rights Council — Comfort Women Report / Korean Council for Justice",
        "verified": True,
    },
    {
        "summary": "WHO Global Report on Violence Against Women — 2021. The World Health Organization's landmark study found that globally 1 in 3 women — approximately 736 million — have experienced physical or sexual violence by an intimate partner or sexual violence from a non-partner. Rates are highest in low-income countries but the epidemic spans every nation. Intimate partner violence accounts for 38% of all murders of women globally. The report calls male violence against women a global public health crisis.",
        "city": "Geneva, Switzerland", "state": "DC",
        "date_incident": "2021-03-09",
        "violence_type": "domestic_violence",
        "status": "reported",
        "source_url": "https://www.who.int/publications/i/item/9789240022256",
        "source_name": "WHO — Global Report on Violence Against Women 2021",
        "verified": True,
    },
    {
        "summary": "Iran — Mahsa Amini and the Woman Life Freedom Movement, 2022. Mahsa Amini, 22, died on September 16, 2022 in the custody of Iran's morality police after being arrested for allegedly wearing her hijab improperly. Her death triggered the largest protests in Iran since the 1979 revolution under the slogan 'Woman, Life, Freedom.' At least 530 protesters were killed by security forces, including 71 children. Thousands were arrested. The movement highlighted state violence against women enforcing compulsory dress codes.",
        "city": "Tehran, Iran", "state": "DC",
        "date_incident": "2022-09-16",
        "violence_type": "homicide",
        "status": "reported",
        "source_url": "https://www.amnesty.org/en/latest/news/2022/09/iran-mahsa-amini/",
        "source_name": "Amnesty International — Mahsa Amini / Woman Life Freedom Movement 2022",
        "verified": True,
    },
    {
        "summary": "Afghanistan — Taliban Erasure of Women 2021–present. Following the Taliban takeover of Afghanistan in August 2021, women and girls were systematically stripped of rights including education beyond sixth grade, employment, freedom of movement, and access to healthcare without a male guardian. UN Women documented widespread domestic violence with no legal recourse. Girls' secondary schools were closed nationwide. The UN Special Rapporteur called the situation 'gender apartheid' — the most severe suppression of women's rights in the world.",
        "city": "Kabul, Afghanistan", "state": "DC",
        "date_incident": "2021-08-15",
        "violence_type": "coercive_control",
        "status": "reported",
        "source_url": "https://www.unwomen.org/en/news/stories/2021/8/explainer-the-situation-for-women-and-girls-in-afghanistan",
        "source_name": "UN Women — Afghanistan Gender Apartheid Report 2021",
        "verified": True,
    },
]


def seed():
    init_db()
    saved = 0
    skipped = 0
    for case in CASES:
        rec = normalize_record(case)
        if rec is None:
            print(f"  SKIP (normalize failed): {case.get('city')}")
            skipped += 1
            continue
        rec["case_id"] = make_case_id(
            rec["city"], rec["state"], rec["violence_type"],
            rec["date_incident"], rec.get("source_url", ""), rec.get("summary", "")
        )
        try:
            save_case(rec)
            saved += 1
            print(f"  saved: {rec['summary'][:80]}")
        except Exception as e:
            if "duplicate" in str(e).lower() or "unique" in str(e).lower():
                skipped += 1
            else:
                print(f"  ERROR: {e}")
    print(f"\nGlobal seed complete. {saved} saved, {skipped} skipped.")


if __name__ == "__main__":
    seed()
