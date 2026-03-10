#!/usr/bin/env python3
"""Register meta_title and meta_description translations for 13 Hairgenetix blog articles."""

import json
import os
import subprocess
import sys
import time

STORE = os.environ.get("SHOPIFY_STORE", "a24be5-c5.myshopify.com")
TOKEN = os.environ.get("SHOPIFY_ACCESS_TOKEN", "")
if not TOKEN:
    print("ERROR: SHOPIFY_ACCESS_TOKEN environment variable is required.", file=sys.stderr)
    sys.exit(1)
API = f"https://{STORE}/admin/api/2024-10/graphql.json"
LOCALES = ["nl", "de", "fr", "es", "it", "sv", "da", "nb"]

# Article data: resourceId -> {meta_title, meta_title_digest, meta_description, meta_description_digest}
ARTICLES = {
    "gid://shopify/Article/1001570894156": {
        "meta_title_digest": "29cb437586ef194c60112a8d37e636aebca01322e304f2203ce38bd2fea112e6",
        "meta_description_digest": "9f31663b223b736164d68a59733c260d09c43f88385dd057af6589a9bb686f55",
        "en_title": "AHK-Cu Copper Peptide Hair Growth Study (2007) — Plain-Language Summary | Hairgenetix",
        "en_desc": "Seoul National University proved copper peptide AHK-Cu stimulates hair follicle growth and protects growth cells. Read the plain-language summary of this landmark 2007 study.",
    },
    "gid://shopify/Article/1001571025228": {
        "meta_title_digest": "bbca2cfe865b06f7c05d2bfc840d16700c53bffb5aa31297380ebedac89c882b",
        "meta_description_digest": "82b252b387874fcc1ef9dd5c81220f3514e6beaa6d939ecc05cb9c1af9f5e9d9",
        "en_title": "GHK-Cu Copper Peptide Regeneration Review (2018) — Research Summary | Hairgenetix",
        "en_desc": "Plain-language summary of Pickart & Margolina's 2018 review of GHK-Cu copper peptide. Gene data shows it affects 4,000+ genes linked to tissue repair, hair growth, and anti-inflammation.",
    },
    "gid://shopify/Article/1001571057996": {
        "meta_title_digest": "76184dbb38e7883b15ba8dcbbe4a74946bfaf1868f12f181072bd60ae58d54f9",
        "meta_description_digest": "a22a77f97d6dabd62fd94ca0521e45f0bc8986382a21a6355861950cbde8c77c",
        "en_title": "Copper Peptide Microneedling Hair Regrowth Study (2025) — Research Summary | Hairgenetix",
        "en_desc": "Plain-language summary of Kuceki et al. 2025 study. 5 monthly sessions of copper peptide microneedling achieved 26.5% median hair regrowth — more than double the results of 3-session protocols.",
    },
    "gid://shopify/Article/1001571090764": {
        "meta_title_digest": "b4a4930c5ddcf20caa22115a9358473676c109d819848861df5232f5e6e47c2d",
        "meta_description_digest": "d6fd719c103bda9f372b047538181725ac82729676ec4bc8d3eb9eb115542208",
        "en_title": "GHK Peptide Hair Growth Clinical Trial (2016) — Research Summary | Hairgenetix",
        "en_desc": "Plain-language summary of Lee et al. 2016 clinical trial. 45 men used a GHK peptide complex for 6 months — the treatment group grew 52-72 extra hairs with zero side effects.",
    },
    "gid://shopify/Article/1001571123532": {
        "meta_title_digest": "d39f21308760c027b010e5bf5702533dcd98dc4d8b28b8768a9ba3125a6c5397",
        "meta_description_digest": "8e53841d286cd295b1926aafb013b6b0902ae275024b0ba81d46446791ae43b1",
        "en_title": "Microneedling for Hair Loss: Landmark Dhurat 2013 Study — Research Summary | Hairgenetix",
        "en_desc": "Plain-language summary of Dhurat et al. 2013 — the study that proved microneedling works for hair loss. 100 patients, 4x more hair growth vs minoxidil alone. 82% reported >50% improvement.",
    },
    "gid://shopify/Article/1001571156300": {
        "meta_title_digest": "c5761a78042e5ed8eea5ef4a7a2684655bdf35881f80b235769f3901abc81cc6",
        "meta_description_digest": "3651c3cc61fbd6ec3c60f7f3039a2904d29308ff82028d30c4b33a5246693ca6",
        "en_title": "Microneedling for Hair Loss Meta-Analysis (2022) — Research Summary | Hairgenetix",
        "en_desc": "Plain-language summary of Gupta et al. 2022 meta-analysis. Pooled data from multiple trials confirms microneedling alone outperforms minoxidil 5%, and combining them works even better.",
    },
    "gid://shopify/Article/1001571189068": {
        "meta_title_digest": "20fe5b9d848d9b2cee7959c35dc678c838f3d125374e94f78040dc643550b991",
        "meta_description_digest": "dd48ef2e7dfdc207350c0260daf544ee921005c46e0d284f000e73560c678a40",
        "en_title": "Copper Tripeptide Hair Loss Study (2021) — Research Summary | Hairgenetix",
        "en_desc": "Plain-language summary of Pamela 2021 pilot study. Copper tripeptide serum improved hair fullness in men with pattern baldness over 6 months in a placebo-controlled clinical trial.",
    },
    "gid://shopify/Article/1001571254604": {
        "meta_title_digest": "94ec3b8dfb9493e9036194e981de9ab01e06b76dbda7827555a950397bf83009",
        "meta_description_digest": "a0501cb7f393cd4cc90993c293bef467c3be3b7936f842df0c98dd354597f5d6",
        "en_title": "Microneedling + Topical Treatment Meta-Analysis (2024) — Research Summary | Hairgenetix",
        "en_desc": "2024 meta-analysis of 8 trials (472 patients): microneedling + topical treatment grew 16 extra hairs/cm² vs topical alone. Plain-language research summary.",
    },
    "gid://shopify/Article/1001571287372": {
        "meta_title_digest": "b92d3dcba12c01dabe6294b0d96b9ebe7f98ba580606bfcb0a03a5dfe1707b16",
        "meta_description_digest": "3a536a9809a5b31b079776c997fa149cdbf908388f765ac501b88ae8ac623a11",
        "en_title": "Combined Microneedling Meta-Analysis (2024, 696 Patients) — Research Summary | Hairgenetix",
        "en_desc": "Largest meta-analysis on microneedling for hair loss: 13 trials, 696 patients. Combined therapy improves both hair density AND diameter. Plain-language summary.",
    },
    "gid://shopify/Article/1001571320140": {
        "meta_title_digest": "495f90f12cfb35ec4e1e2cb9ec51c429f59df23e5fa218069665a57ea6a92280",
        "meta_description_digest": "569bf407fbe26eebbfcb3ef0e9833b252e6d113aba6615061e717c74396add4f",
        "en_title": "Mesotherapy for Female Hair Loss Study (2013, 126 Women) — Research Summary | Hairgenetix",
        "en_desc": "Plain-language summary of Moftah et al. 2013: mesotherapy improved hair in 62.8% of 126 women with pattern hair loss. Hair became thicker and stronger.",
    },
    "gid://shopify/Article/1001571418444": {
        "meta_title_digest": "abe2b53576d9742d88a15f47dbda3f21895d5b2b6f421894115f169153430773",
        "meta_description_digest": "69f39f9c86d4a51165aa7900ac8b6282c024f3d8b66cbf4f388dab07a97f7d17",
        "en_title": "Minoxidil + Microneedling Meta-Analysis (2023) — Research Summary | Hairgenetix",
        "en_desc": "2023 meta-analysis of 10 trials (466 patients): minoxidil + microneedling significantly increases hair count vs minoxidil alone. No serious side effects.",
    },
    "gid://shopify/Article/1001571451212": {
        "meta_title_digest": "8a5936daf5dbfc46295d69a6fa63b925406a7c5ff4fd1130066bc8db620f5b4e",
        "meta_description_digest": "e6f9f7c7f20b064c570ab8f76e3d9c5f51807ff016596a2888c0ec043ed3cd8e",
        "en_title": "Mesotherapy Hair Loss Real-World Study (2022, 541 Patients) — Research Summary | Hairgenetix",
        "en_desc": "Real-world study of 541 patients: 38.4% showed marked improvement with mesotherapy. No serious or sexual side effects. Plain-language research summary.",
    },
    "gid://shopify/Article/1001571483980": {
        "meta_title_digest": "3319507ea6ed90f063669dc1f15fcea69726f8b25de740f19081317e941ab7c9",
        "meta_description_digest": "9e2e2acb063a24899ae7b646786779c131e613451be79ac9675c41dcce55e23b",
        "en_title": "Microneedling Depth Comparison Study (2021) — Research Summary | Hairgenetix",
        "en_desc": "Surprising finding: 0.6mm microneedling outperformed 1.2mm for hair growth. 60-patient randomised trial. Plain-language summary of Faghihi et al. 2021.",
    },
}

