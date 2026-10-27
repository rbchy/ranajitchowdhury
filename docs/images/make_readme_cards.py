#!/usr/bin/env python3
"""
Draws the two README cards of this portfolio: the Portfolio Status Board and the GitHub Stats card
(plain SVG, no dependencies), in the same style as the cards of the E-Commerce Suite README.

The numbers are copied from GitHub (the repository list of github.com/rbchy and the CI run of the flagship
projects) on the date below; update them and run `python3 docs/images/make_readme_cards.py`.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent
AS_OF = "26 Oct 2026"

# ---- github.com/rbchy, 26 Oct 2026 ----
AREAS = [  # (label, repositories, colour)
    ("Web UI automation", 16, "#4fb3a9"),
    ("Full-stack applications", 12, "#f4b04a"),
    ("Mobile (Appium)", 5, "#8fb8de"),
    ("API automation", 2, "#e58a8a"),
    ("Portfolio / profile", 2, "#b7a3e0"),
]
# (project, what it shows, state) - state: flagship | active | stable
FEATURED = [
    ("RbcTcsWorld E-Commerce Suite", "1,497 tests · 18 CI gates", "flagship"),
    ("RbcTcsWorld Shop", "live-store roadmap · phase 2 next", "flagship"),
    ("PharmaPack QMS + Serialization", "GMP packaging · desktop builds", "active"),
    ("ClinTrial-Connect", "Spring Boot · 115+ tests", "active"),
    ("QA Brains: Python Playwright", "12 passed · 0 failed", "stable"),
    ("QA Brains: TypeScript Playwright", "14 passed · 0 failed", "stable"),
    ("QA Brains: Java Playwright", "Cucumber JVM · TestNG", "stable"),
    ("Appium Mobile Automation", "23 / 23 · 100 % pass", "stable"),
    ("OpenEMR Healthcare", "Selenium · Cucumber", "stable"),
    ("Sauce Labs Cloud", "20+ browser/OS combos", "stable"),
    ("API: REST Assured + Postman", "auth · data-driven", "stable"),
    ("Payroll Management System", "Java Swing · MySQL", "stable"),
]
# last push of each repository, by month (37 repositories)
LAST_PUSH = [("Dec 24", 1), ("Dec 25", 1), ("May 26", 5), ("Jun 26", 14), ("Jul 26", 7), ("Aug 26", 1),
             ("Sep 26", 5), ("Oct 26", 3)]
# the test languages and frameworks the repositories use (4 languages, 6 frameworks, plus BDD runners)
TOOLS = [("Java", "#b07219"), ("JavaScript", "#f1e05a"), ("TypeScript", "#3178c6"), ("Python", "#3572A5"),
         ("Selenium", "#43b02a"), ("Playwright", "#45ba4b"), ("Cypress", "#9fbac2"), ("Appium", "#a78bfa"),
         ("REST Assured", "#43b02a"), ("Postman", "#ff6c37"), ("Cucumber", "#23d96c"), ("TestNG", "#f4b04a")]

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
         f'aria-label="Portfolio status board: {repos} public repositories, 2 flagship applications, 1,497 automated tests '
         f'and 18 CI quality gates in the flagship, 40 plus years in technology; 12 featured projects: 2 flagship, 2 active, 8 stable.">',
         f'<rect width="{w}" height="{h}" rx="14" fill="{BG}"/>',
         text(32, 48, "Portfolio Status Board", 24, TITLE, 700),
         text(32, 72, f"Ranajit Baran Chowdhury · github.com/rbchy · {AS_OF}", 13, MUTED)]
    tiles = [(f"{repos}", "public repositories", "web · mobile · API · full stack"),
             ("2", "flagship applications", "E-Commerce Suite · Shop"),
             ("1,497", "automated tests", "in the flagship, every push"),
             ("18 / 18", "CI quality gates", "GitHub Actions + Jenkins"),
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
    repos = sum(n for _, n in LAST_PUSH)
    w, h = 1000, 400
    p = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" '
         f'aria-label="GitHub stats: {repos} public repositories, 35 updated in 2026; tests in Java, JavaScript, TypeScript and Python with Selenium, Playwright, Cypress, Appium, REST Assured and Postman.">',
         f'<rect width="{w}" height="{h}" rx="14" fill="{BG}"/>',
         text(32, 48, "GitHub Stats", 24, TITLE, 700),
         text(32, 72, f"github.com/rbchy · {AS_OF}", 13, MUTED)]
    nums = [(f"{repos}", "public repositories"), ("35", "updated in 2026"), ("4", "languages in tests"),
            ("6", "test frameworks"), ("2", "CI systems"), ("1,497", "tests in one project")]
    for i, (big, label) in enumerate(nums):
        x, y = 32 + (i % 2) * 150, 96 + (i // 2) * 70
        p.append(f'<rect x="{x}" y="{y}" width="138" height="60" rx="10" fill="{PANEL}"/>')
        p.append(text(x + 14, y + 30, big, 22, "#ffffff", 700) + text(x + 14, y + 49, label, 11.5, MUTED))

    cx0, cy0, cw, ch = 360, 122, 608, 158
    p.append(text(cx0, 96, "Repositories by month of their last update", 15, INK, 700))
    top = max(n for _, n in LAST_PUSH)
    step = cw / len(LAST_PUSH)
    p.append(f'<line x1="{cx0}" y1="{cy0 + ch}" x2="{cx0 + cw}" y2="{cy0 + ch}" stroke="{MUTED}" stroke-opacity=".4"/>')
    for i, (month, n) in enumerate(LAST_PUSH):
        bh = ch * n / top
        bx = cx0 + i * step + 10
        p.append(f'<rect x="{bx:.1f}" y="{cy0 + ch - bh:.1f}" width="{step - 20:.1f}" height="{max(bh, 1.5):.1f}" rx="3" fill="#4fb3a9"/>')
        p.append(text(round(bx + (step - 20) / 2, 1), round(cy0 + ch - bh - 5, 1), str(n), 11, INK, 600, "middle"))
        p.append(text(round(bx + (step - 20) / 2, 1), cy0 + ch + 16, month, 11, MUTED, 400, "middle"))

    p.append(text(32, 330, "Languages and tools", 15, INK, 700))
    lx, ly = 196, 314
    for name, col in TOOLS:
        cw = len(name) * 7 + 30
        if lx + cw > w - 32:
            lx, ly = 196, ly + 32
        p.append(f'<rect x="{lx}" y="{ly}" width="{cw}" height="24" rx="12" fill="{PANEL}"/>')
        p.append(f'<circle cx="{lx + 12}" cy="{ly + 12}" r="5" fill="{col}"/>')
        p.append(text(lx + 22, ly + 16, name, 12, INK))
        lx += cw + 6
    p.append("</svg>")
    (OUT / "github-stats.svg").write_text("\n".join(p) + "\n", encoding="utf-8")


if __name__ == "__main__":
    status_board()
    github_stats()
    print("wrote", OUT / "portfolio-status.svg", "and", OUT / "github-stats.svg")
