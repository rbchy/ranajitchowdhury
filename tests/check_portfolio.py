#!/usr/bin/env python3
"""Consistency checks for the portfolio README (run in CI, no network needed).

- docs/portfolio.json is well formed: unique names, known areas, numbers >= 0
- the pie charts in README.md match the data (repositories by area, tests by area)
- the headline numbers in README.md (repositories, green CI, total tests) match the data
- every repository in the data appears in README.md, and nothing unknown is listed
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "docs" / "portfolio.json").read_text(encoding="utf-8"))
README = (ROOT / "README.md").read_text(encoding="utf-8")
problems = []


def check(cond, msg):
    if not cond:
        problems.append(msg)


repos = DATA["repos"]
areas = {a["key"]: a["label"] for a in DATA["areas"]}
names = [r["name"] for r in repos]
check(len(names) == len(set(names)), f"duplicate repositories: {[n for n, c in Counter(names).items() if c > 1]}")
for r in repos:
    check(r["area"] in areas, f"{r['name']}: unknown area {r['area']}")
    check(isinstance(r["tests"], int) and r["tests"] >= 0, f"{r['name']}: tests must be a non-negative int")
check(abs(sum(x[1] for x in DATA["languages"]) - 100) < 0.05, "language percentages must add up to 100")

total_tests = sum(r["tests"] for r in repos)
with_ci = sum(1 for r in repos if r["workflow"])


def pie(title_part):
    m = re.search(r"```mermaid\s*\npie[^\n]*\n\s*title [^\n]*" + re.escape(title_part) + r"[^\n]*\n(.*?)```", README, re.S)
    if not m:
        problems.append(f"no pie chart titled '...{title_part}...'")
        return {}
    return {k: float(v) for k, v in re.findall(r'"([^"]+)"\s*:\s*([\d.]+)', m.group(1))}


by_area = pie("public repositories by area")
for key, label in areas.items():
    want = sum(1 for r in repos if r["area"] == key)
    check(by_area.get(label) == want, f"pie 'repositories by area': {label} is {by_area.get(label)}, data says {want}")

tests_area = pie("automated tests by area")
for key, label in areas.items():
    want = sum(r["tests"] for r in repos if r["area"] == key)
    if want:
        check(tests_area.get(label) == want, f"pie 'tests by area': {label} is {tests_area.get(label)}, data says {want}")
check(f"{total_tests:,} automated tests" in README, f"README should say '{total_tests:,} automated tests'")
check(f"{len(repos)} public repositories" in README, f"README should say '{len(repos)} public repositories'")
check(f"green%20CI-{with_ci}%20%2F%20{with_ci}" in README, f"green-CI badge should read {with_ci} / {with_ci}")

linked = set(re.findall(r"github\.com/rbchy/([A-Za-z0-9_.-]+)", README))
for n in names:
    check(n in linked, f"{n} is in portfolio.json but not linked in README.md")
unknown = sorted(l for l in linked if l not in names and l not in {"rbchy?tab=repositories"})
check(not unknown, f"README links to repositories that are not in portfolio.json: {unknown}")

if problems:
    print("\n".join(f"✗ {p}" for p in problems))
    sys.exit(1)
print(f"✓ {len(repos)} repositories · {with_ci} with CI · {total_tests:,} tests · README and data agree")
