import pytest

from playwright.sync_api import Page, expect
from pages.page_home_portfolio import HomePortfolioPage


class HomePortfolio:
  @pytest.fixture(scope="function", autouse=True)
  def before_each(page: Page):
    page.goto("https://julianfigueroa.netlify.app/")

  @pytest.mark.parametrize(('sectionName', 'titleExpected', 'titleLocator'),[
    ('Experience', 'Test Engineer', 'experience-title'),
    ('Tech-Stack', 'Tech Stack', 'techstack-title'),
    ('Me', 'Hi there', 'me-title')
  ])
  def test_portfolio_navigation(page: Page,
                            sectionName,
                            titleExpected,
                            titleLocator):
    user = HomePortfolioPage(page)
    user.select_section(sectionName)

    title = page.locator(f'#{titleLocator}')
    expect(title).to_have_text(titleExpected)