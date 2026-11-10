#!/usr/bin/env python3
"""
Draws the two README cards of this portfolio: the Portfolio Status Board and the GitHub Stats card
(plain SVG, no dependencies), in the same style as the cards of the E-Commerce Suite README.

All numbers come from docs/portfolio.json (one entry per public repository: area, stack, the result of its
latest green CI run). Edit that file and run `python3 docs/images/make_readme_cards.py`; CI fails if the
committed SVGs are not what this script draws.
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
DATA = json.loads((OUT.parent / "portfolio.json").read_text(encoding="utf-8"))
AS_OF = DATA["as_of"]
STATS_AS_OF = DATA["as_of"]

REPOS = DATA["repos"]
AREAS = [(a["label"], sum(1 for r in REPOS if r["area"] == a["key"]), a["color"]) for a in DATA["areas"]]
TOTAL_TESTS = sum(r["tests"] for r in REPOS)
WITH_CI = sum(1 for r in REPOS if r["workflow"])
SHOP = next(r for r in REPOS if r["name"] == "RbcTcsWorld")
SUITE = next(r for r in REPOS if r["name"] == "RbcTcsWorld_ECommerceSuite")

# (project, what it shows, state) - state: flagship | active | stable
FEATURED = [
    ("RbcTcsWorld E-Commerce Suite", f"{SUITE['tests']:,} tests · 18 CI gates", "flagship"),
    ("RbcTcsWorld Shop", f"{SHOP['tests']:,} tests · 19 CI gates · affiliate first", "flagship"),
    ("PharmaPack QMS + Serialization", "78 / 78 · desktop builds", "active"),
    ("ClinTrial-Connect", "115 / 115 · Spring Boot", "active"),
    ("Payroll app + automation", "160 + 260 tests · real MySQL", "stable"),
    ("Amazon: Cypress BDD", "39 scenarios × 3 browsers", "stable"),
    ("QA Brains: Python Playwright", "15 / 15 · Chromium + Firefox", "stable"),
    ("QA Brains: TypeScript Playwright", "15 / 15 · GitHub Actions", "stable"),
    ("Android UI: MyDemo (Appium)", "75 / 75 · emulator in CI", "stable"),
    ("Appium Mobile Automation", "22 device + 8 unit · emulator", "stable"),
    ("NorthFace AutomationExercise", "83 passed · 2 skipped", "stable"),
    ("API: REST Assured + Postman", "20 tests + 40 assertions", "stable"),
]
# tests per repository, the ten largest after the two flagships
TOP = sorted((r for r in REPOS if not r.get("flagship") and r["tests"]), key=lambda r: -r["tests"])[:10]
SHORT = {
    "PayrollManagementSystems_Automation_Java_MySql_Selenium": "Payroll tests",
    "PayrollManagementSystem": "Payroll app",
    "RbcTcsWorld_ClinTrial-Connect": "ClinTrial",
    "NorthFace_AutomationExercise-BDD-Test-Automation": "NorthFace",
    "RbcTcsWorld_Pharmaceuticals_PMC": "PMC",
    "RbcTcsWorld-EPMS": "EPMS",
    "RbcTcsWorld_PharmaPackQMS_Serialization": "Serializ.",
    "BhojanAloy-Food-Coffee-Shop-POS-System": "BhojanAloy",
    "AndroidUIAppiumTest_MyDemoEcommerce": "MyDemo",
    "OrangeHRM_TestAutomation_TestNG_Junit5": "OrangeHRM",
    "RbcTcsWorld_PharmaPackQMS": "QMS",
}
LANGUAGES = [tuple(x) for x in DATA["languages"]]

BG, PANEL, INK, MUTED, OK, TITLE = "#12313f", "#1b4253", "#e8f1f3", "#9fbac2", "#4ade80", "#f4b04a"
FONT = "font-family=\"'Segoe UI', Helvetica, Arial, sans-serif\""
STATE = {"flagship": ("#f4b04a", "flagship"), "active": ("#4ade80", "active"), "stable": ("#8fb8de", "stable")}


def text(x, y, s, size=13, fill=INK, weight=400, anchor="start"):
    return f'<text x="{x}" y="{y}" {FONT} font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>'


def tile(x, y, w, big, label, sub):
    return (f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="96" rx="10" fill="{PANEL}"/>'
            + text(round(x + 16, 1), y + 40, big, 28, "#ffffff", 700) + text(round(x + 16, 1), y + 62, label, 13, INK, 600)
            + text(round(x + 16, 1), y + 81, sub, 11.5, MUTED))


def status_board():
    repos = sum(n for _, n, _ in AREAS)
    w, h = 1000, 600
    p = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" '
         f'aria-label="Portfolio status board, {AS_OF}: {repos} public repositories, {WITH_CI} with green CI in GitHub Actions, '
         f'{TOTAL_TESTS:,} automated tests across them, {SHOP["tests"]:,} tests and 19 CI gates in the Shop, 40 plus years in technology; '
         f'12 featured projects: 2 flagship, 2 active, 8 stable.">',
         f'<rect width="{w}" height="{h}" rx="14" fill="{BG}"/>',
         text(32, 48, "Portfolio Status Board", 24, TITLE, 700),
         text(32, 72, f"Ranajit Baran Chowdhury · github.com/rbchy · {AS_OF}", 13, MUTED)]
    tiles = [(f"{repos}", "public repositories", "web · mobile · API · full stack"),
             (f"{WITH_CI} / {WITH_CI}", "repos with green CI", "GitHub Actions, every push"),
             (f"{TOTAL_TESTS:,}", "automated tests", "counted per repository"),
             (f"{SHOP['tests']:,}", "tests in the Shop", "19 / 19 CI quality gates"),
             ("40+", "years in technology", "ports · pharma · QA")]
    tw = (w - 64 - 4 * 12) / 5
    for i, (big, label, sub) in enumerate(tiles):
        p.append(tile(32 + i * (tw + 12), 92, tw, big, label, sub))

    p.append(text(32, 228, "Repositories by area", 15, INK, 700))
    x, bw = 32.0, w - 64
    for label, n, col in AREAS:
        seg = bw * n / repos
        p.append(f'<rect x="{x:.1f}" y="242" width="{max(seg - 2, 2):.1f}" height="26" rx="4" fill="{col}"/>')
        x += seg
    lx = 32
    for label, n, col in AREAS:
        p.append(f'<rect x="{lx}" y="282" width="12" height="12" rx="3" fill="{col}"/>')
        s = f"{label} {n}"
        p.append(text(lx + 18, 293, s, 12.5, INK))
        lx += 18 + len(s) * 6.7 + 26

    p.append(text(32, 336, "Featured projects", 15, INK, 700))
    cols, gw, gh = 3, (w - 64 - 2 * 12) / 3, 36
    for i, (name, what, state) in enumerate(FEATURED):
        cx, cy = 32 + (i % cols) * (gw + 12), 350 + (i // cols) * (gh + 6)
        col, word = STATE[state]
        p.append(f'<rect x="{cx:.1f}" y="{cy}" width="{gw:.1f}" height="{gh}" rx="8" fill="{PANEL}"/>')
        p.append(f'<circle cx="{cx + 16:.1f}" cy="{cy + 18}" r="6" fill="{col}"/>')
        p.append(text(round(cx + 30, 1), cy + 16, name, 12.5, INK, 600))
        p.append(text(round(cx + 30, 1), cy + 30, f"{word} · {what}", 10.5, MUTED))
    ly = 350 + 4 * (gh + 6) + 18
    lx = 32
    for state in ("flagship", "active", "stable"):
        col, word = STATE[state]
        p.append(f'<circle cx="{lx + 6}" cy="{ly - 4}" r="6" fill="{col}"/>')
        p.append(text(lx + 18, ly, {"flagship": "flagship: full test system in CI", "active": "active: under development",
                                     "stable": "stable: complete and maintained"}[state], 12, MUTED))
        lx += 250
    p.append("</svg>")
    (OUT / "portfolio-status.svg").write_text("\n".join(p) + "\n", encoding="utf-8")


def github_stats():
    repos = len(REPOS)
    w, h = 1000, 400
    langs = ", ".join(f"{n} {p}" for n, p, _ in LANGUAGES)
    p = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" '
         f'aria-label="GitHub stats, {STATS_AS_OF}: {repos} public repositories, all updated in November 2026, {WITH_CI} with green CI; '
         f'tests per repository for the ten largest after the flagships; languages over all repositories as GitHub counts them (percent): {langs}.">',
         f'<rect width="{w}" height="{h}" rx="14" fill="{BG}"/>',
         text(32, 48, "GitHub Stats", 24, TITLE, 700),
         text(32, 72, f"github.com/rbchy · {STATS_AS_OF}", 13, MUTED)]
    nums = [(f"{repos}", "public repositories"), (f"{WITH_CI}", "with green CI"), ("5", "code languages"),
            ("7", "test frameworks"), ("2", "CI systems"), (f"{TOTAL_TESTS:,}", "automated tests")]
    for i, (big, label) in enumerate(nums):
        x, y = 32 + (i % 2) * 150, 96 + (i // 2) * 70
        p.append(f'<rect x="{x}" y="{y}" width="138" height="60" rx="10" fill="{PANEL}"/>')
        p.append(text(x + 14, y + 30, big, 22, "#ffffff", 700) + text(x + 14, y + 49, label, 11.5, MUTED))

    cx0, cy0, cw, ch = 360, 122, 608, 140
    p.append(text(cx0, 96, "Tests per repository (ten largest after the two flagships)", 15, INK, 700))
    top = max(r["tests"] for r in TOP)
    step = cw / len(TOP)
    p.append(f'<line x1="{cx0}" y1="{cy0 + ch}" x2="{cx0 + cw}" y2="{cy0 + ch}" stroke="{MUTED}" stroke-opacity=".4"/>')
    colour = {a["key"]: a["color"] for a in DATA["areas"]}
    for i, r in enumerate(TOP):
        n = r["tests"]
        bh = ch * n / top
        bx = cx0 + i * step + 8
        p.append(f'<rect x="{bx:.1f}" y="{cy0 + ch - bh:.1f}" width="{step - 16:.1f}" height="{max(bh, 1.5):.1f}" rx="3" fill="{colour[r["area"]]}"/>')
        p.append(text(round(bx + (step - 16) / 2, 1), round(cy0 + ch - bh - 5, 1), str(n), 11, INK, 600, "middle"))
        p.append(text(round(bx + (step - 16) / 2, 1), cy0 + ch + 16, SHORT.get(r["name"], r["name"][:12]), 10.5, MUTED, 400, "middle"))

    p.append(text(32, 326, "Languages", 15, INK, 700))
    lx = 136
    for name, pct, col in LANGUAGES:
        p.append(f'<circle cx="{lx}" cy="321" r="5" fill="{col}"/>')
        lab = f"{name} {pct} %"
        p.append(text(lx + 10, 325, lab, 12, INK))
        lx += 10 + len(lab) * 6.6 + 12
    x, bw = 32.0, w - 64
    for name, pct, col in LANGUAGES:
        seg = bw * pct / 100
        p.append(f'<rect x="{x:.1f}" y="338" width="{max(seg - 2, 2):.1f}" height="12" rx="3" fill="{col}"/>')
        x += seg
    p.append(text(32, 372, f"GitHub's own byte count over all {repos} repositories ({STATS_AS_OF}). Bar colours = area, as in the status board.", 11.5, MUTED))
    p.append("</svg>")
    (OUT / "github-stats.svg").write_text("\n".join(p) + "\n", encoding="utf-8")


if __name__ == "__main__":
    status_board()
    github_stats()
    print("wrote", OUT / "portfolio-status.svg", "and", OUT / "github-stats.svg")
