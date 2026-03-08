# QA Checklist — Hairgenetix Changes (2026-03-08)

> Manual verification checklist for all pages affected by HG-047 through HG-066.
> Check each page visually for: correct content, no layout damage, correct language, working links.

**Languages:** EN, NL, DE, FR, ES, IT, SV, DA, NO
**Base URL:** `https://hairgenetix.com`
**Locale URLs:** `https://hairgenetix.com/{lang}/...` (e.g., `/nl/`, `/de/`, etc.)

---

## 1. Homepage (all 9 languages)

**Changes made:** Schema (Organization, BreadcrumbList), og:image https fix, twitter:image added, H1 nesting fix, FR meta title shortened

| Language | URL | What to check |
|----------|-----|---------------|
| EN | `/` | Layout intact, H1 visible, no broken elements |
| NL | `/nl` | H1 says "KEER JE HAARVERLUST OM" (not nested in h2) |
| DE | `/de` | H1 says "STOPPEN SIE IHREN HAARAUSFALL" |
| FR | `/fr` | H1 correct, browser tab title shorter than before |
| ES | `/es` | H1 says "REVIERTA SU CAÍDA DEL CABELLO" |
| IT | `/it` | H1 says "INVERTI LA CADUTA DEI CAPELLI" |
| SV | `/sv` | H1 says "VÄND DITT HÅRAVFALL" (not nested in h2) |
| DA | `/da` | H1 says "VEND DIT HÅRTAB" (not nested in h2) |
| NO | `/no` | H1 says "REVERSER DITT HÅRTAP" (not nested in h2) |

**Visual checks for ALL languages:**
- [ ] Hero banner displays correctly (no broken heading tags)
- [ ] Footer looks normal (Trustpilot link, copyright 2026)
- [ ] Page loads without errors

---

## 2. Product Pages (all 9 languages, spot-check 3 products)

**Changes made:** Product schema category translated, meta titles added/shortened, meta descriptions shortened, first product EN meta_title set

### Product 1: Copper Peptide Hair Growth Serum
| Language | URL | Meta title check (browser tab) | Meta desc check (view source) |
|----------|-----|-------------------------------|------------------------------|
| EN | `/products/copper-peptide-hair-growth-serum` | "Copper Peptide Hair Serum — Hairgenetix" | Under 155 chars |
| NL | `/nl/products/copper-peptide-hair-growth-serum` | "Koperpeptide haarserum — Hairgenetix" | Under 155 chars, in Dutch |
| DE | `/de/products/copper-peptide-hair-growth-serum` | "Kupferpeptid-Haarserum — Hairgenetix" | Under 155 chars, in German |
| FR | `/fr/products/copper-peptide-hair-growth-serum` | "Sérum capillaire peptide de cuivre — Hairgenetix" | Under 155 chars, in French |
| ES | `/es/products/copper-peptide-hair-growth-serum` | "Suero capilar péptidos de cobre — Hairgenetix" | Under 155 chars, in Spanish |
| IT | `/it/products/copper-peptide-hair-growth-serum` | "Siero capillare peptidi di rame — Hairgenetix" | Under 155 chars, in Italian |
| SV | `/sv/products/copper-peptide-hair-growth-serum` | "Kopparpeptid hårserum — Hairgenetix" | Under 155 chars, in Swedish |
| DA | `/da/products/copper-peptide-hair-growth-serum` | "Kobberpeptid hårserum — Hairgenetix" | Under 155 chars, in Danish |
| NO | `/no/products/copper-peptide-hair-growth-serum` | "Hårvekstserum med kobberpeptid — Hairgenetix" | Under 155 chars, in Norwegian |

### Product 2: Copper Peptide Shampoo (spot check)
| Language | URL | Check |
|----------|-----|-------|
| FR | `/fr/products/copper-peptide-hair-growth-shampoo-ghk-cu` | Meta desc in French, under 155 chars |
| DE | `/de/products/copper-peptide-hair-growth-shampoo-ghk-cu` | Meta desc in German, under 155 chars |
| IT | `/it/products/copper-peptide-hair-growth-shampoo-ghk-cu` | Meta desc in Italian, under 155 chars |

### Product 3: Complete Set (spot check)
| Language | URL | Check |
|----------|-----|-------|
| FR | `/fr/products/copper-peptide-set-complete-hair-growth-treatment-shampoo-conditioner-serum` | Meta desc under 155 chars |
| ES | `/es/products/copper-peptide-set-complete-hair-growth-treatment-shampoo-conditioner-serum` | Meta desc under 155 chars |

**Visual checks for ALL product pages:**
- [ ] Product images load correctly
- [ ] Price displays correctly
- [ ] Add to cart button works
- [ ] Product description text is intact and in correct language
- [ ] No broken layout elements

