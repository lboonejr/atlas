---
name: scout
description: Car Hunt scanner — scans Gmail listing alerts and a curated dealer list for qualifying SUVs/Crossovers and Sedans, scores fits, and writes new listings to the Car Search Monday board. Triggers when the user says things like "run scout", "run the car hunt", "scan for cars", or on the scheduled 9am/1pm/5pm ET cron.
---

# Scout — Car Hunt scanner

v5. Scans two lanes for cars matching the owner's criteria, dedupes against the
live Car Search board, writes new rows, and reports results to Slack and the
Samira anchor item. Standalone routine — same harness as Atlas.

## Identity & schedule

- Model: claude-sonnet-4-6 (cost)
- Schedule: 3x/day at 9:00 / 13:00 / 17:00 ET (uses 3 of 4 open routine slots)
- Connectors (3): Gmail · Monday (lboonejrs-team) · Slack
- Built-in tool, NOT a connector: web search — enabled in Scout's code. API runs:
  add `{"type":"web_search_20250305","name":"web_search"}` to the tools array.
  Claude Code runs: allow the WebSearch tool.

Cron is UTC. EDT (summer) = UTC−4:

```yaml
# .github/workflows/scout.yml  (EDT)
on:
  schedule:
    - cron: "0 13,17,21 * * *"   # 9am / 1pm / 5pm ET
# EST (winter) shift to: 0 14,18,22 * * *
```

## Targets (live IDs)

| Thing | ID |
|---|---|
| Car Search board (write rows here) | 18418974601 |
| Top group (active listings) | topics |
| Archive group (passed) | group_mm4pmtg |
| Samira board (anchor item lives here) | 18418714876 |
| Anchor item "Personal Car Search" | 12331835716 |
| #car-search (all output) | C0BEC2RFC00 |
| Gmail labels (Lane A) | Car-Hunt · Car-Hunt/seen |
| Dealer target list (Lane B source) | inlined in Lane B below (32 dealers, 3 tiers) |

### Column IDs on board 18418974601

| Field | Column ID | Notes |
|---|---|---|
| Verdict | color_mm4pfg5v | Good fit / Maybe / Skip |
| Key | text_mm4pv8vg | dedupe |
| Source | text_mm4p1feq | |
| Found | date_mm4p1gve | |
| Price | numeric_mm4ktakw | |
| Mileage | numeric_mm4k6t2n | |
| Year | numeric_mm4ka9nq | |
| Location | text_mm4kzxkr | |
| Listing Link | link_mm4k5qmd | canonical (ignore the dup link cols) |
| Notes | long_text_mm4kkka8 | canonical |
| Status (pipeline) | color_mm4k96gz | set new rows to "New Listing" |

## Criteria (both lanes)

Body style: SUV/Crossover OR Sedan, no make/model filter EXCEPT the brand-origin
rule below. price <= $5000 · mileage <= 200000 · year 2008-2026 · within ~50 mi
of zip 08110 · must realistically seat a 6'2" driver.

**Brand-origin filter — NO American-brand vehicles, Jeep excepted.**
Exclude these makes: Ford, Lincoln, Chevrolet, GMC, Buick, Cadillac, Chrysler,
Dodge, Ram, Tesla, Rivian, Lucid, Pontiac, Saturn, Hummer, Mercury, Plymouth,
Oldsmobile. Jeep is ALLOWED (owner exception). Filter is brand of origin, NOT
assembly plant — US-assembled imports (Toyota, Honda, Subaru, Nissan, etc.) are
IN. Any qualifying import + Jeep passes.

**City-miles preference (soft).** City-driven cars carry rougher miles. Dealers
in urban cores (Camden, Trenton, Philadelphia, Chester, Wilmington) are already
excluded from the Lane B target list. For any Lane A / Craigslist listing that
shows city prior-registration or is unusually high-mileage for its year, keep
it but rank it DOWN as a tiebreaker only — never hide a car (owner tolerates up
to 200k).

## Each run

### 0. First-run setup

Ensure the two Car-Hunt Gmail filters exist (inbound listing alerts that apply
label Car-Hunt). If both exist, no-op. Never duplicate them.