# Translations per article per locale
# Format: TRANSLATIONS[article_id][locale] = {"meta_title": "...", "meta_description": "..."}
TRANSLATIONS = {}


def t(article_id, locale, title, desc):
    if article_id not in TRANSLATIONS:
        TRANSLATIONS[article_id] = {}
    TRANSLATIONS[article_id][locale] = {"meta_title": title, "meta_description": desc}


# ============================================================
# Article 1: 1001570894156 — AHK-Cu 2007 study
# ============================================================
aid = "gid://shopify/Article/1001570894156"
t(
    aid,
    "nl",
    "AHK-Cu koperpeptide haargroei studie (2007) | Hairgenetix",
    "Seoul National University bewees dat koperpeptide AHK-Cu haarfollikelgroei stimuleert. Lees de samenvatting van dit baanbrekende onderzoek uit 2007.",
)
t(
    aid,
    "de",
    "AHK-Cu Kupferpeptid Haarwuchs-Studie (2007) | Hairgenetix",
    "Die Seoul National University bewies, dass das Kupferpeptid AHK-Cu das Haarfollikelwachstum anregt. Lesen Sie die Zusammenfassung dieser Studie von 2007.",
)
t(
    aid,
    "fr",
    "AHK-Cu peptide de cuivre croissance capillaire (2007) | Hairgenetix",
    "L'Universite de Seoul a prouve que le peptide de cuivre AHK-Cu stimule la croissance des follicules pileux. Resume accessible de cette etude de 2007.",
)
t(
    aid,
    "es",
    "AHK-Cu peptido de cobre crecimiento capilar (2007) | Hairgenetix",
    "La Universidad Nacional de Seul demostro que el peptido de cobre AHK-Cu estimula el crecimiento del foliculo piloso. Resumen accesible del estudio de 2007.",
)
t(
    aid,
    "it",
    "AHK-Cu peptide di rame crescita capelli studio (2007) | Hairgenetix",
    "La Seoul National University ha dimostrato che il peptide di rame AHK-Cu stimola la crescita dei follicoli piliferi. Sintesi accessibile dello studio 2007.",
)
t(
    aid,
    "sv",
    "AHK-Cu kopparpeptid harvaxt studie (2007) | Hairgenetix",
    "Seoul National University bevisade att kopparpeptiden AHK-Cu stimulerar harfollikeltillvaxt. Las sammanfattningen av denna banbrytande studie fran 2007.",
)
t(
    aid,
    "da",
    "AHK-Cu kobberpeptid harvakst studie (2007) | Hairgenetix",
    "Seoul National University beviste at kobberpeptid AHK-Cu stimulerer harfollikelvakst. Las resumeet af denne banebrydende undersogelse fra 2007.",
)
t(
    aid,
    "nb",
    "AHK-Cu kobberpeptid harvekst studie (2007) | Hairgenetix",
    "Seoul National University beviste at kobberpeptid AHK-Cu stimulerer harfolikkelvekst. Les sammendraget av denne banebrytende studien fra 2007.",
)

