# Sandbox Fix Proposals — EN Site

> Date: 2026-03-09
> Status: Ready for Malcolm review
> Context: These fixes require visible content changes that could affect page layout. Each needs approval before implementing.

---

## Fix 2: Heading Hierarchy Restructure

**Problem:** H2 headings across the site are marketing slogans ("Experience Hair Revival", "Gentle Power") instead of informational/question-based headings that AI models can extract.

**Affected pages:** Blog article (most impactful), homepage sections, product page

**Proposed changes (blog article example):**
- Current H2: "Gentle Power of Gold Mesotherapy"
- Proposed H2: "What Is Hair Mesotherapy and How Does It Work?"
- Current H2: "A Recipe for Hair Revival"
- Proposed H2: "What Ingredients Are in Hair Mesotherapy Serums?"

**Risk:** Changing H2 text on Shopify sections requires editing section settings or Liquid templates. May affect existing translations. HIGH layout risk if heading lengths change significantly.

**Recommendation:** Start with blog article only (most value, least risk). The blog body_html headings can be changed without touching templates.

---

## Fix 6: Comparison Tables

**Problem:** No "mesotherapy vs. alternatives" comparison content exists. AI models need structured comparisons to recommend Hairgenetix.

**Proposed approach:** Add a comparison table to the blog article body_html:

| Treatment | Invasiveness | At-Home | Cost/Month | Clinical Evidence |
|-----------|-------------|---------|------------|------------------|
| Hairgenetix Mesotherapy | Non-invasive | Yes | ~€50 | 93% reduction in 150-day trial |
| Minoxidil (Rogaine) | Non-invasive | Yes | €20-40 | FDA-approved, 30-40% see results |
| Finasteride (Propecia) | Oral medication | Yes (prescription) | €30-60 | Effective but hormonal side effects |
| PRP Therapy | Invasive (injections) | No (clinic only) | €200-500/session | Mixed evidence |
| Hair Transplant | Surgical | No (surgery) | €3,000-15,000 | Permanent but expensive |

**Risk:** LOW if added to blog article body_html. MEDIUM if added to product or homepage (requires template changes).

**Recommendation:** Add to blog article first, then evaluate for other pages.

---

## Fix 8: Science Page Content Rewrite

**Problem:** The science page (`/pages/the-science`) currently shows ONLY:
- A banner image
- Trust badges (shared across all pages)
- The recently added 515-char definition paragraph

It has NO actual scientific content. The entire page relies on the `sw--the_science_banner` section and shared trust indicators.

**What's needed:**
1. Mechanism of action explanation (how copper peptides work at cellular level)
2. Clinical trial methodology and results (the 150-day study details)
3. Ingredient deep-dives (GHK-Cu, AHK-Cu, PDRN, hyaluronic acid)
4. Published research citations with links
5. Comparison with other approaches

**Implementation options:**
- Option A: Add rich body_html content (renders via `main-page` section — confirmed working)
- Option B: Create new Shopify sections for structured science content

**Risk:** HIGH — this is a major content addition. Option A is safer (body_html only, no template changes). Content must be medically accurate and reviewed.

**Recommendation:** Use Option A. Draft 2000-3000 words of science content with proper H2-H4 hierarchy, PubMed citations, and comparison table. Malcolm reviews before publishing.

---

## Fix 9: About Page Content Enhancement

**Problem:** The about page had virtually no unique content. We've already added:
- Definition paragraph with company description
- Clinical evidence paragraph with 3 PubMed citations

Still needed:
1. Company story (founding, mission, why mesotherapy)
2. Team section (Malcolm Smith, Dr. Esther Bodde)
3. Company milestones/timeline
4. Manufacturing and quality standards

**Current body_html:** 4,805 chars (enhanced from ~0 in previous session)

**Risk:** MEDIUM — body_html changes only, no template risk. But company story needs Malcolm's input on what to include.

**Recommendation:** Malcolm provides bullet points of company story, team info, and milestones. We write the full content and add to body_html. The `main-page` section renders it automatically.

---

## Priority Order

1. **Fix 6** (comparison table in blog) — lowest risk, high value
2. **Fix 2** (blog headings) — medium risk, high AISO value
3. **Fix 9** (about content) — needs Malcolm input
4. **Fix 8** (science content) — largest effort, highest impact

---

## Next Steps

Malcolm: Review these proposals and tell me:
1. Which to proceed with?
2. For Fix 9: What company story details should we include?
3. For Fix 8: Any specific scientific claims or study details to highlight?