### 1. Lane A — Gmail (major aggregators via saved-search email alerts)

Query: `label:Car-Hunt -label:Car-Hunt/seen`

Extract every SUV/Crossover and Sedan meeting the criteria — no model filter,
apply the brand-origin rule. Dedup by VIN, else composite. Apply label
`Car-Hunt/seen` to each message processed.

### 2. Lane B — web (local dealers, direct scan)

Two body-style sweeps: (a) used SUV/Crossover, (b) used Sedan. `web_search` the
curated dealer sites below in tier order (Tier 1 core first, then Tier 2
expansion, then Tier 3 BHPH), plus indexed Craigslist for private sellers.
Apply criteria + brand-origin rule. Do NOT scrape CarGurus / Cars.com /
Autotrader / Carfax directly — they block bots and now flow in through Lane A
email alerts.

**TIER 1 — core (scan first, surface first):**

- City Select Auto Sales — Pennsauken & Burlington, NJ — cityselectauto.com (2 locations)
- ICarXL — Pennsauken, NJ — usauctionclub.com
- Majestic Automotive Group — Cinnaminson, NJ — majesticautonj.com
- Auto Direct Cars & Corvettes — Edgewater Park, NJ — autodirectcars.com
- Cadillac's Plus / Car N Drive — Burlington, NJ — njcarndrive.com
- Tri States Auto Group — Burlington, NJ — tristatesautogroup.com
- AutoBay — Burlington, NJ — autobay.com
- Burlington Auto Outlet — Burlington, NJ — burlingtonautooutlets.com
- Fairway Auto Outlet — Burlington, NJ — fairwayautooutlet.com (likely same op as Fairway Auto Sales, Hainesport — dedupe on first scan)
- Davis Certified Used (Davis Honda) — Burlington, NJ — davishonda.net/used-vehicles/
- Interboro Motors — Burlington, NJ — interboromotors.com
- M&M Royal Auto Inc — Burlington, NJ — mmroyalauto.com
- Alpha Car Auto Sales — Delran, NJ — alphacarautosales.com

**TIER 2 — expansion independents (within ~50 mi):**

- Premier Auto Group — Turnersville, NJ — premierautogroupllc.com
- Good Wheels Auto Sales — Glassboro, NJ — goodwheelsonline.com
- Apollo Auto Sales — Sewell, NJ — apollopreowned.com
- Mainline Auto — Deptford, NJ — mainlineautosales.com
- Iron Horse Auto Sales — Sewell, NJ — ironhorseauto.net
- Wholesale Outlet Automotive Group — Blackwood, NJ — outletcars.com
- Cherry Hill Auto Sales — Cherry Hill, NJ — cherryhillautosales.net
- Wisdom Motors — Maple Shade, NJ — wisdommotors.com
- Car Revolution — Maple Shade, NJ — carrevolution.com
- VIP Auto Outlet — Maple Shade, NJ — vipautooutlet.com
- CarShop Mt. Holly — Mount Holly, NJ — carshop.com
- Fairless Motors — Fairless Hills, PA — fairlessmotors.com
- Burns Auto Group — Fairless Hills, PA — burnsautogroup.com
- B&B Automotive — Levittown, PA — bandbautomotive.com
- Bristol Auto Mall — Levittown, PA — bristolautomall.com
- Weathers Motors — Media, PA — weathersmotors.com
- Fellah Auto Group — Springfield, PA — fellahautogroup.com

**TIER 3 — Buy-Here-Pay-Here (scan last, rank lowest):**

- Pallies Auto Sales — Sewell, NJ — palliesautosalesinc.com
- The Motor Zone — Stratford, NJ — themotorzoneinc.com (multiple lots; Vineland one may fall outside 50 mi — verify)

### 3. Merge + score

Combine both lanes. Per real listing build: year, make, model, price, mileage,
location, url, source. Drop any American-brand vehicle (Jeep OK). Verdict
(Good fit / Maybe / Skip) from price-vs-mileage, 6'2" headroom fit, and the
general reliability reputation of that exact make/model/year. Flag known
problem drivetrains/years as Maybe or Skip. Apply the city-miles soft
tiebreaker and prefer higher-tier dealers when otherwise equal. One-line
reason.