# ============================================================
# Article 2: 1001571025228 — GHK-Cu 2018 review
# ============================================================
aid = "gid://shopify/Article/1001571025228"
t(
    aid,
    "nl",
    "GHK-Cu koperpeptide regeneratie review (2018) | Hairgenetix",
    "Samenvatting van Pickart & Margolina's review over GHK-Cu koperpeptide. Gendata toont invloed op 4.000+ genen voor weefselreparatie en haargroei.",
)
t(
    aid,
    "de",
    "GHK-Cu Kupferpeptid Regeneration Review (2018) | Hairgenetix",
    "Zusammenfassung des Pickart & Margolina Reviews uber GHK-Cu. Gendaten zeigen Wirkung auf 4.000+ Gene fur Gewebereparatur und Haarwachstum.",
)
t(
    aid,
    "fr",
    "GHK-Cu peptide de cuivre regeneration revue (2018) | Hairgenetix",
    "Resume de la revue de Pickart & Margolina sur le GHK-Cu. Les donnees genetiques montrent un effet sur 4 000+ genes lies a la reparation et la pousse.",
)
t(
    aid,
    "es",
    "GHK-Cu peptido de cobre regeneracion revision (2018) | Hairgenetix",
    "Resumen de la revision de Pickart y Margolina sobre GHK-Cu. Datos geneticos muestran efecto en 4.000+ genes de reparacion tisular y crecimiento capilar.",
)
t(
    aid,
    "it",
    "GHK-Cu peptide di rame rigenerazione revisione (2018) | Hairgenetix",
    "Sintesi della revisione di Pickart e Margolina su GHK-Cu. I dati genetici mostrano effetti su 4.000+ geni legati a riparazione e crescita dei capelli.",
)
t(
    aid,
    "sv",
    "GHK-Cu kopparpeptid regenerering oversikt (2018) | Hairgenetix",
    "Sammanfattning av Pickart & Margolinas oversikt om GHK-Cu. Gendata visar paverkan pa 4 000+ gener for vavnadsreparation och harvaxt.",
)
t(
    aid,
    "da",
    "GHK-Cu kobberpeptid regenerering review (2018) | Hairgenetix",
    "Resume af Pickart & Margolinas review om GHK-Cu kobberpeptid. Gendata viser effekt pa 4.000+ gener for vavsreparation og harvakst.",
)
t(
    aid,
    "nb",
    "GHK-Cu kobberpeptid regenerering oversikt (2018) | Hairgenetix",
    "Sammendrag av Pickart & Margolinas oversikt om GHK-Cu. Gendata viser effekt pa 4 000+ gener for vevsreparasjon og harvekst.",
)

# ============================================================
# Article 3: 1001571057996 — Copper peptide microneedling 2025
# ============================================================
aid = "gid://shopify/Article/1001571057996"
t(
    aid,
    "nl",
    "Koperpeptide microneedling haarhergroei studie (2025) | Hairgenetix",
    "Kuceki et al. 2025: 5 maandelijkse microneedling sessies met koperpeptide bereikten 26,5% haarhergroei. Lees de samenvatting van dit onderzoek.",
)
t(
    aid,
    "de",
    "Kupferpeptid Microneedling Haarwuchs-Studie (2025) | Hairgenetix",
    "Kuceki et al. 2025: 5 monatliche Microneedling-Sitzungen mit Kupferpeptid erzielten 26,5% Haarnachwuchs. Lesen Sie die Zusammenfassung.",
)
t(
    aid,
    "fr",
    "Peptide de cuivre microneedling repousse etude (2025) | Hairgenetix",
    "Kuceki et al. 2025 : 5 seances mensuelles de microneedling au peptide de cuivre ont atteint 26,5% de repousse capillaire. Resume de l'etude.",
)
t(
    aid,
    "es",
    "Peptido de cobre microneedling recrecimiento estudio (2025) | Hairgenetix",
    "Kuceki et al. 2025: 5 sesiones mensuales de microneedling con peptido de cobre lograron 26,5% de recrecimiento capilar. Lea el resumen del estudio.",
)
t(
    aid,
    "it",
    "Peptide di rame microneedling ricrescita studio (2025) | Hairgenetix",
    "Kuceki et al. 2025: 5 sessioni mensili di microneedling con peptide di rame hanno ottenuto il 26,5% di ricrescita. Leggi la sintesi dello studio.",
)
t(
    aid,
    "sv",
    "Kopparpeptid microneedling haratevaxt studie (2025) | Hairgenetix",
    "Kuceki et al. 2025: 5 manatliga microneedling-sessioner med kopparpeptid uppnadde 26,5% haratevaxt. Las sammanfattningen av studien.",
)
t(
    aid,
    "da",
    "Kobberpeptid microneedling harvakst studie (2025) | Hairgenetix",
    "Kuceki et al. 2025: 5 manedlige microneedling-sessioner med kobberpeptid opnaede 26,5% harvakst. Las resumeet af undersogelsen.",
)
t(
    aid,
    "nb",
    "Kobberpeptid microneedling harvekst studie (2025) | Hairgenetix",
    "Kuceki et al. 2025: 5 manedlige microneedling-sesjoner med kobberpeptid oppnadde 26,5% harvekst. Les sammendraget av studien.",
)

