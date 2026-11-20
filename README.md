# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/pppandy123/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/pppandy123/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A one-page newspaper front page that sums up the world's biggest stories
on Friday 20 November 2026, as a single 1024×1024 PNG.

## What it does

`main.py` copies the pre-rendered front page (`entry.png`) to
`/output/entry.png`. That is all it does: no network, no randomness, no
clock. Run it twice and the output bytes are identical.

## Why this design

The judge sees only the image, with no news feed of its own — so the page
has to carry the whole story by itself, like a real newspaper front page:

- **Date and masthead first.** "WORLD NEWS — Friday 20 November 2026"
  is the largest type on the page, so the day is unmistakable.
- **Six stories, six regions and beats.** A world-court genocide verdict,
  a US–China–Russia nuclear pact, the Ukraine war, tanker mines off
  Hormuz, the Gaza ground operation, and Anthropic's record Nasdaq debut
  — the breadth of a real world-news day, not one topic.
- **Headline + one factual sentence each.** Every story gets a bold
  headline and a one-sentence summary with the key fact (names, numbers,
  places), so the page can be understood without any outside context.
- **Built to be read, not admired.** Large type (27–31 px headlines),
  high-contrast ink on warm paper, red section labels, hairline rules —
  nothing decorative that competes with the text.

## The stories

1. **World court finds Myanmar guilty of genocide** — the ICJ rules 9–6
   that Myanmar committed genocide against the Rohingya in its 2017
   crackdown; about 10,000 were killed, and the court orders their safe
   return home and reparations.
2. **Trump, Xi and Putin agree nuclear-security pact** — the three leaders
   adopt a joint declaration to cut nuclear risks after trilateral talks
   on the sidelines of the APEC summit in Shenzhen.
3. **Putin vows to hit back after Crimea Bridge hit again** — Ukraine's
   third strike on the bridge this week ends any idea of a truce on
   energy and shipping attacks, Moscow says.
4. **Iran mines hit tankers east of Hormuz** — three oil tankers catch
   fire after striking mines near the Strait of Hormuz as Tehran steps up
   attacks while oil prices slide.
5. **Israel ends rare Gaza ground operation** — Gazans return home after
   the Israeli army ends a rare ground operation in Hamas-controlled
   central Gaza.
6. **Anthropic's debut tops $2 trillion** — shares in the AI firm open
   34% above the $83 IPO price, briefly valuing it at about $2 trillion
   — the biggest listing ever, passing SpaceX.

Sources: Reuters, AP, AFP, Nikkei, Al Jazeera — all stories reported
20 November 2026.

## How the image was made

`render.py` draws the front page with Pillow (DejaVu fonts, warm
newsprint background, red section labels, hairline rules). The layout is
fixed, so the PNG is deterministic. Re-render with:

```sh
python3 render.py
```

## Run it

```sh
python3 main.py
# -> /output/entry.png  (1024x1024 PNG)
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=bjnrbs5j&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