Key = normalized url, else `source|year|make|model|price|mileage`.

### 4. Dedupe

Read existing Key values: `get_board_items_page(boardId 18418974601, columnIds
["text_mm4pv8vg"], includeColumns true)`. Drop any listing whose Key already
exists.

### 5. Write

For each NEW listing, `create_item` on board 18418974601 (top group):

- name = `Car - {year} {make} {model} ${price}`
- columnValues (JSON):

```json
{
  "text_mm4pv8vg": "{key}",
  "text_mm4p1feq": "{source}",
  "color_mm4pfg5v": {"label": "{Good fit|Maybe|Skip}"},
  "numeric_mm4ktakw": {price}, "numeric_mm4k6t2n": {mileage},
  "numeric_mm4ka9nq": {year}, "text_mm4kzxkr": "{location}",
  "link_mm4k5qmd": {"url": "{url}", "text": "Listing"},
  "date_mm4p1gve": {"date": "YYYY-MM-DD"},
  "long_text_mm4kkka8": "{reason}",
  "color_mm4k96gz": {"label": "New Listing"}
}
```

### 6. Report

Post to #car-search (C0BEC2RFC00):

- One summary result line for the run (counts + top fit). Zero new = one line.
- Each Good fit also gets its OWN message, with a threaded outreach draft to
  the seller underneath it. Draft only — NEVER auto-send.

On a hard failure (board unreachable, repeated), post the failure line here
too — everything lands in #car-search.

### 7. Anchor

Post one `create_update` on Samira item 12331835716: dated, count of new finds
+ top 1-2 + board link. Leave its Status In Progress (do NOT close it).

## Result line — post to #car-search (C0BEC2RFC00)

```
🌐 ✅ Car web scan — 3 new fits (top: 2015 Forester $4,800)
direct · monday.com/boards/18418974601 — Scout
```

Zero new:

```
🌐 ✅ Car web scan — no new fits this pass
direct · monday.com/boards/18418974601 — Scout
```

Each Good fit (own message + threaded draft):

```
🌐 Good fit — 2015 Subaru Forester $4,800 · 118k mi · Pennsauken
fits 6'2", clean price-to-miles · monday.com/boards/18418974601 — Scout
   └ (thread) outreach draft, ready to send by hand — never auto-sent
```

Failure:

```
🌐 ⚠️ Car web scan FAILED — {error in a few words}
monday.com/boards/18418974601 — Scout (attempt N)
```

Voice: globe-led, "- Scout", mobile-first, no em dashes, no ALL CAPS.

## Guardrails

- **Never auto-send outreach.** Seller drafts are threaded under the Good fit
  message for the owner to send by hand.
- **Never relabel or delete Gmail filters** beyond applying `Car-Hunt/seen` —
  filter setup is idempotent (check before creating).
- **Never scrape CarGurus / Cars.com / Autotrader / Carfax directly** — they
  block bots; those sources flow in only via Lane A email alerts.
- **Never hide a car for high mileage** — the city-miles rule only reorders,
  it never drops a listing that otherwise meets the ceiling.
- **Never close the Samira anchor item** — leave Status In Progress every run.

## Deploy checklist

1. Add Scout as a managed agent / routine (sonnet), same harness as Atlas.
2. Connect the three connectors: Gmail + Monday (lboonejrs-team) + Slack.
   Enable web search in code (API: `web_search` server tool in the tools
   array; Claude Code: allow the WebSearch tool) — it is NOT a connector.
3. Commit the cron workflow (`.github/workflows/scout.yml`, adjust EDT/EST).
4. Register Scout on the registry — DONE. Scout is registered on the "Atlas
   Skills & Accounts Registry" board (18419004984, Skills group), and the Car
   Search board is logged there under Boards.
5. First run: watch #car-search for the result line and confirm rows land +
   dedupe holds.
6. v5 deltas to verify on first run: mileage/year now 200k / 2008+; American
   brands dropped (Jeep still appears); Lane B pulls from the inlined dealer
   list in tier order and does NOT hit CarGurus/Cars.com/Autotrader/Carfax
   directly; city-miles tiebreaker demotes rough listings without hiding them.
