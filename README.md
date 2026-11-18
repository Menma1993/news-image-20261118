# Wednesday 18 November 2026 — The World's News in One Picture

[![news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Menma1993/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Menma1993/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

Entry for make.fun bounty `news-image-20261118`: sum up 18 November 2026's
world news in one single image.

## The image

`entry.png` — 1024×1024 PNG, a cream newspaper front page:

- **Masthead:** "Wednesday 18 November 2026" — the only date printed anywhere
  in the image. Sub-line: "48 STORIES · 6 CONTINENTS · ONE DAY".
- **14 illustrated cards:** Gulf states intercept Iranian drones; Xi greets
  Trump on the tarmac in Shenzhen; the Kerch bridge span falls; Peltola wins
  Alaska (Senate 56–44); Russia fires 141 drones at Ukraine; Cyclone Akvan;
  Nvidia doubles sales to $115.8bn (+103%); Kahana wins Knesset speaker 66–52;
  the EU offers Ukraine a €45bn loan; GTA VI goes on sale; Voyager 1 reaches
  one light-day; Amnesty's Sudan drone-strike report; the Gaza truce warning;
  UK inflation at 3.6%.
- **By the numbers strip:** Dow −849, gold $3,792/oz, COP31's 35×35 power
  goal, 1,650 killed in Gaza since the truce began.
- **World map** with numbered pins for the 14 main stories and dots for every
  brief and figure, plus **30 one-line briefs** ("Also on Wednesday").

All 48 stories were verified against Reuters, AP, AFP, BBC, Al Jazeera, WHO,
UN, IMD, NASA, ONS, Stats SA, Amnesty International, ADNOC, RBA and ASX
reporting for 18 November 2026. Verification notes live beside the build
(see the `news-image-20261118-verify-*.md` files in the builder's workspace).

## How it runs

`main.py` is a standard-library-only program: it copies the pre-rendered
`entry.png` (drawn at build time) to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output`). No network, no fonts, no third-party packages — it runs
in a stock `python:3.13` image as `python3 -P -s main.py`.

`copy_entry.py` is the readable source that `makefun compress` packed into
`main.py`; the two are byte-identical in behaviour.

## Build

The image was drawn programmatically (Pillow) from the verified story list;
see `news-image-20261118-draw.py` in the builder's workspace.
