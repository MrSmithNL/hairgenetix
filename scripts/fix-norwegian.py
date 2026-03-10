#!/usr/bin/env python3
"""Fix Norwegian translations - use locale 'no' instead of 'nb'."""

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

ARTICLES = {
    "gid://shopify/Article/1001570894156": {
        "meta_title_digest": "29cb437586ef194c60112a8d37e636aebca01322e304f2203ce38bd2fea112e6",
        "meta_description_digest": "9f31663b223b736164d68a59733c260d09c43f88385dd057af6589a9bb686f55",
        "no_title": "AHK-Cu kobberpeptid harvekst studie (2007) | Hairgenetix",
        "no_desc": "Seoul National University beviste at kobberpeptid AHK-Cu stimulerer harfolikkelvekst. Les sammendraget av denne banebrytende studien fra 2007.",
    },
    "gid://shopify/Article/1001571025228": {
        "meta_title_digest": "bbca2cfe865b06f7c05d2bfc840d16700c53bffb5aa31297380ebedac89c882b",
        "meta_description_digest": "82b252b387874fcc1ef9dd5c81220f3514e6beaa6d939ecc05cb9c1af9f5e9d9",
        "no_title": "GHK-Cu kobberpeptid regenerering oversikt (2018) | Hairgenetix",
        "no_desc": "Sammendrag av Pickart & Margolinas oversikt om GHK-Cu. Gendata viser effekt pa 4 000+ gener for vevsreparasjon og harvekst.",
    },
    "gid://shopify/Article/1001571057996": {
        "meta_title_digest": "76184dbb38e7883b15ba8dcbbe4a74946bfaf1868f12f181072bd60ae58d54f9",
        "meta_description_digest": "a22a77f97d6dabd62fd94ca0521e45f0bc8986382a21a6355861950cbde8c77c",
        "no_title": "Kobberpeptid microneedling harvekst studie (2025) | Hairgenetix",
        "no_desc": "Kuceki et al. 2025: 5 manedlige microneedling-sesjoner med kobberpeptid oppnadde 26,5% harvekst. Les sammendraget av studien.",
    },
    "gid://shopify/Article/1001571090764": {
        "meta_title_digest": "b4a4930c5ddcf20caa22115a9358473676c109d819848861df5232f5e6e47c2d",
        "meta_description_digest": "d6fd719c103bda9f372b047538181725ac82729676ec4bc8d3eb9eb115542208",
        "no_title": "GHK peptid harvekst klinisk studie (2016) | Hairgenetix",
        "no_desc": "Lee et al. 2016: 45 menn brukte et GHK-peptidkompleks i 6 maneder. Behandlingsgruppen fikk 52-72 ekstra har uten bivirkninger.",
    },
    "gid://shopify/Article/1001571123532": {
        "meta_title_digest": "d39f21308760c027b010e5bf5702533dcd98dc4d8b28b8768a9ba3125a6c5397",
        "meta_description_digest": "8e53841d286cd295b1926aafb013b6b0902ae275024b0ba81d46446791ae43b1",
        "no_title": "Microneedling mot hartap: Dhurat 2013 studie | Hairgenetix",
        "no_desc": "Sammendrag av Dhurat et al. 2013 -- studien som beviste at microneedling virker mot hartap. 100 pasienter, 4x mer harvekst enn minoxidil alene.",
    },
    "gid://shopify/Article/1001571156300": {
        "meta_title_digest": "c5761a78042e5ed8eea5ef4a7a2684655bdf35881f80b235769f3901abc81cc6",
        "meta_description_digest": "3651c3cc61fbd6ec3c60f7f3039a2904d29308ff82028d30c4b33a5246693ca6",
        "no_title": "Microneedling hartap metaanalyse (2022) | Hairgenetix",
        "no_desc": "Sammendrag av Gupta et al. 2022 metaanalyse. Samlede data bekrefter: microneedling alene overgaar minoxidil 5%, og kombinasjonen virker enda bedre.",
    },
    "gid://shopify/Article/1001571189068": {
        "meta_title_digest": "20fe5b9d848d9b2cee7959c35dc678c838f3d125374e94f78040dc643550b991",
        "meta_description_digest": "dd48ef2e7dfdc207350c0260daf544ee921005c46e0d284f000e73560c678a40",
        "no_title": "Kobbertripeptid hartap studie (2021) | Hairgenetix",
        "no_desc": "Sammendrag av Pamela 2021 pilotstudie. Kobbertripeptid serum forbedret harfylden hos menn med skallethet i en placebokontrollert klinisk studie pa 6 maneder.",
    },
    "gid://shopify/Article/1001571254604": {
        "meta_title_digest": "94ec3b8dfb9493e9036194e981de9ab01e06b76dbda7827555a950397bf83009",
        "meta_description_digest": "a0501cb7f393cd4cc90993c293bef467c3be3b7936f842df0c98dd354597f5d6",
        "no_title": "Microneedling + topisk behandling metaanalyse (2024) | Hairgenetix",
        "no_desc": "Metaanalyse av 8 studier (472 pasienter): microneedling + topisk behandling ga 16 ekstra har/cm2 sammenlignet med topisk behandling alene.",
    },
    "gid://shopify/Article/1001571287372": {
        "meta_title_digest": "b92d3dcba12c01dabe6294b0d96b9ebe7f98ba580606bfcb0a03a5dfe1707b16",
        "meta_description_digest": "3a536a9809a5b31b079776c997fa149cdbf908388f765ac501b88ae8ac623a11",
        "no_title": "Kombinert microneedling metaanalyse (2024, 696 pasienter) | Hairgenetix",
        "no_desc": "Storste metaanalyse om microneedling mot hartap: 13 studier, 696 pasienter. Kombinasjonsbehandling forbedrer bade hartetthet og hartykkelse.",
    },
    "gid://shopify/Article/1001571320140": {
        "meta_title_digest": "495f90f12cfb35ec4e1e2cb9ec51c429f59df23e5fa218069665a57ea6a92280",
        "meta_description_digest": "569bf407fbe26eebbfcb3ef0e9833b252e6d113aba6615061e717c74396add4f",
        "no_title": "Mesoterapi kvinnelig hartap studie (2013) | Hairgenetix",
        "no_desc": "Sammendrag av Moftah et al. 2013: mesoterapi forbedret haret hos 62,8% av 126 kvinner med hartap. Haret ble tykkere og sterkere.",
    },
    "gid://shopify/Article/1001571418444": {
        "meta_title_digest": "abe2b53576d9742d88a15f47dbda3f21895d5b2b6f421894115f169153430773",
        "meta_description_digest": "69f39f9c86d4a51165aa7900ac8b6282c024f3d8b66cbf4f388dab07a97f7d17",
        "no_title": "Minoxidil + microneedling metaanalyse (2023) | Hairgenetix",
        "no_desc": "Metaanalyse av 10 studier (466 pasienter): minoxidil + microneedling oker harantallet signifikant sammenlignet med minoxidil alene. Ingen alvorlige bivirkninger.",
    },
    "gid://shopify/Article/1001571451212": {
        "meta_title_digest": "8a5936daf5dbfc46295d69a6fa63b925406a7c5ff4fd1130066bc8db620f5b4e",
        "meta_description_digest": "e6f9f7c7f20b064c570ab8f76e3d9c5f51807ff016596a2888c0ec043ed3cd8e",
        "no_title": "Mesoterapi hartap virkelighetsstudie (2022) | Hairgenetix",
        "no_desc": "Virkelighetsstudie med 541 pasienter: 38,4% viste markant forbedring med mesoterapi. Ingen alvorlige eller seksuelle bivirkninger. Les sammendraget.",
    },
    "gid://shopify/Article/1001571483980": {
        "meta_title_digest": "3319507ea6ed90f063669dc1f15fcea69726f8b25de740f19081317e941ab7c9",
        "meta_description_digest": "9e2e2acb063a24899ae7b646786779c131e613451be79ac9675c41dcce55e23b",
        "no_title": "Microneedling dybde sammenligningsstudie (2021) | Hairgenetix",
        "no_desc": "Overraskende funn: 0,6mm microneedling var bedre enn 1,2mm for harvekst. Randomisert studie med 60 pasienter. Sammendrag av Faghihi et al. 2021.",
    },
}