# ============================================================
# Article 4: 1001571090764 — GHK peptide 2016 trial
# ============================================================
aid = "gid://shopify/Article/1001571090764"
t(
    aid,
    "nl",
    "GHK peptide haargroei klinische trial (2016) | Hairgenetix",
    "Lee et al. 2016: 45 mannen gebruikten een GHK peptide complex gedurende 6 maanden. De behandelgroep groeide 52-72 extra haren zonder bijwerkingen.",
)
t(
    aid,
    "de",
    "GHK Peptid Haarwuchs klinische Studie (2016) | Hairgenetix",
    "Lee et al. 2016: 45 Manner nutzten einen GHK-Peptid-Komplex uber 6 Monate. Die Behandlungsgruppe erzielte 52-72 zusatzliche Haare ohne Nebenwirkungen.",
)
t(
    aid,
    "fr",
    "GHK peptide croissance capillaire essai clinique (2016) | Hairgenetix",
    "Lee et al. 2016 : 45 hommes ont utilise un complexe de peptide GHK pendant 6 mois. Le groupe traite a gagne 52-72 cheveux supplementaires sans effets secondaires.",
)
t(
    aid,
    "es",
    "GHK peptido crecimiento capilar ensayo clinico (2016) | Hairgenetix",
    "Lee et al. 2016: 45 hombres usaron un complejo de peptido GHK durante 6 meses. El grupo tratado crecio 52-72 cabellos adicionales sin efectos secundarios.",
)
t(
    aid,
    "it",
    "GHK peptide crescita capelli trial clinico (2016) | Hairgenetix",
    "Lee et al. 2016: 45 uomini hanno usato un complesso peptidico GHK per 6 mesi. Il gruppo trattato ha ottenuto 52-72 capelli extra senza effetti collaterali.",
)
t(
    aid,
    "sv",
    "GHK peptid harvaxt klinisk provning (2016) | Hairgenetix",
    "Lee et al. 2016: 45 man anvande ett GHK-peptidkomplex i 6 manader. Behandlingsgruppen fick 52-72 extra har utan biverkningar.",
)
t(aid, "da", "GHK peptid harvakst klinisk forsog (2016) | Hairgenetix", "Lee et al. 2016: 45 mand brugte et GHK-peptidkompleks i 6 maneder. Behandlingsgruppen fik 52-72 ekstra har uden bivirkninger.")
t(
    aid,
    "nb",
    "GHK peptid harvekst klinisk studie (2016) | Hairgenetix",
    "Lee et al. 2016: 45 menn brukte et GHK-peptidkompleks i 6 maneder. Behandlingsgruppen fikk 52-72 ekstra har uten bivirkninger.",
)

# ============================================================
# Article 5: 1001571123532 — Microneedling Dhurat 2013
# ============================================================
aid = "gid://shopify/Article/1001571123532"
t(
    aid,
    "nl",
    "Microneedling tegen haaruitval: Dhurat 2013 studie | Hairgenetix",
    "Samenvatting van Dhurat et al. 2013 — het onderzoek dat bewees dat microneedling werkt tegen haaruitval. 100 patienten, 4x meer haargroei dan minoxidil alleen.",
)
t(
    aid,
    "de",
    "Microneedling gegen Haarausfall: Dhurat 2013 Studie | Hairgenetix",
    "Zusammenfassung von Dhurat et al. 2013 — die Studie, die bewies, dass Microneedling gegen Haarausfall wirkt. 100 Patienten, 4x mehr Haarwuchs als Minoxidil allein.",
)
t(
    aid,
    "fr",
    "Microneedling contre la chute de cheveux : etude Dhurat 2013 | Hairgenetix",
    "Resume de Dhurat et al. 2013 — l'etude qui a prouve que le microneedling fonctionne contre la chute de cheveux. 100 patients, 4x plus de repousse que le minoxidil seul.",
)
t(
    aid,
    "es",
    "Microneedling contra la caida del cabello: estudio Dhurat 2013 | Hairgenetix",
    "Resumen de Dhurat et al. 2013 — el estudio que demostro que el microneedling funciona contra la caida del cabello. 100 pacientes, 4x mas crecimiento que minoxidil solo.",
)
t(
    aid,
    "it",
    "Microneedling contro la caduta dei capelli: studio Dhurat 2013 | Hairgenetix",
    "Sintesi di Dhurat et al. 2013 — lo studio che ha dimostrato che il microneedling funziona contro la caduta dei capelli. 100 pazienti, 4x piu crescita del minoxidil.",
)
t(
    aid,
    "sv",
    "Microneedling mot harforlust: Dhurat 2013 studie | Hairgenetix",
    "Sammanfattning av Dhurat et al. 2013 — studien som bevisade att microneedling fungerar mot harforlust. 100 patienter, 4x mer harvaxt an enbart minoxidil.",
)
t(
    aid,
    "da",
    "Microneedling mod hartab: Dhurat 2013 undersogelse | Hairgenetix",
    "Resume af Dhurat et al. 2013 — undersogelsen der beviste at microneedling virker mod hartab. 100 patienter, 4x mere harvakst end minoxidil alene.",
)
t(
    aid,
    "nb",
    "Microneedling mot hartap: Dhurat 2013 studie | Hairgenetix",
    "Sammendrag av Dhurat et al. 2013 — studien som beviste at microneedling virker mot hartap. 100 pasienter, 4x mer harvekst enn minoxidil alene.",
)

