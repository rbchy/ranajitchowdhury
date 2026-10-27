# Ranajit Baran Chowdhury - QA Automation Portfolio

[![Open to work](https://img.shields.io/badge/status-open%20to%20work-22c55e)](mailto:chyranajit@gmail.com)
![Role](https://img.shields.io/badge/QA%20Automation%20%2F%20SDET-0d9488)
![Repositories](https://img.shields.io/badge/public%20repositories-37-155e75)
![Flagship tests](https://img.shields.io/badge/flagship%20tests-1497-brightgreen)
![CI gates](https://img.shields.io/badge/CI%20quality%20gates-18-brightgreen)
![Location](https://img.shields.io/badge/Pennsylvania%2C%20USA-remote%20%2F%20hybrid-1e3a8a)

Test automation across **web, mobile and API**, in **Java, Python, JavaScript and TypeScript**, with **Selenium,
Playwright, Cypress, Appium, REST Assured, Postman and Cucumber**. 37 public repositories: e-commerce, banking,
healthcare, HR, pharmaceutical packaging and cloud testing. The flagship is a complete test system around an online
store: 1,497 automated tests behind 18 CI quality gates in GitHub Actions and Jenkins. Behind it are four decades of
enterprise systems work, from container terminal management (NAVIS SPARCS N4) to GMP pharmaceutical packaging.

Author: **Ranajit Baran (RB) Chowdhury**, QA Automation Engineer / SDET -
[GitHub](https://github.com/rbchy) · [LinkedIn](https://www.linkedin.com/in/rbchy/) ·
[Website](https://rbchy.github.io/rbchy/) · [Portfolio](https://rbc6543.wixsite.com/rbc-portfolio) ·
[chyranajit@gmail.com](mailto:chyranajit@gmail.com)

> *"Quality is never an accident; it is always the result of intelligent effort."*

---

## 🚦 Portfolio Status Board

<img src="docs/images/portfolio-status.svg" alt="Portfolio status board: 37 public repositories, 2 flagship applications, 1,497 automated tests and 18 CI quality gates in the flagship, 40+ years in technology; 12 featured projects: 2 flagship, 2 active, 8 stable" width="100%">

[![Suite CI](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/actions/workflows/ci.yml)
[![Shop CI](https://github.com/rbchy/RbcTcsWorld/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/RbcTcsWorld/actions/workflows/ci.yml)
![Followers](https://img.shields.io/github/followers/rbchy?label=followers)
![Last commit](https://img.shields.io/github/last-commit/rbchy/ranajitchowdhury?label=last%20update)

The board is a snapshot of 26 Oct 2026, redrawn with [`docs/images/make_readme_cards.py`](docs/images/make_readme_cards.py);
the CI badges above are live.

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
    title 1,497 tests in the flagship, by level
    "Backend unit + integration" : 772
    "API, DB, BDD, Selenium UI" : 444
    "Playwright (5 browsers/devices)" : 273
    "Appium (Android + iOS)" : 8
```

## 📈 GitHub Stats

<img src="docs/images/github-stats.svg" alt="GitHub stats: 37 public repositories, 35 updated in 2026; languages over all repositories with committed test-report HTML left out: Java 67.0 %, CSS 13.9 %, JavaScript 10.6 %, TypeScript 4.2 %, Gherkin 2.4 %, Python 1.1 %, other 0.8 %" width="100%">

---

## Reviewing this in 5 minutes

1. **The flagship:** [RbcTcsWorld E-Commerce Suite](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite) - the
   application is the test object; the work is the test system around it. Start with its README and the
   [live reports](https://rbchy.github.io/RbcTcsWorld_ECommerceSuite/reports/).
2. **Defects the tests actually found:** [29 defect reports](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/blob/main/docs/qa/DEFECT_REPORTS.md),
   each with evidence, root cause, fix and regression test.
3. **How release decisions are made:** [Test Strategy](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/blob/main/docs/qa/TEST_STRATEGY.md) ·
   [Risk Register](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/blob/main/docs/qa/RISK_REGISTER.md) ·
   [Traceability (129 requirements)](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/blob/main/docs/qa/TRACEABILITY_MATRIX.md) ·
   [UAT Plan](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/blob/main/docs/qa/UAT_PLAN.md)
4. **From portfolio to live store:** [RbcTcsWorld Shop](https://github.com/rbchy/RbcTcsWorld) and its
   [roadmap](https://github.com/rbchy/RbcTcsWorld/blob/main/docs/store/ROADMAP.md).
5. **One framework, three languages:** QA Brains in [Python](https://github.com/rbchy/QaBrainsAutomationPythonPlawright),
   [TypeScript](https://github.com/rbchy/QaBrainsAutomationTypeScriptPlaywright) and
   [Java](https://github.com/rbchy/QaBrainsAutomationJavaPlaywright) with Playwright.
6. **Domain depth:** [PharmaPack QMS + Serialization](https://github.com/rbchy/RbcTcsWorld_PharmaPackQMS_Serialization)
   (GMP packaging, from my work as a pharmaceutical packaging Line Lead).

---

## ⭐ Flagship projects

| Project | What it is | Evidence |
|---|---|---|
| [RbcTcsWorld E-Commerce Suite](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite) | Amazon-inspired store (Java 21, Spring Boot 4.1, PostgreSQL, React) built to be tested: unit, API, contract, DB, BDD, Selenium, Playwright, Appium, accessibility, performance, security, mutation testing | ![tests](https://img.shields.io/badge/tests-1497-brightgreen) ![coverage](https://img.shields.io/badge/lines-97.3%25-brightgreen) ![mutation](https://img.shields.io/badge/mutation-89.3%25-brightgreen) [![CI](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/RbcTcsWorld_ECommerceSuite/actions/workflows/ci.yml) |
| [RbcTcsWorld Shop](https://github.com/rbchy/RbcTcsWorld) | The same code on its way to a real store: Stripe Elements, tax, shipping, e-mail domain, backups, legal pages, under the same 18 gates | ![stage](https://img.shields.io/badge/stage-pre--launch-f59e0b) [![CI](https://github.com/rbchy/RbcTcsWorld/actions/workflows/ci.yml/badge.svg)](https://github.com/rbchy/RbcTcsWorld/actions/workflows/ci.yml) |

---

## 📂 Projects by area

Live badges show each repository's last update.

### 📱 Mobile (Appium)

| Project | Stack | Result | Updated |
|---|---|---|---|
| [AppiumMobileAutomation](https://github.com/rbchy/AppiumMobileAutomation) | Java · Appium 3 · TestNG · Allure · Sauce Labs My Demo App | 23 / 23, 100 % pass | ![](https://img.shields.io/github/last-commit/rbchy/AppiumMobileAutomation?label=) |
| [AppiumAutomation_ApiDemos](https://github.com/rbchy/AppiumAutomation_ApiDemos) | Java · Appium 3.5 · TestNG · ExtentReports | lifecycle, gestures, input | ![](https://img.shields.io/github/last-commit/rbchy/AppiumAutomation_ApiDemos?label=) |
| [AndroidUIAppiumTest_MyDemoEcommerce](https://github.com/rbchy/AndroidUIAppiumTest_MyDemoEcommerce) | Java 17 · Appium 3 · UiAutomator2 · TestNG | Android e-commerce flows | ![](https://img.shields.io/github/last-commit/rbchy/AndroidUIAppiumTest_MyDemoEcommerce?label=) |
| [WebdriverIO Native Demo App](https://github.com/rbchy/WebdriverIO-Native-DemoApp-MobileTestAutomationJavaAppiumTestNG) | Java · Appium · TestNG · Allure | native app flows | ![](https://img.shields.io/github/last-commit/rbchy/WebdriverIO-Native-DemoApp-MobileTestAutomationJavaAppiumTestNG?label=) |

### 🌐 Web UI automation (BDD)

| Project | Stack | Result | Updated |
|---|---|---|---|
| [QA Brains: TypeScript](https://github.com/rbchy/QaBrainsAutomationTypeScriptPlaywright) | TypeScript · Playwright · Cucumber.js | 14 passed, 0 failed | ![](https://img.shields.io/github/last-commit/rbchy/QaBrainsAutomationTypeScriptPlaywright?label=) |
| [QA Brains: Python](https://github.com/rbchy/QaBrainsAutomationPythonPlawright) | Python · Playwright · Behave · Allure | 12 passed, 0 failed | ![](https://img.shields.io/github/last-commit/rbchy/QaBrainsAutomationPythonPlawright?label=) |
| [QA Brains: Java Playwright](https://github.com/rbchy/QaBrainsAutomationJavaPlaywright) | Java · Playwright · Cucumber JVM · TestNG | stable | ![](https://img.shields.io/github/last-commit/rbchy/QaBrainsAutomationJavaPlaywright?label=) |
| [QA Brains: Java Selenium](https://github.com/rbchy/QaBrainsAutomationJavaSelenium) | Java · Selenium · Cucumber · TestNG | stable | ![](https://img.shields.io/github/last-commit/rbchy/QaBrainsAutomationJavaSelenium?label=) |
| [Amazon: Cypress](https://github.com/rbchy/Amazon-Cypress-JavaScript-Automation) | JavaScript · Cypress 14 · Cucumber | login, shopping, cart | ![](https://img.shields.io/github/last-commit/rbchy/Amazon-Cypress-JavaScript-Automation?label=) |
| [QA Brains: Cypress](https://github.com/rbchy/QaBrainsAutomationCypressJavaScript) | JavaScript · Cypress 13 · Cucumber | e-commerce flows | ![](https://img.shields.io/github/last-commit/rbchy/QaBrainsAutomationCypressJavaScript?label=) |
| [NorthFace AutomationExercise](https://github.com/rbchy/NorthFace_AutomationExercise-BDD-Test-Automation) | UI, E2E, API, accessibility, performance and security in one project | BDD | ![](https://img.shields.io/github/last-commit/rbchy/NorthFace_AutomationExercise-BDD-Test-Automation?label=) |
| [Sauce Demo + MyShopify](https://github.com/rbchy/Sauce-Demo.MyShopify.AutomationTest) | Java · Selenium · TestNG | two shops | ![](https://img.shields.io/github/last-commit/rbchy/Sauce-Demo.MyShopify.AutomationTest?label=) |
| [Multicart Demo](https://github.com/rbchy/Multicart_Demo_Automation) | Java · Selenium · Cucumber | cart and checkout | ![](https://img.shields.io/github/last-commit/rbchy/Multicart_Demo_Automation?label=) |
| [ParaBank (banking)](https://github.com/rbchy/ParaBank-BankingAutomationJavaSelenium) | Java · Selenium · Spring Boot · MySQL | transfers, loans, statements | ![](https://img.shields.io/github/last-commit/rbchy/ParaBank-BankingAutomationJavaSelenium?label=) |
| [OpenEMR (healthcare)](https://github.com/rbchy/OpenEMR_Automation) | Java · Selenium · Cucumber · TestNG | patients, records, roles | ![](https://img.shields.io/github/last-commit/rbchy/OpenEMR_Automation?label=) |
| [OrangeHRM (HR)](https://github.com/rbchy/OrangeHRM_TestAutomation_TestNG_Junit5) | Java · Selenium · TestNG · JUnit 5 | HR and payroll | ![](https://img.shields.io/github/last-commit/rbchy/OrangeHRM_TestAutomation_TestNG_Junit5?label=) |
| [Sauce Labs cloud](https://github.com/rbchy/QaBrainsSauceLabAPI_Automation) | Java · Selenium · Cucumber · Sauce Labs · Jenkins | 20+ parallel browser/OS combinations | ![](https://img.shields.io/github/last-commit/rbchy/QaBrainsSauceLabAPI_Automation?label=) |

### 🔌 API testing

| Project | Stack | Result | Updated |
|---|---|---|---|
| [QA Brains API: REST Assured](https://github.com/rbchy/QaBrainsAPIAutomationRestAssured) | Java · REST Assured · TestNG | auth, data-driven, schema checks | ![](https://img.shields.io/github/last-commit/rbchy/QaBrainsAPIAutomationRestAssured?label=) |
| [QA Brains API: Postman](https://github.com/rbchy/QaBrainsAPIAutomation_Postman) | Postman · Newman | collections, environments, HTML report | ![](https://img.shields.io/github/last-commit/rbchy/QaBrainsAPIAutomation_Postman?label=) |

### 💻 Full-stack applications

| Project | Stack | Domain | Updated |
|---|---|---|---|
| [PharmaPack QMS + Serialization](https://github.com/rbchy/RbcTcsWorld_PharmaPackQMS_Serialization) | Java · desktop builds for Windows, macOS, Linux | GMP pharmaceutical packaging | ![](https://img.shields.io/github/last-commit/rbchy/RbcTcsWorld_PharmaPackQMS_Serialization?label=) |
| [ClinTrial-Connect](https://github.com/rbchy/RbcTcsWorld_ClinTrial-Connect) | Spring Boot · 115+ automated tests | clinical-trial patient matching | ![](https://img.shields.io/github/last-commit/rbchy/RbcTcsWorld_ClinTrial-Connect?label=) |
| [EPMS](https://github.com/rbchy/RbcTcsWorld-EPMS) | Spring Boot REST API + test suite | payroll | ![](https://img.shields.io/github/last-commit/rbchy/RbcTcsWorld-EPMS?label=) |
| [PPES](https://github.com/rbchy/PPES-Pharmaceutical-Packaging-Management) | Java 17 · MySQL 8 · DAO / MVC | packaging inventory | ![](https://img.shields.io/github/last-commit/rbchy/PPES-Pharmaceutical-Packaging-Management?label=) |
| [Payroll Management System](https://github.com/rbchy/PayrollManagementSystem) | Java Swing · MySQL · JDBC | payroll | ![](https://img.shields.io/github/last-commit/rbchy/PayrollManagementSystem?label=) |
| [BhojanAloy POS](https://github.com/rbchy/BhojanAloy-Food-Coffee-Shop-POS-System) | Java Swing · MySQL | food and coffee shop point of sale | ![](https://img.shields.io/github/last-commit/rbchy/BhojanAloy-Food-Coffee-Shop-POS-System?label=) |
| [Inventory Control](https://github.com/rbchy/InventoryControlManagement_JavaMySql) | Java 17 · MySQL 8 · JDBC | real-time inventory | ![](https://img.shields.io/github/last-commit/rbchy/InventoryControlManagement_JavaMySql?label=) |

All 37 repositories: [github.com/rbchy?tab=repositories](https://github.com/rbchy?tab=repositories).

---

## 🛠️ Skills

| Area | Tools |
|---|---|
| Languages | Java · Python · TypeScript · JavaScript · SQL |
| Web UI | Selenium 4 · Playwright · Cypress · Page Object Model |
| Mobile | Appium 3 · UiAutomator2 (Android) · XCUITest (iOS) |
| BDD and runners | Cucumber · Behave · TestNG · JUnit 5 |
| API | REST Assured · Postman / Newman · JSON Schema contracts · OpenAPI diff |
| Quality engineering | JaCoCo coverage · PIT mutation testing · axe-core accessibility · k6 / JMeter performance · OWASP ZAP · OSV-Scanner |
| CI/CD and delivery | GitHub Actions · Jenkins · Docker / Compose · Maven · npm |
| Reporting | Allure · ExtentReports · Cucumber HTML · Playwright HTML |
| Cloud and data | Sauce Labs · AWS basics · PostgreSQL · MySQL · Oracle · Redis |
| Ways of working | Agile Scrum · SDLC / STLC · risk-based testing · traceability · UAT · Jira |

---

## 👨‍💼 Career

| Years | Role |
|---|---|
| 2022 - present | **Sharp Packaging Services LLC** - Line Lead, pharmaceutical blister packaging (primary and secondary): teams of up to 25 operators, batch records and line clearance, serialization, GMP, FDA regulations, OEB handling |
| 2016 - present | **RbcTcsWorld** (self-employed) - QA automation engineer, system designer and developer |
| 1990 - 1995 | **The Computer Systems**, Bangladesh - system consultant, designer and programmer |
| 1979 - 2016 | **Chittagong Port Authority**, Bangladesh - NAVIS SPARCS N4 super user: CTMS configuration, container billing, MIS, team training |

**Education:** Master's in Public Administration, University of Chittagong (1984-1985).

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

**Available for:** full-time · contract · freelance QA Automation Engineer / SDET roles.

---

No portfolio proves a tester is good. This one shows the work instead: frameworks built from scratch, tests that
found real defects, and the evidence behind every number.
