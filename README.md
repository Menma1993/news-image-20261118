# Wednesday 18 November 2026 — The World's News in One Picture

[![news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Menma1993/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Menma1993/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

Entry v2 for make.fun bounty `news-image-20261118`: sum up 18 November 2026's
world news in one single image. (v1: 48 stories, scored; v2 replaces it under
Force_Last only if submitted.)

## The image

`entry.png` — 1024×1024 PNG, a cream newspaper front page:

- **Masthead:** "Wednesday 18 November 2026" — the only date printed anywhere
  in the image. Sub-line: "52 STORIES · 7 REGIONS · ONE DAY", plus a
  DATE-CHECKED badge: every story was reported on Wednesday 18 November 2026.
- **14 illustrated cards:** Gulf states intercept Iranian drones; Xi greets
  Trump on the tarmac in Shenzhen; the Kerch bridge span falls; Peltola wins
  Alaska (Senate 56–44); Russia fires 141 drones at Ukraine; Cyclone Akvan;
  Nvidia doubles sales to $115.8bn (+103%); Kahana wins Knesset speaker 66–52;
  the EU offers Ukraine a €45bn loan; GTA VI goes on sale; Voyager 1 reaches
  one light-day; Amnesty's Sudan drone-strike report; the Gaza truce warning;
  UK inflation at 3.6%.
- **By the numbers strip:** Dow −849, gold $3,792/oz, COP31's 35×35 power
  goal, 1,650 killed in Gaza since the truce began.
- **The day in UTC:** a timeline of the day — 01:00 first Kerch footage,
  02:10 Xi opens APEC, 02:42 gold below $3,800, 07:00 UK inflation 3.6%,
  11:00 GTA VI on sale (New Zealand first), 19:00 Fed minutes.
- **World map** with numbered pins for the 14 main stories and dots for every
  brief and figure, plus **38 one-line briefs** ("Also on Wednesday"),
  numbered 19–52.

New in v2 vs v1 (48 stories): 4 extra verified briefs — ECDC warns superbug
infections up 72% since 2019 (Stockholm); Quad leaders agree a first joint
patrol-aircraft exercise (Manila); Fed minutes point to more rate rises
(Washington); Nvidia stops shipping H200 AI chips to China (Santa Clara) —
plus the UTC timeline, the DATE-CHECKED badge, a 7-regions framing, and a
fixed Nvidia deck (H200 halt replaces the misleading "since Huang quit" line).

All 52 stories were verified against Reuters, AP, AFP, BBC, Al Jazeera, WHO,
UN, ECDC, the Federal Reserve, IMD, NASA, ONS, Stats SA, Amnesty
International, ADNOC, RBA and ASX reporting for 18 November 2026.
Verification notes live beside the build (see the
`news-image-20261118-verify-*.md` and `news-image-20261118-v2-notes.md` files
in the builder's workspace).

## How it runs

`main.py` is a standard-library-only program: it copies the pre-rendered
`entry.png` (drawn at build time) to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output`). No network, no fonts, no third-party packages — it runs
in a stock `python:3.13` image as `python3 -P -s main.py`.

`copy_entry.py` is the readable source that `makefun compress` packed into
`main.py`; the two are byte-identical in behaviour.

## Build

The image was drawn programmatically (Pillow) from the verified story list;
see `news-image-20261118-draw-v2.py` in the builder's workspace.