# ============================================================
# Article 6: 1001571156300 — Microneedling meta-analysis 2022
# ============================================================
aid = "gid://shopify/Article/1001571156300"
t(
    aid,
    "nl",
    "Microneedling haaruitval meta-analyse (2022) | Hairgenetix",
    "Samenvatting van Gupta et al. 2022 meta-analyse. Gecombineerde data bevestigt: microneedling alleen overtreft minoxidil 5%, en de combinatie werkt nog beter.",
)
t(
    aid,
    "de",
    "Microneedling Haarausfall Meta-Analyse (2022) | Hairgenetix",
    "Zusammenfassung der Gupta et al. 2022 Meta-Analyse. Gepoolte Daten bestatigen: Microneedling allein ubertrifft Minoxidil 5%, die Kombination wirkt noch besser.",
)
t(
    aid,
    "fr",
    "Microneedling chute de cheveux meta-analyse (2022) | Hairgenetix",
    "Resume de la meta-analyse de Gupta et al. 2022. Les donnees combinees confirment : le microneedling seul surpasse le minoxidil 5%, et leur combinaison est encore meilleure.",
)
t(
    aid,
    "es",
    "Microneedling caida del cabello metaanalisis (2022) | Hairgenetix",
    "Resumen del metaanalisis de Gupta et al. 2022. Los datos combinados confirman: microneedling solo supera al minoxidil 5%, y la combinacion funciona aun mejor.",
)
t(
    aid,
    "it",
    "Microneedling caduta capelli meta-analisi (2022) | Hairgenetix",
    "Sintesi della meta-analisi di Gupta et al. 2022. I dati combinati confermano: il microneedling da solo supera il minoxidil 5%, e la combinazione funziona ancora meglio.",
)
t(
    aid,
    "sv",
    "Microneedling harforlust metaanalys (2022) | Hairgenetix",
    "Sammanfattning av Gupta et al. 2022 metaanalys. Samlade data bekraftar: microneedling ensamt overtraffar minoxidil 5%, och kombinationen fungerar annu battre.",
)
t(
    aid,
    "da",
    "Microneedling hartab metaanalyse (2022) | Hairgenetix",
    "Resume af Gupta et al. 2022 metaanalyse. Samlede data bekrafter: microneedling alene overgaar minoxidil 5%, og kombinationen virker endnu bedre.",
)
t(
    aid,
    "nb",
    "Microneedling hartap metaanalyse (2022) | Hairgenetix",
    "Sammendrag av Gupta et al. 2022 metaanalyse. Samlede data bekrefter: microneedling alene overgaar minoxidil 5%, og kombinasjonen virker enda bedre.",
)

# ============================================================
# Article 7: 1001571189068 — Copper tripeptide 2021
# ============================================================
aid = "gid://shopify/Article/1001571189068"
t(
    aid,
    "nl",
    "Kopertripeptide haaruitval studie (2021) | Hairgenetix",
    "Samenvatting van Pamela 2021 pilotstudie. Kopertripeptide serum verbeterde haarvolume bij mannen met kaalheid in een placebo-gecontroleerde klinische studie van 6 maanden.",
)
t(
    aid,
    "de",
    "Kupfertripeptid Haarausfall Studie (2021) | Hairgenetix",
    "Zusammenfassung der Pamela 2021 Pilotstudie. Kupfertripeptid-Serum verbesserte die Haarfulle bei Mannern mit Haarausfall in einer placebokontrollierten Studie uber 6 Monate.",
)
t(
    aid,
    "fr",
    "Tripeptide de cuivre chute de cheveux etude (2021) | Hairgenetix",
    "Resume de l'etude pilote Pamela 2021. Le serum tripeptide de cuivre a ameliore la densite capillaire chez les hommes avec calvitie en essai clinique de 6 mois.",
)
t(
    aid,
    "es",
    "Tripeptido de cobre caida del cabello estudio (2021) | Hairgenetix",
    "Resumen del estudio piloto Pamela 2021. El suero de tripeptido de cobre mejoro la densidad capilar en hombres con calvicie en un ensayo clinico de 6 meses.",
)
t(
    aid,
    "it",
    "Tripeptide di rame caduta capelli studio (2021) | Hairgenetix",
    "Sintesi dello studio pilota Pamela 2021. Il siero tripeptide di rame ha migliorato la densita dei capelli negli uomini con calvizie in uno studio clinico di 6 mesi.",
)
t(
    aid,
    "sv",
    "Koppartripeptid harforlust studie (2021) | Hairgenetix",
    "Sammanfattning av Pamela 2021 pilotstudie. Koppartripeptidserum forbattrade harfyllnaden hos man med haravfall i en placebokontrollerad klinisk studie pa 6 manader.",
)
t(
    aid,
    "da",
    "Kobbertripeptid hartab studie (2021) | Hairgenetix",
    "Resume af Pamela 2021 pilotundersogelse. Kobbertripeptid serum forbedrede harfylden hos mand med skaldethed i en placebokontrolleret klinisk undersogelse pa 6 maneder.",
)
t(
    aid,
    "nb",
    "Kobbertripeptid hartap studie (2021) | Hairgenetix",
    "Sammendrag av Pamela 2021 pilotstudie. Kobbertripeptid serum forbedret harfylden hos menn med skallethet i en placebokontrollert klinisk studie pa 6 maneder.",
)

# ============================================================
# Article 8: 1001571254604 — Microneedling + topical 2024
# ============================================================
aid = "gid://shopify/Article/1001571254604"
t(
    aid,
    "nl",
    "Microneedling + topische behandeling meta-analyse (2024) | Hairgenetix",
    "Meta-analyse van 8 studies (472 patienten): microneedling + topische behandeling leverde 16 extra haren/cm2 op ten opzichte van topische behandeling alleen.",
)
t(
    aid,
    "de",
    "Microneedling + topische Behandlung Meta-Analyse (2024) | Hairgenetix",
    "Meta-Analyse von 8 Studien (472 Patienten): Microneedling + topische Behandlung erzielte 16 zusatzliche Haare/cm2 gegenuber topischer Behandlung allein.",
)
t(
    aid,
    "fr",
    "Microneedling + traitement topique meta-analyse (2024) | Hairgenetix",
    "Meta-analyse de 8 essais (472 patients) : microneedling + traitement topique a produit 16 cheveux supplementaires/cm2 par rapport au traitement topique seul.",
)
t(
    aid,
    "es",
    "Microneedling + tratamiento topico metaanalisis (2024) | Hairgenetix",
    "Metaanalisis de 8 ensayos (472 pacientes): microneedling + tratamiento topico produjo 16 cabellos extra/cm2 frente al tratamiento topico solo.",
)
t(
    aid,
    "it",
    "Microneedling + trattamento topico meta-analisi (2024) | Hairgenetix",
    "Meta-analisi di 8 studi (472 pazienti): microneedling + trattamento topico ha prodotto 16 capelli extra/cm2 rispetto al trattamento topico da solo.",
)
t(
    aid,
    "sv",
    "Microneedling + topisk behandling metaanalys (2024) | Hairgenetix",
    "Metaanalys av 8 studier (472 patienter): microneedling + topisk behandling gav 16 extra har/cm2 jamfort med enbart topisk behandling.",
)
t(
    aid,
    "da",
    "Microneedling + topisk behandling metaanalyse (2024) | Hairgenetix",
    "Metaanalyse af 8 studier (472 patienter): microneedling + topisk behandling gav 16 ekstra har/cm2 sammenlignet med topisk behandling alene.",
)
t(
    aid,
    "nb",
    "Microneedling + topisk behandling metaanalyse (2024) | Hairgenetix",
    "Metaanalyse av 8 studier (472 pasienter): microneedling + topisk behandling ga 16 ekstra har/cm2 sammenlignet med topisk behandling alene.",
)