---

## 3. FAQ Page (all 9 languages)

**Changes made:** Page title/H1 translated, FAQPage schema translated (15 Q&As), meta title + description added for SV/DA/NO, NL handle detection fixed

| Language | URL | H1 should say | Schema check |
|----------|-----|---------------|-------------|
| EN | `/pages/faqs` | "Frequently Asked Questions" | FAQPage schema present |
| NL | `/nl/pages/veelgestelde-vragen` | "Veelgestelde vragen" | FAQPage schema present (NL uses translated handle!) |
| DE | `/de/pages/faqs` | "FAQs" | FAQPage schema present |
| FR | `/fr/pages/faqs` | "Questions Fréquemment Posées" | FAQPage schema present |
| ES | `/es/pages/faqs` | "Preguntas Frecuentes" | FAQPage schema present |
| IT | `/it/pages/faqs` | "Domande Frequenti" | FAQPage schema present |
| SV | `/sv/pages/faqs` | "Vanliga Frågor" | FAQPage schema present |
| DA | `/da/pages/faqs` | "Ofte Stillede Spørgsmål" | FAQPage schema present |
| NO | `/no/pages/faqs` | "Ofte Stilte Spørsmål" | FAQPage schema present |

**Visual checks:**
- [ ] All 15 FAQ accordion items visible and expandable
- [ ] FAQ text is in the correct language per locale
- [ ] Page layout is intact (no broken accordions or missing content)

---

## 4. Blog Listing Page (all 9 languages)

**Changes made:** Title translated, meta_title + meta_description added for all languages, EN meta desc shortened

| Language | URL | Page title should say | Browser tab (meta title) |
|----------|-----|-----------------------|------------------------|
| EN | `/blogs/articles` | "Articles" | "Hair Growth Articles & Research \| Hairgenetix" |
| NL | `/nl/blogs/articles` | "Artikelen" | "Artikelen over haargroei & onderzoek \| Hairgenetix" |
| DE | `/de/blogs/articles` | "Artikel" | "Artikel zu Haarwachstum & Forschung \| Hairgenetix" |
| FR | `/fr/blogs/articles` | "Articles" | "Articles croissance capillaire & recherche \| Hairgenetix" |
| ES | `/es/blogs/articles` | "Artículos" | "Artículos crecimiento capilar \| Hairgenetix" |
| IT | `/it/blogs/articles` | "Articoli" | "Articoli sulla crescita dei capelli e ricerca \| Hairgenetix" |
| SV | `/sv/blogs/articles` | "Artiklar" | "Artiklar om hårväxt & forskning \| Hairgenetix" |
| DA | `/da/blogs/articles` | "Artikler" | "Artikler om hårvækst & forskning \| Hairgenetix" |
| NO | `/no/blogs/articles` | "Artikler" | "Artikler om hårvekst & forskning \| Hairgenetix" |

**Visual checks:**
- [ ] Article cards display correctly
- [ ] Article links work
- [ ] No layout damage

---

## 5. Blog Articles (all 9 languages, spot-check 1 article)

**Changes made:** PubMed citations added, question-based headings, TL;DR blocks, Article schema, snippet-ready definitions

### Article: "Copper Peptides for Hair Growth"
| Language | URL | Check |
|----------|-----|-------|
| EN | `/blogs/articles/copper-peptides-hair-growth` | PubMed citation links work, headings are question-format, TL;DR block visible |
| NL | `/nl/blogs/articles/copper-peptides-hair-growth` | Article displays, content in Dutch |
| DE | `/de/blogs/articles/copper-peptides-hair-growth` | Article displays, content in German |
| FR | `/fr/blogs/articles/copper-peptides-hair-growth` | Article displays, no Cloudflare block |
| ES | `/es/blogs/articles/copper-peptides-hair-growth` | Article displays, no Cloudflare block |
| IT | `/it/blogs/articles/copper-peptides-hair-growth` | Article displays, no Cloudflare block |

**Visual checks:**
- [ ] Article text is readable and properly formatted
- [ ] PubMed links (blue underlined) are clickable and open correct studies
- [ ] No broken images or missing sections

---

## 6. Science / Research Pages (all 9 languages, spot-check 2)

**Changes made:** MedicalScholarlyArticle schema keywords + about translated, answer-first intro blocks, DE handle detection fixed

| Language | URL | Check |
|----------|-----|-------|
| EN | `/pages/the-science` | Intro block visible, content intact |
| NL | `/nl/pages/the-science` | Content in Dutch |
| DE | `/de/pages/wissenschaftlich-forschend` | DE uses translated handle! Content in German |
| EN | `/pages/scientific-research` | Intro block visible |

