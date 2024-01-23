from playwright.sync_api import Page

class HomePortfolioPage:

    def __init__(self, page: Page) -> None:
        self.page = page

    def section_link(self, section: str):
        return self.page.get_by_role("link", name=section)

    def select_section(self, section: str) -> None:
        section_link = self.section_link(section)
        section_link.click()