# ============================================================
# Article 9: 1001571287372 — Combined microneedling 2024
# ============================================================
aid = "gid://shopify/Article/1001571287372"
t(
    aid,
    "nl",
    "Gecombineerde microneedling meta-analyse (2024) | Hairgenetix",
    "Grootste meta-analyse over microneedling tegen haaruitval: 13 studies, 696 patienten. Gecombineerde therapie verbetert zowel haardichtheid als haardikte.",
)
t(
    aid,
    "de",
    "Kombinierte Microneedling Meta-Analyse (2024) | Hairgenetix",
    "Grosste Meta-Analyse zu Microneedling bei Haarausfall: 13 Studien, 696 Patienten. Kombinationstherapie verbessert sowohl Haardichte als auch Haardicke.",
)
t(
    aid,
    "fr",
    "Microneedling combine meta-analyse (2024, 696 patients) | Hairgenetix",
    "La plus grande meta-analyse sur le microneedling contre la chute : 13 essais, 696 patients. La therapie combinee ameliore densite ET diametre des cheveux.",
)
t(
    aid,
    "es",
    "Microneedling combinado metaanalisis (2024, 696 pacientes) | Hairgenetix",
    "El mayor metaanalisis sobre microneedling contra la caida: 13 ensayos, 696 pacientes. La terapia combinada mejora densidad Y diametro del cabello.",
)
t(
    aid,
    "it",
    "Microneedling combinato meta-analisi (2024, 696 pazienti) | Hairgenetix",
    "La piu grande meta-analisi sul microneedling contro la caduta: 13 studi, 696 pazienti. La terapia combinata migliora densita E diametro dei capelli.",
)
t(
    aid,
    "sv",
    "Kombinerad microneedling metaanalys (2024, 696 patienter) | Hairgenetix",
    "Storsta metaanalysen om microneedling mot harforlust: 13 studier, 696 patienter. Kombinationsbehandling forbattrar bade hardensitet och hartjocklek.",
)
t(
    aid,
    "da",
    "Kombineret microneedling metaanalyse (2024, 696 patienter) | Hairgenetix",
    "Storste metaanalyse om microneedling mod hartab: 13 studier, 696 patienter. Kombinationsbehandling forbedrer bade hartaethed og hartykkelse.",
)
t(
    aid,
    "nb",
    "Kombinert microneedling metaanalyse (2024, 696 pasienter) | Hairgenetix",
    "Storste metaanalyse om microneedling mot hartap: 13 studier, 696 pasienter. Kombinasjonsbehandling forbedrer bade hartetthet og hartykkelse.",
)

# ============================================================
# Article 10: 1001571320140 — Mesotherapy female 2013
# ============================================================
aid = "gid://shopify/Article/1001571320140"
t(
    aid,
    "nl",
    "Mesotherapie vrouwelijk haaruitval studie (2013) | Hairgenetix",
    "Samenvatting van Moftah et al. 2013: mesotherapie verbeterde haar bij 62,8% van 126 vrouwen met patroonhaaruitval. Haar werd dikker en sterker.",
)
t(
    aid,
    "de",
    "Mesotherapie weiblicher Haarausfall Studie (2013) | Hairgenetix",
    "Zusammenfassung von Moftah et al. 2013: Mesotherapie verbesserte das Haar bei 62,8% von 126 Frauen mit erblichem Haarausfall. Haar wurde dicker und kraftiger.",
)
t(
    aid,
    "fr",
    "Mesotherapie chute de cheveux feminine etude (2013) | Hairgenetix",
    "Resume de Moftah et al. 2013 : la mesotherapie a ameliore les cheveux chez 62,8% de 126 femmes avec alopecie. Les cheveux sont devenus plus epais et forts.",
)
t(
    aid,
    "es",
    "Mesoterapia caida del cabello femenina estudio (2013) | Hairgenetix",
    "Resumen de Moftah et al. 2013: la mesoterapia mejoro el cabello en el 62,8% de 126 mujeres con alopecia. El cabello se volvio mas grueso y fuerte.",
)
t(
    aid,
    "it",
    "Mesoterapia caduta capelli femminile studio (2013) | Hairgenetix",
    "Sintesi di Moftah et al. 2013: la mesoterapia ha migliorato i capelli nel 62,8% di 126 donne con alopecia. I capelli sono diventati piu spessi e forti.",
)
t(
    aid,
    "sv",
    "Mesoterapi kvinnligt harforlust studie (2013) | Hairgenetix",
    "Sammanfattning av Moftah et al. 2013: mesoterapi forbattrade haret hos 62,8% av 126 kvinnor med haravfall. Haret blev tjockare och starkare.",
)
t(
    aid,
    "da",
    "Mesoterapi kvindeligt hartab studie (2013) | Hairgenetix",
    "Resume af Moftah et al. 2013: mesoterapi forbedrede haret hos 62,8% af 126 kvinder med hartab. Haret blev tykkere og starkere.",
)
t(
    aid,
    "nb",
    "Mesoterapi kvinnelig hartap studie (2013) | Hairgenetix",
    "Sammendrag av Moftah et al. 2013: mesoterapi forbedret haret hos 62,8% av 126 kvinner med hartap. Haret ble tykkere og sterkere.",
)