MUTATION = """
mutation translationsRegister($resourceId: ID!, $translations: [TranslationInput!]!) {
  translationsRegister(resourceId: $resourceId, translations: $translations) {
    translations { key value locale }
    userErrors { message field }
  }
}
"""

total_success = 0
total_errors = 0

for i, (aid, data) in enumerate(ARTICLES.items()):
    translations_input = [
        {"key": "meta_title", "value": data["no_title"], "locale": "no", "translatableContentDigest": data["meta_title_digest"]},
        {"key": "meta_description", "value": data["no_desc"], "locale": "no", "translatableContentDigest": data["meta_description_digest"]},
    ]
    variables = {"resourceId": aid, "translations": translations_input}
    payload = {"query": MUTATION, "variables": variables}

    cmd = ["curl", "-s", "-X", "POST", API, "-H", "Content-Type: application/json", "-H", f"X-Shopify-Access-Token: {TOKEN}", "-d", json.dumps(payload)]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    resp = json.loads(result.stdout)

    if "data" in resp and resp["data"]["translationsRegister"]:
        tr = resp["data"]["translationsRegister"]
        errors = tr.get("userErrors", [])
        translations = tr.get("translations", [])
        if errors:
            for e in errors:
                print(f"[{i + 1}/13] ERROR: {e['message']}")
                total_errors += 1
        if translations:
            total_success += len(translations)
            print(f"[{i + 1}/13] OK: {len(translations)} Norwegian translations for article {aid.split('/')[-1]}")
    elif "errors" in resp:
        for e in resp["errors"]:
            print(f"[{i + 1}/13] API ERROR: {e.get('message', str(e))}")
            total_errors += 1

    time.sleep(0.3)

print(f"\nNorwegian (no) fix complete: {total_success} registered, {total_errors} errors")
