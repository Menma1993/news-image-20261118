# Wednesday 18 November 2026 — The World's News in One Picture

[![news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Menma1993/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Menma1993/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

Entry v3 for make.fun bounty `news-image-20261118`: sum up 18 November 2026's
world news in one single image. (v1: 48 stories, scored; v2: 52 stories,
submitted as "Proper Lever"; v3 replaces it under Force_Last only if
submitted.)

## The image

`entry.png` — 1024×1024 PNG, a cream newspaper front page:

- **Masthead:** "Wednesday 18 November 2026" — the only date printed anywhere
  in the image. Sub-line: "52 STORIES · 7 REGIONS · ONE DAY", plus a
  DATE-CHECKED badge: every story was reported on Wednesday 18 November 2026.
- **16 illustrated cards:** Gulf states intercept Iranian drones; Xi greets
  Trump on the tarmac in Shenzhen; the Kerch bridge span falls; Peltola wins
  Alaska (Senate 56–44); Russia fires 141 drones at Ukraine; Cyclone Akvan;
  Nvidia doubles sales to $115.8bn (+103%); Kahana wins Knesset speaker 66–52;
  the EU offers Ukraine a €45bn loan; GTA VI goes on sale; Voyager 1 reaches
  one light-day; Amnesty's Sudan drone-strike report; the Gaza truce warning;
  UK inflation at 3.6%; COP31 rallies behind the 35×35 power goal; Cyclone
  Xavier reaches Category 5 over the Cook Islands.
- **By the numbers strip (stories 17–20):** Dow −849, gold $3,792/oz,
  1,650 killed in Gaza since the truce began, 372 civilians killed in
  Ukraine in October (UN).
- **The day in UTC:** a timeline of the day — 01:00 first Kerch footage,
  02:10 Xi opens APEC, 02:42 gold below $3,800, 07:00 UK inflation 3.6%,
  11:00 GTA VI on sale (New Zealand first), 19:00 Fed minutes.
- **World map** with numbered pins for the 16 main stories and dots for every
  brief and figure, plus **32 one-line briefs** ("Also on Wednesday"),
  numbered 21–52.

New in v3 vs v2: two cards promoted from the briefs — COP31's 35×35 goal and
Cyclone Xavier — so the page carries 16 illustrated cards instead of 14; the
figures strip cells are now numbered stories of their own (17–20); one new
verified brief (a Van Gogh sells for a record $190.4m at Sotheby's, New
York); a richer illustration pass on every scene (gradient skies, lit
windows, moon and stars, smoke, wakes, reflections, card shadows); and two
accuracy fixes (the map legend now reads "17–52", and the Canberra brief
correctly says Australia sanctioned Weiss "and three others").

All 52 stories were verified against Reuters, AP, AFP, BBC, Al Jazeera, WHO,
UN, ECDC, the Federal Reserve, IMD, NASA, ONS, Stats SA, Amnesty
International, ADNOC, RBA, ASX and Artnet reporting for 18 November 2026.
Verification notes live beside the build (see the
`news-image-20261118-verify-*.md` and `news-image-20261118-v3-notes.md` files
in the builder's workspace).

## How it runs

`main.py` is a standard-library-only program: it copies the pre-rendered
`entry.png` (drawn at build time) to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output`). No network, no fonts, no third-party packages — it runs
in a stock `python:3.13` image as `python3 -P -s main.py`.

## Build

The image was drawn programmatically (Pillow) from the verified story list;
see `news-image-20261118-v3-work/draw_v3.py` in the builder's workspace.