# ============================================================
# Article 11: 1001571418444 — Minoxidil + microneedling 2023
# ============================================================
aid = "gid://shopify/Article/1001571418444"
t(
    aid,
    "nl",
    "Minoxidil + microneedling meta-analyse (2023) | Hairgenetix",
    "Meta-analyse van 10 studies (466 patienten): minoxidil + microneedling verhoogt het aantal haren significant vergeleken met minoxidil alleen. Geen ernstige bijwerkingen.",
)
t(
    aid,
    "de",
    "Minoxidil + Microneedling Meta-Analyse (2023) | Hairgenetix",
    "Meta-Analyse von 10 Studien (466 Patienten): Minoxidil + Microneedling steigert die Haarzahl signifikant gegenuber Minoxidil allein. Keine schweren Nebenwirkungen.",
)
t(
    aid,
    "fr",
    "Minoxidil + microneedling meta-analyse (2023) | Hairgenetix",
    "Meta-analyse de 10 essais (466 patients) : minoxidil + microneedling augmente significativement le nombre de cheveux par rapport au minoxidil seul. Pas d'effets graves.",
)
t(
    aid,
    "es",
    "Minoxidil + microneedling metaanalisis (2023) | Hairgenetix",
    "Metaanalisis de 10 ensayos (466 pacientes): minoxidil + microneedling aumenta significativamente el recuento capilar frente a minoxidil solo. Sin efectos graves.",
)
t(
    aid,
    "it",
    "Minoxidil + microneedling meta-analisi (2023) | Hairgenetix",
    "Meta-analisi di 10 studi (466 pazienti): minoxidil + microneedling aumenta significativamente il conteggio dei capelli rispetto al solo minoxidil. Nessun effetto grave.",
)
t(
    aid,
    "sv",
    "Minoxidil + microneedling metaanalys (2023) | Hairgenetix",
    "Metaanalys av 10 studier (466 patienter): minoxidil + microneedling okar harantalet signifikant jamfort med enbart minoxidil. Inga allvarliga biverkningar.",
)
t(
    aid,
    "da",
    "Minoxidil + microneedling metaanalyse (2023) | Hairgenetix",
    "Metaanalyse af 10 studier (466 patienter): minoxidil + microneedling oger harantallet signifikant sammenlignet med minoxidil alene. Ingen alvorlige bivirkninger.",
)
t(
    aid,
    "nb",
    "Minoxidil + microneedling metaanalyse (2023) | Hairgenetix",
    "Metaanalyse av 10 studier (466 pasienter): minoxidil + microneedling oker harantallet signifikant sammenlignet med minoxidil alene. Ingen alvorlige bivirkninger.",
)

# ============================================================
# Article 12: 1001571451212 — Mesotherapy real-world 2022
# ============================================================
aid = "gid://shopify/Article/1001571451212"
t(
    aid,
    "nl",
    "Mesotherapie haaruitval praktijkstudie (2022) | Hairgenetix",
    "Praktijkstudie met 541 patienten: 38,4% toonde duidelijke verbetering met mesotherapie. Geen ernstige of seksuele bijwerkingen. Lees de samenvatting.",
)
t(
    aid,
    "de",
    "Mesotherapie Haarausfall Praxisstudie (2022) | Hairgenetix",
    "Praxisstudie mit 541 Patienten: 38,4% zeigten deutliche Verbesserung mit Mesotherapie. Keine schweren oder sexuellen Nebenwirkungen. Lesen Sie die Zusammenfassung.",
)
t(
    aid,
    "fr",
    "Mesotherapie chute de cheveux etude terrain (2022) | Hairgenetix",
    "Etude terrain sur 541 patients : 38,4% ont montre une amelioration marquee avec la mesotherapie. Aucun effet secondaire grave ou sexuel. Resume accessible.",
)
t(
    aid,
    "es",
    "Mesoterapia caida del cabello estudio real (2022) | Hairgenetix",
    "Estudio del mundo real con 541 pacientes: 38,4% mostro mejoria notable con mesoterapia. Sin efectos secundarios graves ni sexuales. Lea el resumen.",
)
t(
    aid,
    "it",
    "Mesoterapia caduta capelli studio reale (2022) | Hairgenetix",
    "Studio reale su 541 pazienti: il 38,4% ha mostrato un miglioramento marcato con la mesoterapia. Nessun effetto collaterale grave o sessuale. Leggi la sintesi.",
)
t(
    aid,
    "sv",
    "Mesoterapi harforlust verklighetsbaserad studie (2022) | Hairgenetix",
    "Verklighetsbaserad studie med 541 patienter: 38,4% visade tydlig forbattring med mesoterapi. Inga allvarliga eller sexuella biverkningar. Las sammanfattningen.",
)
t(
    aid,
    "da",
    "Mesoterapi hartab virkelighedsstudie (2022) | Hairgenetix",
    "Virkelighedsstudie med 541 patienter: 38,4% viste markant forbedring med mesoterapi. Ingen alvorlige eller seksuelle bivirkninger. Las resumeet.",
)
t(
    aid,
    "nb",
    "Mesoterapi hartap virkelighetsstudie (2022) | Hairgenetix",
    "Virkelighetsstudie med 541 pasienter: 38,4% viste markant forbedring med mesoterapi. Ingen alvorlige eller seksuelle bivirkninger. Les sammendraget.",
)

