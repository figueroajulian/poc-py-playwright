from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click_element(self, selector):
        self.page.locator(selector).click()

    def fill_input(self, selector, text):
        self.page.locator(selector).fill(text)