import pytest

from playwright.sync_api import Page, expect
from pages.page_home_portfolio import HomePortfolioPage


@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page):
    page.goto("https://checkmk.com/")

def test_check_home_selectors(page: Page):
    pass