**Visual checks:**
- [ ] `.hg-intro` styled intro blocks display correctly (answer-first format)
- [ ] Page content is intact and in correct language

---

## 7. Instructions Page (spot-check)

**Changes made:** HowTo schema handle detection for NL ('instructies')

| Language | URL | Check |
|----------|-----|-------|
| EN | `/pages/instructions` | Content intact, HowTo schema in source |
| NL | `/nl/pages/instructies` | NL uses translated handle! Content in Dutch |

---

## 8. Collection Page (all 9 languages)

**Changes made:** Unique meta descriptions added in all 9 languages

| Language | URL | Check |
|----------|-----|-------|
| EN | `/collections/all` | Meta description is product-focused (not homepage desc) |
| NL | `/nl/collections/all` | Meta description in Dutch |
| DE | `/de/collections/all` | Meta description in German |
| FR-NO | `/fr/collections/all` ... `/no/collections/all` | Meta desc in correct language |

**Visual checks:**
- [ ] Product grid displays correctly
- [ ] Product images and prices load

---

## 9. About Us Page

**Changes made:** Created page (HG-031), added to footer menu

| Language | URL | Check |
|----------|-----|-------|
| EN | `/pages/about-us` | Company story, science, guarantee sections visible |

**Visual checks:**
- [ ] Page content reads well
- [ ] Linked from footer "Explore" menu

---

## 10. Special Files (not language-specific)

### llms.txt (all 9 languages)
**Changes made:** Full locale-aware content, all sections translated

| Language | URL | Check |
|----------|-----|-------|
| EN | `/pages/llms-txt` | Plain text, English content, all sections present |
| NL | `/nl/pages/llms-txt` | Section headers in Dutch ("Over ons", "Producten", etc.) |
| DE | `/de/pages/llms-txt` | Section headers in German ("Über uns", "Produkte", etc.) |
| FR | `/fr/pages/llms-txt` | Section headers in French |
| ES | `/es/pages/llms-txt` | Section headers in Spanish |
| IT | `/it/pages/llms-txt` | Section headers in Italian |
| SV | `/sv/pages/llms-txt` | Section headers in Swedish |
| DA | `/da/pages/llms-txt` | Section headers in Danish |
| NO | `/no/pages/llms-txt` | Section headers in Norwegian |

### llms-full.txt
| URL | Check |
|-----|-------|
| `/pages/llms-full-txt` | Extended version loads, all products/pages listed |

### ai.txt
| URL | Check |
|-----|-------|
| `/ai.txt` | Redirects to ai-txt page (200 response) |
| `/.well-known/ai.txt` | Known Shopify limitation — will 404 |

### robots.txt
| URL | Check |
|-----|-------|
| `/robots.txt` | AI bot Allow directives visible (GPTBot, ClaudeBot, etc.) |

---

## 11. Schema Verification (view page source or use Rich Results Test)

For any page, right-click > View Source and search for `application/ld+json` to check structured data.

| Schema Type | Where it should appear | What to check |
|-------------|----------------------|---------------|
| Organization | Every page | Company name, logo, Trustpilot link, AggregateRating (4.6 stars) |
| BreadcrumbList | Every page | "Home" label translated per language (NL: Startpagina, DE: Startseite, FR: Accueil, ES: Inicio, IT: Pagina iniziale, SV: Hem, DA/NO: Hjem) |
| Product | Product pages only | Name, price, SKU, category in correct language |
| FAQPage | FAQ page + product pages | Questions in correct language |
| Article | Blog article pages | Title, datePublished, author |
| ItemList | Blog listing + collection pages | List of items with position numbers |
| MedicalScholarlyArticle | Science pages | Keywords in correct language |
| HowTo | Instructions page | Steps present |
| WebPage / MedicalWebPage | Other content pages | Health pages get MedicalWebPage |

---

## Quick Test Method

1. **Browser tab check** — open page, check the tab title is in correct language and reasonable length
2. **Right-click > View Source** — Ctrl+F for `"@type"` to verify schemas are present
3. **Visual scan** — scroll through the page, check nothing looks broken
4. **Google Rich Results Test** — paste URL into https://search.google.com/test/rich-results to validate schemas

---

## Known CDN Caching Notes

Some changes may take 15-60 minutes to appear after deployment. If a page still shows old content:
- Try adding `?v=check` to the URL
- Wait 30 minutes and re-check
- The Shopify CDN will eventually serve the updated content

Pages most likely to show stale cached content:
- FAQ page H1 (title translation)
- Blog listing title
- Product meta descriptions (recently updated)
- DA/NO og:image and twitter:image
