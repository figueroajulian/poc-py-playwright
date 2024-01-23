from playwright.sync_api import Page

class CheckHomePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.cookies = page.get_by_label("Accept all").click()
        self.selector = page.get_by_role("link")
        page.get_by_role("link", name="Product ").click()
        page.get_by_role("link", name="Support").click()