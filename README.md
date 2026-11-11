<div align="center">

# Ranajit Baran Chowdhury · QA Automation Portfolio

### 37 public repositories, each with its own test suite running in GitHub Actions: web, mobile, API and full-stack, in Java, Python, JavaScript and TypeScript

[![Typing SVG](https://readme-typing-svg.demolab.com/?font=Fira+Code&size=18&pause=1500&color=0D9488&center=true&vCenter=true&width=900&repeat=true&lines=QA+Automation+Engineer+%2F+SDET;Selenium+%C2%B7+Playwright+%C2%B7+Cypress+%C2%B7+Appium+%C2%B7+REST+Assured;37+repositories+%C2%B7+36+green+CI+pipelines+%C2%B7+5%2C216+tests)](https://git.io/typing-svg)

[![Portfolio checks](https://github.com/rbchy/ranajitchowdhury/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/ranajitchowdhury/actions/workflows/ci.yml)
[![Open to work](https://img.shields.io/badge/status-open%20to%20work-22c55e?style=for-the-badge)](mailto:chyranajit@gmail.com)
![Role](https://img.shields.io/badge/QA%20Automation%20%2F%20SDET-0d9488?style=for-the-badge)
![Repositories](https://img.shields.io/badge/public%20repositories-37-155e75?style=for-the-badge)
![Green CI](https://img.shields.io/badge/green%20CI-37%20%2F%2037-22c55e?style=for-the-badge&logo=githubactions&logoColor=white)
![Tests](https://img.shields.io/badge/automated%20tests-5%2C216-brightgreen?style=for-the-badge)
![Location](https://img.shields.io/badge/Pennsylvania%2C%20USA-remote%20%2F%20hybrid-1e3a8a?style=for-the-badge)

[GitHub](https://github.com/rbchy) · [LinkedIn](https://www.linkedin.com/in/rbchy/) · [Website](https://rbchy.github.io/rbchy/) (installable app: Android, iPhone, desktop) · [Portfolio](https://rbc6543.wixsite.com/rbc-portfolio) · [chyranajit@gmail.com](mailto:chyranajit@gmail.com)

</div>

Test automation across **web, mobile and API** with **Selenium, Playwright, Cypress, Appium, REST Assured, Postman, Cucumber and Behave**. Each of the 35 code repositories has a GitHub Actions pipeline that builds the project and runs its tests on every push. This portfolio and the profile site (rbchy) check themselves too, which makes 37 pipelines, all green. That is **5,216 automated tests**, counted per repository. Several suites run on real infrastructure: a MySQL 8 service, an Android 13 emulator, or three browsers.

The flagship is a complete test system around an online store: **1,489 tests behind 18 CI quality gates**. Its code now runs **[RbcTcsWorld Shop](https://github.com/rbchy/RbcTcsWorld)** (2,039 tests, 19 gates) on its way to a live store: first an Amazon affiliate site, later its own shop. Behind it are four decades of enterprise systems work, from container terminal management (NAVIS SPARCS N4) to GMP pharmaceutical packaging.

> *"Quality is never an accident; it is always the result of intelligent effort."*

---

## 🚦 Portfolio Status Board

<img src="docs/images/portfolio-status.svg" alt="Portfolio status board, 10 Nov 2026: 37 public repositories, 37 with green CI in GitHub Actions, 5,216 automated tests across them, 2,039 tests and 19 CI gates in the Shop, 40+ years in technology; 12 featured projects: 2 flagship, 2 active, 8 stable" width="100%">

[![Suite CI](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/actions/workflows/ci.yml)
[![Shop CI](https://github.com/rbchy/RbcTcsWorld/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/RbcTcsWorld/actions/workflows/ci.yml)
![Followers](https://img.shields.io/github/followers/rbchy?label=followers)
![Last commit](https://img.shields.io/github/last-commit/rbchy/ranajitchowdhury?label=last%20update)

The cards are drawn from [`docs/portfolio.json`](docs/portfolio.json) (one entry per repository, 10 Nov 2026) by [`docs/images/make_readme_cards.py`](docs/images/make_readme_cards.py). The CI badges in this README are live.

## 📈 GitHub Stats

<img src="docs/images/github-stats.svg" alt="GitHub stats, 10 Nov 2026: 37 public repositories, 37 with green CI, 5,216 automated tests; tests per repository for the ten largest after the flagships: Payroll automation 260, Payroll app 160, ClinTrial 115, NorthFace 85, PMC 81, EPMS 79, Serialization 78, BhojanAloy 76, MyDemo 75, PharmaPack QMS 66; languages: Java 71.6 %, JavaScript 8.9 %, CSS 8.9 %, HTML 3.7 %, TypeScript 3.4 %, Gherkin 1.8 %, Python 0.9 %, other 0.8 %" width="100%">

---

## 🛠️ November 2026: every repository tested in CI

Between 9 and 10 November every repository was brought under the same rule: **the code is checked against its README, real bugs are fixed with a test that can fail, a GitHub Actions pipeline must be green, and the README is rewritten from what CI actually shows.** Some of what that work found:

| Repository | Found and fixed |
|---|---|
| [PayrollManagementSystem](https://github.com/rbchy/PayrollManagementSystem) | the project **did not compile** (5 classes defined twice); the JAR pointed at a main class that does not exist; *Update Employee* used 4 non-existent columns |
| [Payroll automation](https://github.com/rbchy/PayrollManagementSystems_Automation_Java_MySql_Selenium) | the same *Update* SQL bug, proven on a real MySQL; cheque line `… AND 00/100`; `mvn verify` failed after the tests |
| [Amazon Cypress](https://github.com/rbchy/Amazon-Cypress-JavaScript-Automation) | the code was not on GitHub at all; filter, sort and cart steps could never fail. Now a stateful mock, and a mutation check proves the steps catch bugs |
| [AppiumMobileAutomation](https://github.com/rbchy/AppiumMobileAutomation) | only an `assertTrue(true)` test ran; page dumps went to a laptop-only `/Users/...` path; emulator run found below-the-fold controls |
| [QA Brains Python](https://github.com/rbchy/QaBrainsAutomationPythonPlawright) | placeholder steps (`assert True`), always-headed browser; now Chromium + Firefox, with logged recovery from the live site's own crash screen |
| [WebdriverIO demo app](https://github.com/rbchy/WebdriverIO-Native-DemoApp-MobileTestAutomationJavaAppiumTestNG) | Appium 2 / driver 4 mismatch, wrong locators, login fields leaking between tests |
| [BhojanAloy POS](https://github.com/rbchy/BhojanAloy-Food-Coffee-Shop-POS-System) | schema missing the recipe columns; colliding order numbers |
| [NorthFace](https://github.com/rbchy/NorthFace_AutomationExercise-BDD-Test-Automation) · [AmazonSeleniumTest](https://github.com/rbchy/AmazonSeleniumTest) | money rounding, a price parser crash; bot walls are now reported as *skipped, with the reason*, never bypassed |
| [E-Commerce Suite](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite) | vulnerable dependencies upgraded until OSV-Scanner reports 0 |
| [RbcTcsWorld Shop](https://github.com/rbchy/RbcTcsWorld) | Playwright 1.56 no longer installed on the new Ubuntu runner; a flaky photo-upload test traced to the server's *429 busy* answer (DEF-031, fixed with Retry-After handling) |
| [rbchy (profile site)](https://github.com/rbchy/rbchy) | the daily *profile summary cards* job had failed on all 46 runs (no `actions/checkout`); new site checks keep README, website (6 languages) and resume in line with the data |

```mermaid
stateDiagram-v2
    direction LR
    [*] --> Read: clone + read code and README
    Read --> Red: write a test for each real bug
    Red --> Fix: CI shows the failure
    Fix --> Green: CI passes on every push
    Green --> Docs: README rewritten from the CI run
    Docs --> Merged: fast-forward main, main CI green
    Merged --> [*]
    Green --> Red: a new bug or a live-site change
```

---

## 🥧 Breakdown

```mermaid
pie showData
    title 37 public repositories by area
    "Web UI automation" : 16
    "Full-stack applications" : 12
    "Mobile (Appium)" : 5
    "API automation" : 2
    "Portfolio / profile" : 2
```

```mermaid
pie showData
    title 5,216 automated tests by area (latest green CI run per repository)
    "Full-stack applications" : 4525
    "Web UI automation" : 391
    "Mobile (Appium)" : 240
    "API automation" : 60
```

```mermaid
pie showData
    title Languages over all 37 repositories (GitHub byte count, %)
    "Java" : 71.6
    "JavaScript" : 8.9
    "CSS" : 8.9
    "HTML" : 3.7
    "TypeScript" : 3.4
    "Gherkin" : 1.8
    "Python" : 0.9
    "Other" : 0.8
```

```mermaid
pie showData
    title 1,489 tests in the E-Commerce Suite, by level
    "Backend unit + integration" : 772
    "API, DB, BDD, Selenium UI" : 444
    "Playwright (5 browsers/devices)" : 265
    "Appium (Android + iOS)" : 8
```

```mermaid
pie showData
    title 2,039 tests in RbcTcsWorld Shop, by level
    "Backend unit + integration" : 1164
    "API, DB, BDD, Selenium UI" : 464
    "Playwright (5 browsers/devices)" : 403
    "Appium (Android + iOS)" : 8
```

```mermaid
xychart-beta
    title "Tests per repository (excluding the two flagships)"
    x-axis ["Payroll auto", "Payroll", "ClinTrial", "NorthFace", "PMC", "EPMS", "Serializ.", "BhojanAloy", "MyDemo", "OrangeHRM", "QMS", "Appium Andr.", "ApiDemos", "PPES", "Postman", "Cypress Amz"]
    y-axis "Tests" 0 --> 280
    bar [260, 160, 115, 85, 81, 79, 78, 76, 75, 66, 66, 58, 56, 49, 40, 39]
```

```mermaid
xychart-beta
    title "Repositories per tool (as listed in the stack column below)"
    x-axis ["Cucumber", "Selenium", "TestNG", "MySQL", "Appium", "Spring Boot", "Swing", "Playwright", "JUnit 5", "Cypress"]
    y-axis "Repositories" 0 --> 16
    bar [15, 11, 9, 7, 5, 4, 4, 3, 3, 2]
```

---

## 🗺️ How the portfolio fits together

```mermaid
mindmap
  root((rbchy<br/>37 repos))
    Flagship
      E-Commerce Suite · 1,489 tests
      RbcTcsWorld Shop · 2,039 tests
    Full-stack apps
      Pharma: QMS · Serialization · PMC · PPES
      Payroll app + automation
      EPMS · ClinTrial · Inventory · BhojanAloy POS
    Web UI
      QA Brains in 6 stacks
      Amazon · NorthFace · Guru99
      ParaBank · OpenEMR · OrangeHRM x2
      Sauce Demo · Multicart · Sauce Labs cloud
    Mobile
      MyDemo · ApiDemos · WDIO demo
      AppiumMobileAutomation · Android suite
    API
      REST Assured
      Postman / Newman
```

### What is tested, and with what

```mermaid
flowchart LR
    subgraph AUT["🎯 Applications under test"]
        OWN[My own apps<br/>Suite · Shop · Payroll · Pharma · POS]
        PRACTICE[Practice sites<br/>QA Brains · ParaBank · OpenEMR<br/>OrangeHRM · Sauce Demo · Guru99]
        LIVE[Live sites<br/>Amazon · Google · AutomationExercise]
        MOBILE[Android apps<br/>MyDemo · ApiDemos · WDIO demo]
    end
    subgraph FW["🧪 Frameworks"]
        SEL[Selenium + Cucumber / TestNG]
        PW[Playwright<br/>Java · TS · Python]
        CY[Cypress + Cucumber]
        AP[Appium + UiAutomator2]
        API[REST Assured · Postman]
        UNIT[JUnit 5 · real MySQL]
    end
    subgraph CI["⚙️ GitHub Actions"]
        BUILD[build + unit]
        E2E[browsers · emulator · DB service]
        REP[(reports · screenshots · badges)]
    end
    OWN --> UNIT & SEL & PW & AP
    PRACTICE --> SEL & PW & CY & API
    LIVE --> SEL & CY
    MOBILE --> AP
    FW --> BUILD --> E2E --> REP
```

### The pipeline pattern every repository follows

```mermaid
flowchart TD
    P([push · pull request · manual · weekly]) --> B[Build + fast tests<br/>compile · unit · lint · dry-run]
    B -->|green| S{Needs real infrastructure?}
    S -- MySQL --> DB[(MySQL 8 service<br/>schema from repo)]
    S -- browsers --> BR[Chrome · Firefox · Edge<br/>headless]
    S -- Android --> EM[Android 13 emulator<br/>KVM + Appium 2]
    S -- no --> T
    DB & BR & EM --> T[Full test suite<br/>retries off or logged]
    T --> SUM[Step summary:<br/>passed / failed per suite]
    T --> ART[(Artifacts: HTML reports,<br/>screenshots, logs)]
    T --> BADGE[CI badge in the README]
```

### Framework layers (shared by the UI suites)

```mermaid
classDiagram
    direction LR
    class FeatureFile {
        Gherkin scenarios
        tags: smoke, regression
    }
    class StepDefinitions {
        Given / When / Then
        asserts real values
    }
    class PageObject {
        locators
        actions()
        expectations()
    }
    class DriverManager {
        browser / device per test
        config + env overrides
    }
    class Hooks {
        before: start driver
        after: screenshot + page text on failure
    }
    class Reports {
        Cucumber / Allure / Extent
        JUnit XML
    }
    FeatureFile --> StepDefinitions
    StepDefinitions --> PageObject
    PageObject --> DriverManager
    Hooks --> DriverManager
    StepDefinitions ..> Reports
```

### One push, end to end

```mermaid
sequenceDiagram
    autonumber
    actor RB as RB Chowdhury
    participant GH as GitHub
    participant GA as GitHub Actions
    participant ENV as MySQL / browser / emulator
    RB->>GH: git push
    GH->>GA: workflow ci.yml
    GA->>GA: build + unit tests
    GA->>ENV: start the service the suite needs
    GA->>ENV: run the full suite
    ENV-->>GA: results, screenshots
    GA-->>GH: ✅ / ❌ + artifacts + step summary
    GH-->>RB: badge in the README updates
```

---

## ⏱️ Reviewing this in 5 minutes

1. **The flagship:** [RbcTcsWorld E-Commerce Suite](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite). The application is the test object; the work is the test system around it. Start with its README and the [live reports](https://rbchy.github.io/RbcTcsWorld_ECommerceSuite/reports/).
2. **Defects the tests actually found:** [29 defect reports](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/blob/main/docs/qa/DEFECT_REPORTS.md), each with evidence, root cause, fix and regression test.
3. **How release decisions are made:** [Test Strategy](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/blob/main/docs/qa/TEST_STRATEGY.md) · [Risk Register](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/blob/main/docs/qa/RISK_REGISTER.md) · [Traceability (129 requirements)](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/blob/main/docs/qa/TRACEABILITY_MATRIX.md) · [UAT Plan](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/blob/main/docs/qa/UAT_PLAN.md)
4. **From portfolio to live store:** [RbcTcsWorld Shop](https://github.com/rbchy/RbcTcsWorld) and its [roadmap](https://github.com/rbchy/RbcTcsWorld/blob/main/docs/store/ROADMAP.md):
   - integrations: Stripe Elements, Stripe Tax, Shippo, Amazon SES, and a production stack with tested backups
   - 26 decision records and 163 traced requirements
   - it goes live first as an Amazon affiliate site ([ADR-0026](https://github.com/rbchy/RbcTcsWorld/blob/main/docs/adr/0026-partner-only-site.md))
5. **One site, six stacks:** QA Brains in [Python](https://github.com/rbchy/QaBrainsAutomationPythonPlawright), [TypeScript](https://github.com/rbchy/QaBrainsAutomationTypeScriptPlaywright), [Java Playwright](https://github.com/rbchy/QaBrainsAutomationJavaPlaywright), [Java Selenium](https://github.com/rbchy/QaBrainsAutomationJavaSelenium), [Cypress](https://github.com/rbchy/QaBrainsAutomationCypressJavaScript) and [Sauce Labs](https://github.com/rbchy/QaBrainsSauceLabAPI_Automation).
6. **Mobile on a real emulator in CI:** [MyDemo](https://github.com/rbchy/AndroidUIAppiumTest_MyDemoEcommerce) (75 tests) and [AppiumMobileAutomation](https://github.com/rbchy/AppiumMobileAutomation) boot an Android 13 emulator on every push.
7. **Domain depth:** [PharmaPack QMS + Serialization](https://github.com/rbchy/RbcTcsWorld_PharmaPackQMS_Serialization) (GMP packaging, from my work as a pharmaceutical packaging Line Lead).

---

## ⭐ Flagship projects

| Project | What it is | Evidence |
|---|---|---|
| [RbcTcsWorld E-Commerce Suite](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite) | Amazon-inspired store (Java 21, Spring Boot 4.1, PostgreSQL, React) built to be tested: unit, API, contract, DB, BDD, Selenium, Playwright, Appium, accessibility, performance, security, mutation testing | ![tests](https://img.shields.io/badge/tests-1489-brightgreen) ![coverage](https://img.shields.io/badge/lines-97.3%25-brightgreen) ![mutation](https://img.shields.io/badge/mutation-89.3%25-brightgreen) [![CI](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/actions/workflows/ci.yml) |
| [RbcTcsWorld Shop](https://github.com/rbchy/RbcTcsWorld) | The suite's code on its way to a real store: Stripe Elements, Stripe Tax, Shippo labels and returns, Amazon SES, backups, legal pages, Amazon partner products; an affiliate site first, the own shop later | ![stage](https://img.shields.io/badge/stage-affiliate%20site%20first-f59e0b) ![tests](https://img.shields.io/badge/tests-2039-brightgreen) ![coverage](https://img.shields.io/badge/lines-97.5%25-brightgreen) ![mutation](https://img.shields.io/badge/mutation-86.9%25-brightgreen) [![CI](https://github.com/rbchy/RbcTcsWorld/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/RbcTcsWorld/actions/workflows/ci.yml) |

---

## 📂 Projects by area

Every row comes from [`docs/portfolio.json`](docs/portfolio.json). The CI column shows each repository's live GitHub Actions badge.

<!-- projects:start -->

### 💻 Full-stack applications (each tested in CI) · 12 repositories · 4,525 tests

| Project | Stack | Latest CI result | CI |
|---|---|---|---|
| [RbcTcsWorld](https://github.com/rbchy/RbcTcsWorld) ⭐ | Java 21 · Spring Boot · PostgreSQL · React · Stripe · Shippo · SES | 2,039 tests · 19 / 19 gates · 0 flaky | [![CI](https://github.com/rbchy/RbcTcsWorld/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/RbcTcsWorld/actions/workflows/ci.yml) |
| [RbcTcsWorld\_ECommerceSuite](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite) ⭐ | Java 21 · Spring Boot 4.1 · PostgreSQL · React | 1,489 tests · 18 / 18 gates | [![CI](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/actions/workflows/ci.yml) |
| [PayrollManagementSystems\_Automation\_Java\_MySql\_Selenium](https://github.com/rbchy/PayrollManagementSystems_Automation_Java_MySql_Selenium) | Java 21 · Swing · MySQL · JUnit 5 · Cucumber · AssertJ-Swing | 260 / 260 · real MySQL | [![CI](https://github.com/rbchy/PayrollManagementSystems_Automation_Java_MySql_Selenium/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/PayrollManagementSystems_Automation_Java_MySql_Selenium/actions/workflows/ci.yml) |
| [PayrollManagementSystem](https://github.com/rbchy/PayrollManagementSystem) | Java 21 · Swing · MySQL · JUnit 5 | 160 / 160 · real MySQL | [![CI](https://github.com/rbchy/PayrollManagementSystem/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/PayrollManagementSystem/actions/workflows/ci.yml) |
| [RbcTcsWorld\_ClinTrial-Connect](https://github.com/rbchy/RbcTcsWorld_ClinTrial-Connect) | Spring Boot · JMeter | 115 / 115 | [![CI](https://github.com/rbchy/RbcTcsWorld_ClinTrial-Connect/actions/workflows/tests.yml/badge.svg)](https://github.com/rbchy/RbcTcsWorld_ClinTrial-Connect/actions/workflows/tests.yml) |
| [RbcTcsWorld\_Pharmaceuticals\_PMC](https://github.com/rbchy/RbcTcsWorld_Pharmaceuticals_PMC) | Java · Swing · MySQL | 81 / 81 | [![CI](https://github.com/rbchy/RbcTcsWorld_Pharmaceuticals_PMC/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/RbcTcsWorld_Pharmaceuticals_PMC/actions/workflows/ci.yml) |
| [RbcTcsWorld-EPMS](https://github.com/rbchy/RbcTcsWorld-EPMS) | Spring Boot REST API · MySQL | 79 / 79 | [![CI](https://github.com/rbchy/RbcTcsWorld-EPMS/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/RbcTcsWorld-EPMS/actions/workflows/ci.yml) |
| [RbcTcsWorld\_PharmaPackQMS\_Serialization](https://github.com/rbchy/RbcTcsWorld_PharmaPackQMS_Serialization) | Java · desktop builds (Windows, macOS, Linux) | 78 / 78 | [![CI](https://github.com/rbchy/RbcTcsWorld_PharmaPackQMS_Serialization/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/RbcTcsWorld_PharmaPackQMS_Serialization/actions/workflows/ci.yml) |
| [BhojanAloy-Food-Coffee-Shop-POS-System](https://github.com/rbchy/BhojanAloy-Food-Coffee-Shop-POS-System) | Java Swing · MySQL | 76 / 76 | [![CI](https://github.com/rbchy/BhojanAloy-Food-Coffee-Shop-POS-System/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/BhojanAloy-Food-Coffee-Shop-POS-System/actions/workflows/ci.yml) |
| [RbcTcsWorld\_PharmaPackQMS](https://github.com/rbchy/RbcTcsWorld_PharmaPackQMS) | Java · GMP packaging QMS | 66 / 66 | [![CI](https://github.com/rbchy/RbcTcsWorld_PharmaPackQMS/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/RbcTcsWorld_PharmaPackQMS/actions/workflows/ci.yml) |
| [PPES-Pharmaceutical-Packaging-Management](https://github.com/rbchy/PPES-Pharmaceutical-Packaging-Management) | Java 17 · MySQL 8 · DAO / MVC | 49 / 49 | [![CI](https://github.com/rbchy/PPES-Pharmaceutical-Packaging-Management/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/PPES-Pharmaceutical-Packaging-Management/actions/workflows/ci.yml) |
| [InventoryControlManagement\_JavaMySql](https://github.com/rbchy/InventoryControlManagement_JavaMySql) | Java 17 · MySQL 8 · JDBC | 33 / 33 | [![CI](https://github.com/rbchy/InventoryControlManagement_JavaMySql/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/InventoryControlManagement_JavaMySql/actions/workflows/ci.yml) |

### 🌐 Web UI automation (BDD) · 16 repositories · 391 tests

| Project | Stack | Latest CI result | CI |
|---|---|---|---|
| [NorthFace\_AutomationExercise-BDD-Test-Automation](https://github.com/rbchy/NorthFace_AutomationExercise-BDD-Test-Automation) | Java · Selenium · Cucumber · API · a11y · perf | 83 passed · 2 skipped (bot wall) | [![CI](https://github.com/rbchy/NorthFace_AutomationExercise-BDD-Test-Automation/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/NorthFace_AutomationExercise-BDD-Test-Automation/actions/workflows/ci.yml) |
| [OrangeHRM\_TestAutomation\_TestNG\_Junit5](https://github.com/rbchy/OrangeHRM_TestAutomation_TestNG_Junit5) | Java · Selenium · TestNG · JUnit 5 | 66 / 66 | [![CI](https://github.com/rbchy/OrangeHRM_TestAutomation_TestNG_Junit5/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/OrangeHRM_TestAutomation_TestNG_Junit5/actions/workflows/ci.yml) |
| [Amazon-Cypress-JavaScript-Automation](https://github.com/rbchy/Amazon-Cypress-JavaScript-Automation) | JavaScript · Cypress 14 · Cucumber | 39 / 39 × Chrome · Firefox · Edge | [![CI](https://github.com/rbchy/Amazon-Cypress-JavaScript-Automation/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/Amazon-Cypress-JavaScript-Automation/actions/workflows/ci.yml) |
| [Guru99TelTest](https://github.com/rbchy/Guru99TelTest) | Java · Selenium · TestNG | 29 / 29 | [![CI](https://github.com/rbchy/Guru99TelTest/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/Guru99TelTest/actions/workflows/ci.yml) |
| [ParaBank-BankingAutomationJavaSelenium](https://github.com/rbchy/ParaBank-BankingAutomationJavaSelenium) | Java · Selenium · Cucumber | 20 / 20 | [![CI](https://github.com/rbchy/ParaBank-BankingAutomationJavaSelenium/actions/workflows/tests.yml/badge.svg)](https://github.com/rbchy/ParaBank-BankingAutomationJavaSelenium/actions/workflows/tests.yml) |
| [AmazonSeleniumTest](https://github.com/rbchy/AmazonSeleniumTest) | Java · Selenium · Cucumber | 19 / 19 unit · live runs skip on bot wall | [![CI](https://github.com/rbchy/AmazonSeleniumTest/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/AmazonSeleniumTest/actions/workflows/ci.yml) |
| [Multicart\_Demo\_Automation](https://github.com/rbchy/Multicart_Demo_Automation) | Java · Selenium · Cucumber | 17 / 17 | [![CI](https://github.com/rbchy/Multicart_Demo_Automation/actions/workflows/tests.yml/badge.svg)](https://github.com/rbchy/Multicart_Demo_Automation/actions/workflows/tests.yml) |
| [Sauce-Demo.MyShopify.AutomationTest](https://github.com/rbchy/Sauce-Demo.MyShopify.AutomationTest) | Java · Selenium · Cucumber | 17 / 17 | [![CI](https://github.com/rbchy/Sauce-Demo.MyShopify.AutomationTest/actions/workflows/tests.yml/badge.svg)](https://github.com/rbchy/Sauce-Demo.MyShopify.AutomationTest/actions/workflows/tests.yml) |
| [QaBrainsAutomationPythonPlawright](https://github.com/rbchy/QaBrainsAutomationPythonPlawright) | Python · Playwright · Behave | 15 / 15 × Chromium · Firefox | [![CI](https://github.com/rbchy/QaBrainsAutomationPythonPlawright/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/QaBrainsAutomationPythonPlawright/actions/workflows/ci.yml) |
| [QaBrainsAutomationTypeScriptPlaywright](https://github.com/rbchy/QaBrainsAutomationTypeScriptPlaywright) | TypeScript · Playwright · Cucumber.js | 15 / 15 | [![CI](https://github.com/rbchy/QaBrainsAutomationTypeScriptPlaywright/actions/workflows/tests.yml/badge.svg)](https://github.com/rbchy/QaBrainsAutomationTypeScriptPlaywright/actions/workflows/tests.yml) |
| [QaBrainsAutomationJavaPlaywright](https://github.com/rbchy/QaBrainsAutomationJavaPlaywright) | Java · Playwright · Cucumber · TestNG | 15 / 15 | [![CI](https://github.com/rbchy/QaBrainsAutomationJavaPlaywright/actions/workflows/tests.yml/badge.svg)](https://github.com/rbchy/QaBrainsAutomationJavaPlaywright/actions/workflows/tests.yml) |
| [QaBrainsAutomationJavaSelenium](https://github.com/rbchy/QaBrainsAutomationJavaSelenium) | Java · Selenium · Cucumber · TestNG | 15 / 15 | [![CI](https://github.com/rbchy/QaBrainsAutomationJavaSelenium/actions/workflows/tests.yml/badge.svg)](https://github.com/rbchy/QaBrainsAutomationJavaSelenium/actions/workflows/tests.yml) |
| [QaBrainsAutomationCypressJavaScript](https://github.com/rbchy/QaBrainsAutomationCypressJavaScript) | JavaScript · Cypress · Cucumber | 15 / 15 | [![CI](https://github.com/rbchy/QaBrainsAutomationCypressJavaScript/actions/workflows/tests.yml/badge.svg)](https://github.com/rbchy/QaBrainsAutomationCypressJavaScript/actions/workflows/tests.yml) |
| [QaBrainsSauceLabAPI\_Automation](https://github.com/rbchy/QaBrainsSauceLabAPI_Automation) | Java · Selenium · Cucumber · Sauce Labs | 15 / 15 headless | [![CI](https://github.com/rbchy/QaBrainsSauceLabAPI_Automation/actions/workflows/tests.yml/badge.svg)](https://github.com/rbchy/QaBrainsSauceLabAPI_Automation/actions/workflows/tests.yml) |
| [OrangeHRM\_Automation](https://github.com/rbchy/OrangeHRM_Automation) | Java · Selenium · Cucumber | 5 / 5 | [![CI](https://github.com/rbchy/OrangeHRM_Automation/actions/workflows/tests.yml/badge.svg)](https://github.com/rbchy/OrangeHRM_Automation/actions/workflows/tests.yml) |
| [OpenEMR\_Automation](https://github.com/rbchy/OpenEMR_Automation) | Java · Selenium · Cucumber | 4 / 4 | [![CI](https://github.com/rbchy/OpenEMR_Automation/actions/workflows/tests.yml/badge.svg)](https://github.com/rbchy/OpenEMR_Automation/actions/workflows/tests.yml) |

### 📱 Mobile (Appium, Android emulator in CI) · 5 repositories · 240 tests

| Project | Stack | Latest CI result | CI |
|---|---|---|---|
| [AndroidUIAppiumTest\_MyDemoEcommerce](https://github.com/rbchy/AndroidUIAppiumTest_MyDemoEcommerce) | Java 17 · Appium · UiAutomator2 · TestNG | 75 / 75 · emulator | [![CI](https://github.com/rbchy/AndroidUIAppiumTest_MyDemoEcommerce/actions/workflows/tests.yml/badge.svg)](https://github.com/rbchy/AndroidUIAppiumTest_MyDemoEcommerce/actions/workflows/tests.yml) |
| [AppiumTest\_Andriod\_Automation](https://github.com/rbchy/AppiumTest_Andriod_Automation) | Java · Appium · TestNG | 55 passed · 3 skipped · emulator | [![CI](https://github.com/rbchy/AppiumTest_Andriod_Automation/actions/workflows/tests.yml/badge.svg)](https://github.com/rbchy/AppiumTest_Andriod_Automation/actions/workflows/tests.yml) |
| [AppiumAutomation\_ApiDemos](https://github.com/rbchy/AppiumAutomation_ApiDemos) | Java 17 · Appium 3 · TestNG | 56 / 56 · emulator | [![CI](https://github.com/rbchy/AppiumAutomation_ApiDemos/actions/workflows/tests.yml/badge.svg)](https://github.com/rbchy/AppiumAutomation_ApiDemos/actions/workflows/tests.yml) |
| [AppiumMobileAutomation](https://github.com/rbchy/AppiumMobileAutomation) | Java · Appium 2 · TestNG · Allure | 22 device + 8 unit · emulator | [![CI](https://github.com/rbchy/AppiumMobileAutomation/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/AppiumMobileAutomation/actions/workflows/ci.yml) |
| [WebdriverIO-Native-DemoApp-MobileTestAutomationJavaAppiumTestNG](https://github.com/rbchy/WebdriverIO-Native-DemoApp-MobileTestAutomationJavaAppiumTestNG) | Java · Appium 2 · TestNG | 21 / 21 · emulator | [![CI](https://github.com/rbchy/WebdriverIO-Native-DemoApp-MobileTestAutomationJavaAppiumTestNG/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/WebdriverIO-Native-DemoApp-MobileTestAutomationJavaAppiumTestNG/actions/workflows/ci.yml) |

### 🔌 API testing · 2 repositories · 60 tests

| Project | Stack | Latest CI result | CI |
|---|---|---|---|
| [QaBrainsAPIAutomation\_Postman](https://github.com/rbchy/QaBrainsAPIAutomation_Postman) | Postman · Newman | 40 / 40 assertions | [![CI](https://github.com/rbchy/QaBrainsAPIAutomation_Postman/actions/workflows/tests.yml/badge.svg)](https://github.com/rbchy/QaBrainsAPIAutomation_Postman/actions/workflows/tests.yml) |
| [QaBrainsAPIAutomationRestAssured](https://github.com/rbchy/QaBrainsAPIAutomationRestAssured) | Java · REST Assured · Cucumber | 5 API + 15 UI | [![CI](https://github.com/rbchy/QaBrainsAPIAutomationRestAssured/actions/workflows/tests.yml/badge.svg)](https://github.com/rbchy/QaBrainsAPIAutomationRestAssured/actions/workflows/tests.yml) |

### 🪪 Portfolio and profile · 2 repositories

| Project | Stack | Latest CI result | CI |
|---|---|---|---|
| [rbchy](https://github.com/rbchy/rbchy) | GitHub profile · website · installable app | site, i18n and README checks | [![CI](https://github.com/rbchy/rbchy/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/rbchy/actions/workflows/ci.yml) |
| [ranajitchowdhury](https://github.com/rbchy/ranajitchowdhury) | this portfolio | README checks | [![CI](https://github.com/rbchy/ranajitchowdhury/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/ranajitchowdhury/actions/workflows/ci.yml) |

<!-- projects:end -->

---

## 🛠️ Skills

| Area | Tools |
|---|---|
| Languages | Java · Python · TypeScript · JavaScript · SQL |
| Web UI | Selenium 4 · Playwright · Cypress · Page Object Model |
| Mobile | Appium 2 / 3 · UiAutomator2 (Android) · XCUITest (iOS) · Android emulator in CI |
| BDD and runners | Cucumber · Behave · TestNG · JUnit 5 · pytest |
| API | REST Assured · Postman / Newman · JSON Schema contracts · OpenAPI diff |
| Quality engineering | JaCoCo coverage · PIT mutation testing · axe-core accessibility · k6 / JMeter performance · OWASP ZAP · OSV-Scanner |
| CI/CD and delivery | GitHub Actions · Jenkins · Docker / Compose · Maven · npm |
| Reporting | Allure · ExtentReports · Cucumber HTML · Playwright HTML |
| Cloud and data | Sauce Labs · AWS basics · PostgreSQL · MySQL · Oracle · Redis |
| Ways of working | Agile Scrum · SDLC / STLC · risk-based testing · traceability · UAT · Jira |

---

## 👨‍💼 Career

```mermaid
timeline
    title Four decades in technology
    1979 - 2016 : Chittagong Port Authority, Bangladesh
                : NAVIS SPARCS N4 super user · CTMS · container billing · MIS
    1990 - 1995 : The Computer Systems, Bangladesh
                : system consultant, designer, programmer
    2016 - now  : RbcTcsWorld (self-employed)
                : QA automation engineer · system designer · developer
    2022 - now  : Sharp Packaging Services LLC
                : Line Lead, GMP pharmaceutical blister packaging
    2026        : 37 public repositories, all tested in GitHub Actions
```

| Years | Role |
|---|---|
| 2022 - present | **Sharp Packaging Services LLC**: Line Lead in pharmaceutical blister packaging (primary and secondary). Leads teams of up to 25 operators; batch records and line clearance, serialization, GMP, FDA regulations, OEB handling |
| 2016 - present | **RbcTcsWorld** (self-employed): QA automation engineer, system designer and developer |
| 1990 - 1995 | **The Computer Systems**, Bangladesh: system consultant, designer and programmer |
| 1979 - 2016 | **Chittagong Port Authority**, Bangladesh: NAVIS SPARCS N4 super user (CTMS configuration, container billing, MIS, team training) |

**Education:** Master's in Public Administration, University of Chittagong (1984-1985).

---

## ⚙️ How this README is kept honest

This repository has its own CI ([`ci.yml`](.github/workflows/ci.yml)). It runs on every push and once a week:

- **Data and tables:** the project tables must match `docs/portfolio.json`, and every number in the cards must add up (areas, tests, CI count).
- **Cards:** `make_readme_cards.py` must redraw exactly the committed SVG cards.
- **Charts:** every Mermaid chart in this README must render.
- **CI for every repo:** each repository listed with a workflow must have a CI badge that GitHub serves.

---

## 📫 Contact

| | |
|---|---|
| Email | [chyranajit@gmail.com](mailto:chyranajit@gmail.com) |
| Location | West Norriton, Pennsylvania 19403, USA · open to remote and hybrid |
| Phone | +1 (267) 342-5565 |
| LinkedIn | [linkedin.com/in/rbchy](https://www.linkedin.com/in/rbchy/) |
| GitHub | [github.com/rbchy](https://github.com/rbchy) |
| Website | [rbchy.github.io/rbchy](https://rbchy.github.io/rbchy/) · [Wix portfolio](https://rbc6543.wixsite.com/rbc-portfolio) |
| App | Open the website and press **Install app** (Android, Windows, Mac), or on iPhone use Safari → *Add to Home Screen*. Works offline · [Android build](https://github.com/rbchy/rbchy/actions/workflows/android-app.yml) |

**Available for:** full-time · contract · freelance QA Automation Engineer / SDET roles.

---

No portfolio proves a tester is good. This one shows the work instead: frameworks built from scratch, tests that found real defects, and a green CI run behind every number.