# ============================================================
# Article 13: 1001571483980 — Microneedling depth 2021
# ============================================================
aid = "gid://shopify/Article/1001571483980"
t(
    aid,
    "nl",
    "Microneedling diepte vergelijkingsstudie (2021) | Hairgenetix",
    "Verrassende bevinding: 0,6mm microneedling presteerde beter dan 1,2mm voor haargroei. Gerandomiseerde studie met 60 patienten. Samenvatting van Faghihi et al. 2021.",
)
t(
    aid,
    "de",
    "Microneedling Tiefe Vergleichsstudie (2021) | Hairgenetix",
    "Uberraschend: 0,6mm Microneedling war effektiver als 1,2mm fur Haarwuchs. Randomisierte Studie mit 60 Patienten. Zusammenfassung von Faghihi et al. 2021.",
)
t(
    aid,
    "fr",
    "Microneedling profondeur etude comparative (2021) | Hairgenetix",
    "Decouverte surprenante : le microneedling a 0,6mm a surpasse le 1,2mm pour la repousse. Essai randomise sur 60 patients. Resume de Faghihi et al. 2021.",
)
t(
    aid,
    "es",
    "Microneedling profundidad estudio comparativo (2021) | Hairgenetix",
    "Hallazgo sorprendente: microneedling de 0,6mm supero al de 1,2mm para el crecimiento capilar. Ensayo aleatorizado con 60 pacientes. Resumen de Faghihi et al. 2021.",
)
t(
    aid,
    "it",
    "Microneedling profondita studio comparativo (2021) | Hairgenetix",
    "Scoperta sorprendente: microneedling a 0,6mm ha superato 1,2mm per la crescita dei capelli. Studio randomizzato su 60 pazienti. Sintesi di Faghihi et al. 2021.",
)
t(
    aid,
    "sv",
    "Microneedling djup jamforelsestudie (2021) | Hairgenetix",
    "Overraskande fynd: 0,6mm microneedling var battre an 1,2mm for harvaxt. Randomiserad studie med 60 patienter. Sammanfattning av Faghihi et al. 2021.",
)
t(
    aid,
    "da",
    "Microneedling dybde sammenlignende studie (2021) | Hairgenetix",
    "Overraskende fund: 0,6mm microneedling var bedre end 1,2mm til harvakst. Randomiseret studie med 60 patienter. Resume af Faghihi et al. 2021.",
)
t(
    aid,
    "nb",
    "Microneedling dybde sammenligningsstudie (2021) | Hairgenetix",
    "Overraskende funn: 0,6mm microneedling var bedre enn 1,2mm for harvekst. Randomisert studie med 60 pasienter. Sammendrag av Faghihi et al. 2021.",
)


def run_graphql(query, variables=None):
    """Execute a GraphQL query against the Shopify Admin API."""
    payload = {"query": query}
    if variables:
        payload["variables"] = variables

    cmd = ["curl", "-s", "-X", "POST", API, "-H", "Content-Type: application/json", "-H", f"X-Shopify-Access-Token: {TOKEN}", "-d", json.dumps(payload)]

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    return json.loads(result.stdout)


def register_translations_for_article(article_id, locale_translations, article_data):
    """Register all locale translations for a single article."""
    mutation = """
    mutation translationsRegister($resourceId: ID!, $translations: [TranslationInput!]!) {
      translationsRegister(resourceId: $resourceId, translations: $translations) {
        translations {
          key
          value
          locale
        }
        userErrors {
          message
          field
        }
      }
    }
    """

    translations_input = []
    for locale, texts in locale_translations.items():
        translations_input.append({"key": "meta_title", "value": texts["meta_title"], "locale": locale, "translatableContentDigest": article_data["meta_title_digest"]})
        translations_input.append({"key": "meta_description", "value": texts["meta_description"], "locale": locale, "translatableContentDigest": article_data["meta_description_digest"]})

    variables = {"resourceId": article_id, "translations": translations_input}

    return run_graphql(mutation, variables)


def main():
    total_success = 0
    total_errors = 0

    article_ids = list(ARTICLES.keys())

    for i, article_id in enumerate(article_ids):
        article_data = ARTICLES[article_id]
        locale_translations = TRANSLATIONS[article_id]

        print(f"\n[{i + 1}/13] Registering translations for {article_id}")
        print(f"  English title: {article_data['en_title'][:60]}...")

        try:
            result = register_translations_for_article(article_id, locale_translations, article_data)

            if "data" in result and result["data"]["translationsRegister"]:
                tr_data = result["data"]["translationsRegister"]
                user_errors = tr_data.get("userErrors", [])
                translations = tr_data.get("translations", [])

                if user_errors:
                    for err in user_errors:
                        print(f"  ERROR: {err['message']} (field: {err.get('field', 'N/A')})")
                        total_errors += 1

                if translations:
                    count = len(translations)
                    total_success += count
                    print(f"  OK: {count} translations registered")
                else:
                    print("  WARNING: No translations returned")
            elif "errors" in result:
                for err in result["errors"]:
                    print(f"  API ERROR: {err.get('message', str(err))}")
                    total_errors += 1
            else:
                print(f"  UNEXPECTED: {json.dumps(result)[:200]}")
        except Exception as e:
            print(f"  EXCEPTION: {e}")
            total_errors += 1

        # Small delay between requests to avoid rate limiting
        if i < len(article_ids) - 1:
            time.sleep(0.5)

    print(f"\n{'=' * 60}")
    print("SUMMARY")
    print("  Articles processed: 13")
    print(f"  Languages: {len(LOCALES)} ({', '.join(LOCALES)})")
    print(f"  Expected translations: {13 * 8 * 2} (13 articles x 8 languages x 2 fields)")
    print(f"  Successfully registered: {total_success}")
    print(f"  Errors: {total_errors}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
