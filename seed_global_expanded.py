"""
seed_global_expanded.py — Medusa

Global tab expansion:
  - Montreal Massacre — 14 named victims, December 6, 1989 (Canada)
  - Sophie Lancaster — murdered for being different, UK, 2007
  - Comfort Women — Japanese military sexual slavery 1931–1945
  - Rape of Nanjing — 1937, China
  - UN Women 2024 global femicide statistics
  - Ni Una Menos — Argentina / Latin America, born 2015
  - Chiara Páez — the murder that sparked Ni Una Menos
  - Latin America femicide rates
  - Susana Chávez — Mexican poet who coined "Ni Una Menos", killed 2011

All records flagged tab="global" with appropriate country fields.

Run:
    cd ~/medusa && python3 seed_global_expanded.py
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from medusa.database import init_db, save_case

CASES = [

    # ══════════════════════════════════════════════════════════════════════════
    # MONTREAL MASSACRE — Overview
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "montreal_massacre_overview_canada_1989",
        "violence_type":  "homicide",
        "status":         "convicted",
        "summary": (
            "On December 6, 1989, Marc Lépine, 25, entered the École Polytechnique "
            "engineering school at the Université de Montréal armed with a "
            "legally purchased Ruger Mini-14 semi-automatic rifle and a hunting "
            "knife. He moved through the building for just under 20 minutes, "
            "systematically separating women from men and targeting women. "
            "In a mechanical engineering classroom he ordered the men to leave, "
            "separated nine women, and shouted: 'You are all a bunch of feminists, "
            "and I hate feminists!' before opening fire. He killed 14 women and "
            "wounded 14 others before shooting himself. "
            "In his suicide note, Lépine blamed feminists for ruining his life "
            "and included a hit list of 19 prominent Canadian women — including "
            "journalist Francine Pelletier — whom he had also planned to kill. "
            "He had applied to the engineering school and been rejected. "
            "It was Canada's deadliest mass shooting at the time. "
            "The massacre triggered a national debate that was immediately and "
            "deliberately suppressed by politicians and some media commentators "
            "who called Lépine a 'madman' acting alone — a framing that erased "
            "the explicitly political, anti-feminist nature of the attack. "
            "Survivors and women's advocates fought back, insisting it be "
            "recognized as what it was: a targeted act of mass femicide. "
            "The massacre directly led to Canada's Coalition for Gun Control and "
            "the 1995 Firearms Act. December 6 is now Canada's National Day of "
            "Remembrance and Action on Violence Against Women. "
            "Sources: CBC News; Canadian Encyclopedia; court records."
        ),
        "city":           "Montreal",
        "state":          "DC",
        "lat":            45.5048,
        "lng":            -73.6141,
        "source_url":     "https://thecanadianencyclopedia.ca/en/article/polytechnique-tragedy",
        "source_name":    "The Canadian Encyclopedia",
        "additional_sources": [
            {"url": "https://www.cbc.ca/news/fifthestate/francine-pelletier-montreal-massacre-1.7401282",
             "name": "CBC News — Francine Pelletier"},
            {"url": "https://femicideincanada.ca/what-is-femicide/history/montreal-massacre/",
             "name": "Femicide in Canada"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1989-12-06",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # MONTREAL MASSACRE — 14 Named Victims
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "montreal_massacre_named_victims_1989",
        "violence_type":  "homicide",
        "status":         "convicted",
        "summary": (
            "The 14 women murdered by Marc Lépine at École Polytechnique, "
            "Montreal, on December 6, 1989: "
            "Geneviève Bergeron, 21, civil engineering student; "
            "Hélène Colgan, 23, mechanical engineering student; "
            "Nathalie Croteau, 23, mechanical engineering student; "
            "Barbara Daigneault, 22, mechanical engineering student; "
            "Anne-Marie Edward, 21, chemical engineering student; "
            "Maud Haviernick, 29, materials engineering student; "
            "Barbara Klucznik-Widajewicz, 31, nursing student; "
            "Maryse Laganière, 25, budget clerk in the financial department; "
            "Maryse Leclair, 23, materials engineering student; "
            "Anne-Marie Lemay, 22, mechanical engineering student; "
            "Sonia Pelletier, 23, mechanical engineering student; "
            "Michèle Richard, 21, materials engineering student; "
            "Annie St-Arneault, 23, mechanical engineering student; "
            "Annie Turcotte, 21, materials engineering student. "
            "Ten other women and four men were injured. "
            "Lépine then killed himself. "
            "These women were studying engineering at a time when women were "
            "just beginning to enter the field in significant numbers. Lépine "
            "targeted them specifically because they were women doing so. "
            "Their names are read aloud every December 6 across Canada."
        ),
        "city":           "Montreal",
        "state":          "DC",
        "lat":            45.5048,
        "lng":            -73.6141,
        "source_url":     "https://acelebrationofwomen.org/2011/12/the-montreal-massacre-december-6-1989/",
        "source_name":    "A Celebration of Women / CBC Archives",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1989-12-06",
        "tab":            "global",
        "country":        "Canada",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SOPHIE LANCASTER — murdered for being different, UK, 2007
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "sophie_lancaster_bacup_uk_2007",
        "violence_type":  "homicide",
        "status":         "convicted",
        "summary": (
            "Sophie Louise Lancaster, 20, was beaten to death in Stubbylee Park "
            "in Bacup, Lancashire, England, in the early hours of August 11, 2007. "
            "She and her boyfriend Robert Maltby, 21, were attacked by a group "
            "of five teenage boys — the youngest 15, the oldest 17 — solely "
            "because Sophie and Robert were goths and dressed differently. "
            "The attack began on Robert. When Sophie threw herself over him to "
            "protect him, the boys turned on her, stamping on her head while "
            "she was curled around him. The attackers later bragged to friends: "
            "'There's two moshers nearly dead up Bacup park — you wanna see "
            "them — they're a right mess.' "
            "Both were taken to hospital in comas. Robert eventually recovered. "
            "Sophie's injuries were so severe she never regained consciousness. "
            "She was taken off life support on August 24, 2007, thirteen days "
            "after the attack. She was a vegetarian, a pacifist, and planned to "
            "study English. She had hoped to become a journalist or youth worker. "
            "Ryan Herbert, 16, pleaded guilty to murder and was sentenced to "
            "life with a minimum of 16 years. Brendan Harris, 15, was convicted "
            "of murder and sentenced to life with a minimum of 18 years. The "
            "other three received sentences of 4–6 years for grievous bodily harm. "
            "Sophie's mother Sylvia Lancaster founded the Sophie Lancaster "
            "Foundation, which campaigns against hate crime targeting people "
            "from alternative subcultures and has worked to have such hatred "
            "recognized in UK hate crime legislation. In 2013, Greater Manchester "
            "Police became the first force in the UK to record attacks on goths, "
            "emos, and punks as hate crimes, directly as a result of the "
            "Foundation's advocacy. "
            "Robert Maltby, who survived, is now an illustrator and artist. "
            "He has spoken publicly about the attack only rarely, describing "
            "how difficult it has been to have Sophie reduced to an archetype "
            "when to him she was simply the person he loved — 'Did you ever eat "
            "a meal with her? Did you know how she took her coffee?' "
            "Sources: Lancashire Police; The Guardian; National World; "
            "Sophie Lancaster Foundation."
        ),
        "city":           "Bacup",
        "state":          "DC",
        "lat":            53.7067,
        "lng":            -2.1984,
        "source_url":     "https://www.sophielandcasterfoundation.com/",
        "source_name":    "Sophie Lancaster Foundation",
        "additional_sources": [
            {"url": "https://www.nationalworld.com/news/crime/sophie-lancaster-murder-killer-ryan-herbert-what-happened-to-her-boyfriend-robert-maltby-3615626",
             "name": "National World"},
            {"url": "https://www.crimeandinvestigation.co.uk/articles/murdered-being-different-sophies-story",
             "name": "Crime + Investigation UK"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2007-08-11",
        "tab":            "global",
        "country":        "United Kingdom",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # COMFORT WOMEN — Japanese military sexual slavery 1931–1945
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "comfort_women_japan_wwii_1931_1945",
        "violence_type":  "trafficking",
        "status":         "congressional_record",
        "summary": (
            "Between 1931 and 1945, the Imperial Japanese Army systematically "
            "trafficked between 50,000 and 200,000 women and girls — some "
            "estimates reach higher — into a state-run system of sexual slavery "
            "euphemistically called 'comfort stations.' The vast majority, "
            "approximately 80%, were Korean; others came from China, Taiwan, "
            "the Philippines, Indonesia, Vietnam, Thailand, the Dutch East "
            "Indies, and other occupied territories. Most were teenagers from "
            "poor rural families, taken from their homes at gunpoint, lured "
            "with false promises of factory work or nursing jobs, or abducted "
            "while travelling. "
            "Once enslaved, women were forced to service between 5 and 60 "
            "Japanese soldiers per day in makeshift military brothels. The "
            "fatality rate was approximately 87% — compared to 27% for "
            "front-line Japanese combat soldiers. Girls as young as 12 were "
            "among the victims. "
            "Japan formally denied the existence of comfort stations until "
            "1991, when Korean survivor Kim Hak-soon became the first woman "
            "to speak publicly. Within weeks, 250 other survivors came forward. "
            "In 1993 the Kono Statement partially acknowledged the military's "
            "role, but Japan has never fully accepted legal responsibility. "
            "A 2015 settlement offered reparations to Korean survivors, but "
            "survivors and advocates rejected it as insufficient and lacking "
            "a genuine apology. As of 2026, fewer than a dozen known survivors "
            "remain alive. "
            "Survivor Lee Ok-seon, taken at 14 from Busan in 1943, was forced "
            "to service soldiers in occupied China. She testified: 'I never "
            "wanted to give comfort to those men. I don't want to hate or hold "
            "a grudge, but I can never forgive what happened to me.' "
            "The comfort women system constitutes one of the largest documented "
            "cases of state-organized human trafficking and sexual slavery in "
            "the 20th century. "
            "Sources: Britannica; Columbia Law Korean Legal Studies; "
            "Remember Comfort Women Foundation; SMU Embrey Human Rights Program."
        ),
        "city":           "Seoul",
        "state":          "DC",
        "lat":            37.5665,
        "lng":            126.9780,
        "source_url":     "https://kls.law.columbia.edu/content/military-sexual-slavery-1931-1945",
        "source_name":    "Columbia Law — Korean Legal Studies",
        "additional_sources": [
            {"url": "https://www.britannica.com/topic/comfort-women",
             "name": "Britannica"},
            {"url": "https://remembercomfortwomen.org/history-background/comfort-women-the-unresolved-history/",
             "name": "Remember Comfort Women Foundation"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1931-01-01",
        "tab":            "global",
        "country":        "Korea / Japan (Imperial)",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # RAPE OF NANJING — December 1937, China
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "rape_of_nanjing_china_1937",
        "violence_type":  "sexual_assault",
        "status":         "congressional_record",
        "summary": (
            "During a six-week period beginning December 13, 1937, Japanese "
            "Imperial Army troops occupied Nanjing — then the capital of "
            "Nationalist China — and committed systematic mass atrocities "
            "against the civilian population. Between 20,000 and 80,000 women "
            "and girls were raped, many of them killed afterward. An estimated "
            "200,000 to 300,000 civilians were killed in total. "
            "The sexual violence was systematic and ordered: Japanese soldiers "
            "conducted house-to-house searches for women, abducted them from "
            "refugee camps and from the protection of the International Safety "
            "Zone, and gang-raped and murdered women of all ages including "
            "elderly women and young girls. Women were forced into sexual "
            "slavery at military 'comfort stations' established in the city. "
            "The International Military Tribunal for the Far East (Tokyo War "
            "Crimes Tribunal) convicted Japanese General Iwane Matsui and "
            "diplomat Hirota Koki for failing to prevent the atrocities; "
            "both were executed. "
            "Like the comfort women system, the Rape of Nanjing has been a "
            "subject of ongoing historical denial and minimization by Japanese "
            "nationalist politicians, making it a continuing source of tension "
            "between Japan and China. "
            "Sources: IMTFE records; Iris Chang, The Rape of Nanking (1997); "
            "Yale Divinity School — Yale-China digitized documents."
        ),
        "city":           "Nanjing",
        "state":          "DC",
        "lat":            32.0603,
        "lng":            118.7969,
        "source_url":     "https://library.uca.edu/asianstudiesresources/comfortwomen",
        "source_name":    "International Military Tribunal for the Far East records",
        "additional_sources": [
            {"url": "https://divinity-adhoc.library.yale.edu/nanjing/",
             "name": "Yale Divinity School — Nanjing Documents"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1937-12-13",
        "tab":            "global",
        "country":        "China / Japan (Imperial)",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # UN WOMEN 2024 — Global femicide statistics
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "stat_unwomen_2024_global_femicide",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "UN Women and UNODC joint report, released November 25, 2025 "
            "(International Day for the Elimination of Violence Against Women), "
            "covering 2024 global femicide data: "
            "83,000 women and girls were intentionally killed worldwide in 2024. "
            "Of these, approximately 50,000 — 60% — were killed by an intimate "
            "partner or family member. This equals 137 women and girls killed "
            "every single day by someone in their own family, or one every "
            "10 minutes. By contrast, only 11% of male homicides are committed "
            "by intimate partners or family members. "
            "By region, raw numbers: Africa 22,600; Asia 17,400; Americas 7,700; "
            "Europe 2,100; Oceania 300. "
            "By rate per 100,000 female population: Africa 3.0 (highest); "
            "Americas 1.5; Oceania 1.4; Asia 0.7; Europe 0.5. "
            "In Europe specifically, 64% of all women killed were murdered by "
            "intimate partners — the highest proportion globally. "
            "The report notes a critical accountability gap: fewer countries "
            "are reporting femicide statistics over time, not more. Every "
            "victim must be counted to strengthen prevention and ensure justice. "
            "The observed slight decrease from 2023 (51,100) to 2024 (50,000) "
            "is attributed to data gaps and does not reflect a genuine reduction. "
            "Source: UN Women / UNODC, Femicides in 2024: Global Estimates, "
            "November 25, 2025."
        ),
        "city":           "New York",
        "state":          "NY",
        "lat":            40.7128,
        "lng":            -74.0060,
        "source_url":     "https://www.unwomen.org/en/digital-library/publications/2025/11/femicides-in-2024-global-estimates-of-intimate-partner-family-member-femicides",
        "source_name":    "UN Women / UNODC — Femicides in 2024",
        "additional_sources": [
            {"url": "https://www.unodc.org/unodc/en/press/releases/2025/November/137-women-and-girls-killed-every-day-by-intimate-partners-or-family-members-in-2024.html",
             "name": "UNODC Press Release"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2025-11-25",
        "tab":            "global",
        "country":        "Global",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # CHIARA PÁEZ — the murder that sparked Ni Una Menos
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "chiara_paez_argentina_2015",
        "violence_type":  "homicide",
        "status":         "convicted",
        "summary": (
            "Chiara Páez, 14 years old and a few weeks pregnant, was beaten "
            "to death by her 16-year-old boyfriend Manuel Mansilla on or "
            "around May 10, 2015, in Rufino, Santa Fe province, Argentina. "
            "Chiara wanted to keep the baby. Mansilla did not. He beat her "
            "to death and buried her body in the garden of his family's home. "
            "Her body was found by police dogs. "
            "Mansilla was convicted of femicide. "
            "On May 11, 2015, radio journalist Marcela Ojeda posted a single "
            "tweet about Chiara's murder that launched what became the Ni Una "
            "Menos movement: 'Women actors, politicians, artists, entrepreneurs, "
            "social activists… all women, are we not going to raise our voice? "
            "THEY ARE KILLING US.' Within two and a half hours, the June 3 "
            "march had been organized. On June 3, 2015, more than 200,000 "
            "people flooded the streets of Buenos Aires alone — and hundreds "
            "of thousands more across 120 cities in Argentina — demanding an "
            "end to femicide. Chiara's murder became the spark that ignited "
            "a movement that has since spread across Latin America, Europe, "
            "and the world. As of 2025, 2,827 femicides have been recorded in "
            "Argentina since the first Ni Una Menos march — one every 31 hours. "
            "Sources: Buenos Aires Herald; NPR; Wikipedia."
        ),
        "city":           "Rufino",
        "state":          "DC",
        "lat":            -34.2667,
        "lng":            -62.7000,
        "source_url":     "https://buenosairesherald.com/society/ten-years-of-ni-una-menos-how-one-tweet-led-to-a-global-phenomenon",
        "source_name":    "Buenos Aires Herald",
        "additional_sources": [
            {"url": "https://www.npr.org/2021/10/15/1043908435/how-niunamenos-grew-from-the-streets-of-argentina-into-a-regional-womens-movemen",
             "name": "NPR"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2015-05-10",
        "tab":            "global",
        "country":        "Argentina",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # NI UNA MENOS — Movement overview
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "ni_una_menos_movement_argentina_2015",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "Ni Una Menos ('Not One Woman Less') is a Latin American feminist "
            "movement born in Argentina on June 3, 2015, sparked by the femicide "
            "of 14-year-old Chiara Páez. The first march drew more than 200,000 "
            "people in Buenos Aires alone, with hundreds of thousands more across "
            "120 Argentine cities. The movement rapidly spread to Mexico, Chile, "
            "Peru, Colombia, Uruguay, Brazil, and later to Spain and other "
            "European countries. "
            "The phrase 'Ni Una Menos' was originally coined by Mexican poet "
            "and activist Susana Chávez Castillo as 'Ni una mujer menos, ni una "
            "muerte más' ('Not one woman less, not one more death') to protest "
            "the femicides in Ciudad Juárez. Chávez herself was tortured and "
            "killed in 2011. "
            "Latin America has 14 of the 25 countries with the highest femicide "
            "rates in the world. At least 11 women are killed by gender-based "
            "violence every day across Latin America and the Caribbean. In "
            "Argentina alone, a femicide occurs every 31 hours. "
            "The movement has contributed to significant legislative change: "
            "Argentina's 2018 Micaela Law mandated gender violence training "
            "for all public officials; the 2020 legalization of abortion up "
            "to 14 weeks was directly connected to movement organizing. "
            "Between June 3, 2015 and May 25, 2025 — the movement's 10th "
            "anniversary — 2,827 femicides were recorded in Argentina. "
            "Sources: Buenos Aires Herald; Wikipedia; UN Women; NPR."
        ),
        "city":           "Buenos Aires",
        "state":          "DC",
        "lat":            -34.6037,
        "lng":            -58.3816,
        "source_url":     "https://buenosairesherald.com/society/ten-years-of-ni-una-menos-how-one-tweet-led-to-a-global-phenomenon",
        "source_name":    "Buenos Aires Herald",
        "additional_sources": [
            {"url": "https://en.wikipedia.org/wiki/Ni_una_menos",
             "name": "Wikipedia — Ni Una Menos"},
            {"url": "https://wafmag.org/2015/11/femicide-in-argentina/",
             "name": "Women Across Frontiers Magazine"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2015-06-03",
        "tab":            "global",
        "country":        "Argentina",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # SUSANA CHÁVEZ — Mexican poet who coined "Ni Una Menos", killed 2011
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "susana_chavez_ciudad_juarez_mexico_2011",
        "violence_type":  "homicide",
        "status":         "reported",
        "summary": (
            "Susana Chávez Castillo was a Mexican poet and activist from "
            "Ciudad Juárez, Chihuahua — one of the most dangerous cities in "
            "the world for women — where over 400 women had been murdered since "
            "the 1990s in a pattern of femicide linked to cartel impunity and "
            "state indifference. In the early 2000s, Chávez coined the phrase "
            "'Ni una mujer menos, ni una muerte más' ('Not one woman less, not "
            "one more death') in her poetry and public performances to protest "
            "the killings and demand accountability. "
            "In January 2011, Susana Chávez Castillo was murdered in Ciudad "
            "Juárez. She was 36 years old. Her body was found with her hand cut "
            "off — a calling card associated with organized crime in the region. "
            "Her killing was attributed to gang members. No one was held "
            "accountable. "
            "Her phrase 'Ni Una Menos' was later adopted by Argentine organizers "
            "in 2015 as the name of the movement that would sweep Latin America "
            "and the world. The woman who first gave a name to the demand that "
            "women stop being killed was herself killed, and the phrase lived on "
            "without her. "
            "Sources: Wikipedia — Ni Una Menos; Grokipedia; DAWN Feminist."
        ),
        "city":           "Ciudad Juárez",
        "state":          "DC",
        "lat":            31.6904,
        "lng":            -106.4245,
        "source_url":     "https://grokipedia.com/page/Ni_una_menos",
        "source_name":    "Grokipedia / DAWN Feminist",
        "verified":       True,
        "is_public_figure": True,
        "date_incident":  "2011-01-01",
        "tab":            "global",
        "country":        "Mexico",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # CIUDAD JUÁREZ FEMICIDES — systemic overview
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "ciudad_juarez_femicides_mexico_1990s",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "Ciudad Juárez, Chihuahua, Mexico, on the US border directly across "
            "from El Paso, Texas, became the global symbol of endemic femicide "
            "beginning in the early 1990s. Since 1993, hundreds of women — "
            "estimates range from 400 to over 1,000 — have been murdered in "
            "and around the city, with hundreds more disappeared. Victims are "
            "disproportionately young, poor, Indigenous, and employed in the "
            "maquiladora (factory) sector. Many bodies have been found in the "
            "desert bearing signs of sexual torture. "
            "Investigations have been chronically inadequate. Police repeatedly "
            "blamed the victims, dismissed their families, and closed cases "
            "without suspects. Evidence was lost or destroyed. Some investigators "
            "believe multiple perpetrators are responsible including serial "
            "killers, organized crime networks, and local officials. "
            "In 2001, eight women's bodies were found in a cotton field in the "
            "city — the Campo Algodonero case. In 2009, the Inter-American Court "
            "of Human Rights ruled that Mexico had violated the human rights of "
            "the victims and their families through its failure to investigate, "
            "and ordered the Mexican government to pay reparations, acknowledge "
            "state responsibility, and implement systemic reforms. "
            "The femicides in Juárez inspired Susana Chávez to coin 'Ni Una "
            "Menos' in the early 2000s and directly influenced the global "
            "movement that bears that name. "
            "Sources: Inter-American Court of Human Rights, Campo Algodonero "
            "v. Mexico (2009); Amnesty International; Washington Office on "
            "Latin America."
        ),
        "city":           "Ciudad Juárez",
        "state":          "DC",
        "lat":            31.6904,
        "lng":            -106.4245,
        "source_url":     "https://www.corteidh.or.cr/docs/casos/articulos/seriec_205_ing.pdf",
        "source_name":    "Inter-American Court of Human Rights — Campo Algodonero v. Mexico (2009)",
        "additional_sources": [
            {"url": "https://www.amnesty.org/en/location/americas/north-america/mexico/report-mexico/",
             "name": "Amnesty International — Mexico"},
        ],
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "1993-01-01",
        "tab":            "global",
        "country":        "Mexico",
    },

    # ══════════════════════════════════════════════════════════════════════════
    # LATIN AMERICA — Regional femicide statistics
    # ══════════════════════════════════════════════════════════════════════════

    {
        "case_id":        "stat_latin_america_femicide_rates",
        "violence_type":  "homicide",
        "status":         "congressional_record",
        "summary": (
            "Latin America and the Caribbean has the highest femicide rates "
            "in the world outside of Africa. Key statistics: "
            "14 of the 25 countries with the highest rates of gender-based "
            "violence are in Latin America. "
            "At least 11 women are victims of femicide every day across the "
            "region, according to a 2024 UN Women press release. "
            "In Argentina, a femicide occurs every 31 hours — 2,827 recorded "
            "between 2015 and 2025. "
            "In Mexico, an average of 10 women are killed per day; femicide "
            "was codified as a specific criminal offense in 2012 but prosecutions "
            "remain rare. In 2020, feminist activists painted the names of "
            "femicide victims on the walls of the National Palace in Mexico "
            "City in protest of government inaction. "
            "Bolivia has the highest femicide rate per capita in Latin America. "
            "Brazil records approximately 1,400 femicides per year. "
            "The primary age group targeted is young women aged 15 to 29. "
            "Many countries in the region codified femicide as a specific "
            "crime only in the 2010s — before that, killings of women by "
            "intimate partners were routinely classified as 'crimes of passion' "
            "with reduced sentences. "
            "Sources: UN Women; ECLAC; Ni Una Menos movement data; "
            "Buenos Aires Herald 10th anniversary report."
        ),
        "city":           "Buenos Aires",
        "state":          "DC",
        "lat":            -34.6037,
        "lng":            -58.3816,
        "source_url":     "https://www.unwomen.org/en/digital-library/publications/2025/11/femicides-in-2024-global-estimates-of-intimate-partner-family-member-femicides",
        "source_name":    "UN Women / ECLAC",
        "verified":       True,
        "is_public_figure": False,
        "date_incident":  "2024-01-01",
        "tab":            "global",
        "country":        "Latin America",
    },

]


def main():
    print("\n  [Medusa] Seeding global expanded records...\n")
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
    print("  NOTE: All records use state='DC' as placeholder for non-US cases.")
    print("  Real coordinates are accurate. tab='global' is set on all records.\n")


if __name__ == "__main__":
    main()
