#!/usr/bin/env python3
"""Writes the "Projects by area" tables of README.md from docs/portfolio.json.

The tables sit between <!-- projects:start --> and <!-- projects:end -->. Run
`python3 docs/make_project_tables.py`; with --check it only reports whether the
README is up to date (used by CI).
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "docs" / "portfolio.json").read_text(encoding="utf-8"))
START, END = "<!-- projects:start -->", "<!-- projects:end -->"

TITLES = {
    "app": "💻 Full-stack applications (each tested in CI)",
    "web": "🌐 Web UI automation (BDD)",
    "mobile": "📱 Mobile (Appium, Android emulator in CI)",
    "api": "🔌 API testing",
    "profile": "🪪 Portfolio and profile",
}
ORDER = ["app", "web", "mobile", "api", "profile"]


def ci_badge(repo):
    if not repo["workflow"]:
        return "—"
    url = f"https://github.com/rbchy/{repo['name']}/actions/workflows/{repo['workflow']}"
    return f"[![CI]({url}/badge.svg)]({url})"


def render():
    out = [START, ""]
    for key in ORDER:
        rows = [r for r in DATA["repos"] if r["area"] == key]
        tests = sum(r["tests"] for r in rows)
        out.append(f"### {TITLES[key]} · {len(rows)} repositories" + (f" · {tests:,} tests" if tests else ""))
        out.append("")
        out.append("| Project | Stack | Latest CI result | CI |")
        out.append("|---|---|---|---|")
        for r in rows:
            name = r["name"].replace("_", "\\_")
            star = " ⭐" if r.get("flagship") else ""
            out.append(f"| [{name}](https://github.com/rbchy/{r['name']}){star} | {r['stack']} | {r['result']} | {ci_badge(r)} |")
        out.append("")
    out.append(END)
    return "\n".join(out)


def main():
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    if START not in text or END not in text:
        sys.exit(f"README.md has no {START} ... {END} block")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new = head + render() + tail
    if "--check" in sys.argv:
        if new != text:
            sys.exit("README.md project tables are out of date: run python3 docs/make_project_tables.py")
        print("README project tables are up to date")
        return
    readme.write_text(new, encoding="utf-8")
    print("wrote the project tables into README.md")


if __name__ == "__main__":
    main()
