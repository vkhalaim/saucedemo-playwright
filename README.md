# saucedemo-playwright

A learning project for UI test automation using **Playwright** and **pytest**, built against [saucedemo.com](https://www.saucedemo.com/).

The project focuses on the architecture of a test framework rather than a loose collection of tests: Page Object Model, separation of config/secrets, parametrized negative scenarios, visual regression testing, and CI.

## Stack

- **Python 3.12**
- **Playwright** (sync API) — browser automation
- **pytest** + `pytest-playwright` — test runner
- **pytest-playwright-visual-snapshot** — visual regression
- **python-dotenv** — environment variable handling
- **GitHub Actions** — CI

## Project structure

```
saucedemo-playwright/
├── pages/                      # Page Object Model
│   ├── login_page.py           # LoginPage: login, reading error messages
│   └── inventory_page.py       # InventoryPage: adding items to the cart
├── tests/
│   ├── test_login.py           # positive and negative login scenarios
│   ├── test_cart.py            # adding items, checkout, total verification
│   └── test_visual.py          # visual regression on the inventory page
├── __snapshots__/              # baseline screenshots
├── conftest.py                 # shared fixtures (logged_in_page)
├── config.py                   # single source for reading .env
├── .env                        # secrets (gitignored, never committed)
├── requirements.txt
└── .github/workflows/tests.yml # CI
```

## Architectural decisions

- **Page Object Model** — page interaction logic is encapsulated in classes (`pages/`), so tests read as a description of a scenario rather than a sequence of clicks on locators.
- **Locators** — priority given to `data-test` attributes and semantic roles (`get_by_role`) over text/CSS selectors where possible, for resilience against markup changes.
- **Secrets vs config vs test data** — three distinct responsibilities:
  - secrets (logins/passwords) live in `.env`, read once via `config.py`;
  - test scenarios/data live next to the tests that use them;
  - page behavior lives in the Page Object.
- **Numeric comparisons** — done via `pytest.approx` rather than `==`, to avoid flaky tests caused by float precision.
- **Parametrization** — negative login scenarios are combined into a single test via `@pytest.mark.parametrize`, with human-readable `ids`.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install --with-deps
```

Create a `.env` file in the project root:
```
SAUCE_USERNAME=standard_user
SAUCE_PASSWORD=secret_sauce
SAUCE_USERNAME_LOCKED_OUT=locked_out_user
```

## Running tests

```bash
pytest
```

Update baseline screenshots (after intentional UI changes):
```bash
pytest --update-snapshots
```

## CI

Tests run automatically in GitHub Actions on every push and pull request to `main`. Secrets are passed via GitHub Secrets (Settings → Secrets and variables → Actions), not stored in the repository.

## Test coverage

- Successful login, adding items to the cart, checkout with total verification.
- Negative login scenarios: locked-out user, empty username/password fields.
- Visual regression of the inventory page.