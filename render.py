#!/usr/bin/env python3
"""Render the 20 Nov 2026 world-news front page as a 1024x1024 PNG.

Deterministic: fixed text, fixed fonts, fixed layout. The PNG bytes are
stable across runs on the same machine (Pillow writes no timestamps).
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 236)      # warm newsprint
INK = (17, 17, 17)           # near-black
RED = (139, 0, 0)            # dark red accent
GREY = (68, 68, 68)          # summary grey
HAIR = (150, 140, 120)       # hairline rules

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

MARGIN = 46
CW = W - 2 * MARGIN  # 932 content width

STORIES = [
    {
        "label": "TOP STORY  ·  WORLD COURT",
        "headline": "World court finds Myanmar guilty of genocide",
        "summary": ("The ICJ rules 9\u20136 that Myanmar committed genocide against the "
                    "Rohingya in its 2017 crackdown; about 10,000 were killed, and the "
                    "court orders their safe return home and reparations."),
        "lead": True,
    },
    {
        "label": "DIPLOMACY",
        "headline": "Trump, Xi and Putin agree nuclear-security pact",
        "summary": ("The three leaders adopt a joint declaration to cut nuclear risks "
                    "after trilateral talks on the sidelines of the APEC summit in "
                    "Shenzhen."),
        "lead": False,
    },
    {
        "label": "UKRAINE",
        "headline": "Putin vows to hit back after Crimea Bridge hit again",
        "summary": ("Ukraine's third strike on the bridge this week ends any idea of a "
                    "truce on energy and shipping attacks, Moscow says."),
        "lead": False,
    },
    {
        "label": "STRAIT OF HORMUZ",
        "headline": "Iran mines hit tankers east of Hormuz",
        "summary": ("Three oil tankers catch fire after striking mines near the Strait "
                    "of Hormuz as Tehran steps up attacks while oil prices slide."),
        "lead": False,
    },
    {
        "label": "GAZA",
        "headline": "Israel ends rare Gaza ground operation",
        "summary": ("Gazans return home after the Israeli army ends a rare ground "
                    "operation in Hamas-controlled central Gaza."),
        "lead": False,
    },
    {
        "label": "BUSINESS",
        "headline": "Anthropic's debut tops $2 trillion",
        "summary": ("Shares in the AI firm open 34% above the $83 IPO price, briefly "
                    "valuing it at about $2 trillion \u2014 the biggest listing ever, "
                    "passing SpaceX."),
        "lead": False,
    },
]


def wrap(draw, text, font, max_w):
    """Greedy word wrap to pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # outer border
    d.rectangle([10, 10, W - 11, H - 11], outline=INK, width=3)

    y = 28
    # kicker
    f_kick = ImageFont.truetype(SANS_B, 20)
    kick = "T H E   W O R L D   I N   O N E   P A G E"
    d.text(((W - d.textlength(kick, font=f_kick)) / 2, y), kick, font=f_kick, fill=RED)
    y += 26
    # masthead
    f_title = ImageFont.truetype(SERIF_B, 72)
    title = "WORLD NEWS"
    d.text(((W - d.textlength(title, font=f_title)) / 2, y), title, font=f_title, fill=INK)
    y += 86
    # date line
    f_date = ImageFont.truetype(SANS_B, 24)
    date = "Friday  \u00b7  20 November 2026"
    d.text(((W - d.textlength(date, font=f_date)) / 2, y), date, font=f_date, fill=INK)
    y += 38
    # double rule
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=INK, width=4)
    y += 6
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=INK, width=1)
    y += 10

    for i, s in enumerate(STORIES):
        lead = s["lead"]
        f_label = ImageFont.truetype(SANS_B, 19 if lead else 18)
        f_head = ImageFont.truetype(SANS_B, 31 if lead else 27)
        f_sum = ImageFont.truetype(SANS, 22 if lead else 20)

        # label
        d.text((MARGIN, y), s["label"], font=f_label, fill=RED)
        y += 26
        # headline
        head_lines = wrap(d, s["headline"], f_head, CW)
        for ln in head_lines:
            d.text((MARGIN, y), ln, font=f_head, fill=INK)
            y += 38 if lead else 33
        y += 2
        # summary
        sum_lines = wrap(d, s["summary"], f_sum, CW)
        for ln in sum_lines:
            d.text((MARGIN, y), ln, font=f_sum, fill=GREY)
            y += 28 if lead else 25
        y += 5
        # separator (not after last story)
        if i < len(STORIES) - 1:
            d.line([(MARGIN, y), (W - MARGIN, y)], fill=HAIR, width=1)
            y += 8

    # footer
    f_foot = ImageFont.truetype(SANS, 17)
    foot = "Sources: Reuters  \u00b7  AP  \u00b7  AFP  \u00b7  Nikkei  \u00b7  Al Jazeera   \u2014   All stories reported 20 November 2026"
    d.text(((W - d.textlength(foot, font=f_foot)) / 2, H - 42),
           foot, font=f_foot, fill=GREY)

    assert y <= H - 52, f"content overflow: bottom_y={y}"
    img.save("entry.png", format="PNG", optimize=True)
    print(f"saved entry.png  size={img.size}  bottom_y={y} (canvas {H})")


if __name__ == "__main__":
    main()
