---
name: scout
description: Scan for cars matching the active Car Search criteria (Gmail alerts + curated dealer sites) and write new fits to the Car Search Monday board. Triggers when the user says things like "run scout", "scan for cars", "check the car search", or on the scheduled cron (9am/1pm/5pm ET). v5.
---

# Scout — Car Hunt scanner

A two-lane scan for cars that fit the active search: Lane A reads saved-search
alert emails from the major aggregators (CarGurus, Cars.com, Autotrader,
Carfax, AutoTempest) via Gmail; Lane B scans a curated list of local dealers
and Craigslist directly by web search, since those aggregators block direct
scraping. Results are merged, scored, deduped against the Monday board, and
new fits are written as rows, reported to Slack, and logged to the anchor
Monday update.

## Targets (live IDs)

| Thing | ID |
|---|---|
| Car Search board (write rows here) | 18418974601 |
| Top group (active listings, write new rows here) | group_mm4pmtg ("New Listing") |
| Samira board (anchor item lives here) | 18418714876 |
| Anchor item "Personal Car Search" | 12331835716 |
| #car-search (all output) | C0BEC2RFC00 |
| Gmail labels (Lane A) | Car-Hunt · Car-Hunt/seen |
| Dealer target list (Lane B source) | inlined below (32 dealers, 3 tiers) |

Column IDs on board 18418974601:

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

Body style: SUV/Crossover OR Sedan, no make/model filter EXCEPT the
brand-origin rule below. price <= $5000 · mileage <= 200000 · year 2008-2026 ·
within ~50 mi of zip 08110 · must realistically seat a 6'2" driver.

Brand-origin filter — NO American-brand vehicles, Jeep excepted. Exclude:
Ford, Lincoln, Chevrolet, GMC, Buick, Cadillac, Chrysler, Dodge, Ram, Tesla,
Rivian, Lucid, Pontiac, Saturn, Hummer, Mercury, Plymouth, Oldsmobile. Jeep is
allowed (owner exception). Filter is brand of origin, NOT assembly plant —
US-assembled imports (Toyota, Honda, Subaru, Nissan, etc.) are in.

City-miles preference (soft). City-driven cars carry rougher miles. Dealers
in urban cores (Camden, Trenton, Philadelphia, Chester, Wilmington) are
already excluded from the Lane B target list. For any Lane A/Craigslist
listing that shows city prior-registration or is unusually high-mileage for
its year, keep it but rank it down as a tiebreaker only — never hide a car
(owner tolerates up to 200k).

## Procedure

### 0. First-run setup

Ensure the two Car-Hunt Gmail filters exist (inbound listing alerts that
apply label Car-Hunt). If both exist, no-op. Never duplicate them.

### 1. Lane A — Gmail (major aggregators, via saved-search email alerts)

Query: `label:Car-Hunt -label:Car-Hunt/seen`. Extract every SUV/Crossover and
Sedan meeting the criteria — no model filter, apply the brand-origin rule.
Dedup by VIN, else composite. Apply label `Car-Hunt/seen` to each message
processed.

### 2. Lane B — web (local dealers, direct scan)

Two body-style sweeps: (a) used SUV/Crossover, (b) used Sedan. Web-search the
curated dealer sites below in tier order (Tier 1 core first, then Tier 2
expansion, then Tier 3 BHPH), plus indexed Craigslist for private sellers.
Apply criteria + brand-origin rule. Do NOT scrape CarGurus / Cars.com /
Autotrader / Carfax directly — they block bots and now flow in through Lane A
email alerts.

**If a dealer or Craigslist page returns HTTP 403 to a direct fetch**, do not
retry it and do not write a row from an unverified search snippet alone —
price/mileage/URL must be confirmed on the actual listing page before it goes
on the board. Note the blocked host(s) in the run's report instead of silently
treating the lane as "checked". If most or all of Tier 1-3 plus Craigslist are
403ing in the same run, that is a signal worth escalating (see Report), not
just absorbing quietly — repeated blind Lane B runs mean the routine isn't
doing its job even though it reports "clean".

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

Combine both lanes. Per real listing build: year, make, model, price,
mileage, location, url, source. Drop any American-brand vehicle (Jeep OK).
Verdict (Good fit / Maybe / Skip) from price-vs-mileage, 6'2" headroom fit,
and the general reliability reputation of that exact make/model/year. Flag
known problem drivetrains/years as Maybe or Skip. Apply the city-miles soft
tiebreaker and prefer higher-tier dealers when otherwise equal. One-line
reason. Key = normalized url, else source|year|make|model|price|mileage.

### 4. Dedupe

Read existing Key values: `get_board_items_page` (boardId 18418974601,
columnIds `["text_mm4pv8vg"]`, includeColumns true). Drop any listing whose
Key already exists.

### 5. Write

For each NEW listing, `create_item` on board 18418974601 (top group,
group_mm4pmtg):

- name = `"Car - {year} {make} {model} ${price}"`
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

- One summary result line for the run (counts + top fit). Zero new = one
  line.
- Each Good fit also gets its own message, with a threaded outreach draft to
  the seller underneath it. Draft only — never auto-send.
- On a hard failure (board unreachable, repeated), post the failure line here
  too — everything lands in #car-search.
- If Lane B comes back mostly or fully 403'd across dealer sites and
  Craigslist, say so explicitly rather than reporting a bare "no new fits"
  — a blind lane and an empty market read are different things and the
  report should not blur them. If this has now happened for several
  consecutive runs, call out the run count so the pattern is visible instead
  of resetting to "attempt 1" framing every time.

### 7. Anchor

Post one `create_update` on Samira item 12331835716: dated, count of new
finds + top 1-2 + board link. Leave its Status In Progress (do not close it).

## Result line format — post to #car-search (C0BEC2RFC00)

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

## v5 changes (vs v4)

- Mileage ceiling 150k → 200k
- Year floor 2012 → 2008
- Added "no American brands (Jeep excepted)" filter
- Lane B re-pointed off bot-blocked aggregators (now Lane A email) and onto
  the curated tiered dealer list (inlined above)
- Added city-miles soft tiebreaker and dealer-tier ranking
