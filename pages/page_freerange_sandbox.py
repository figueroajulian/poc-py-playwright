from playwright.sync_api import Page

class FreeRangePage():

    def __init__(self, page: Page) -> None:
        self.page = page
        self.cookie_consent_button = page.get_by_label('')
        self.dynamicid_button = page.get_by_role("button", name="Hacé click para generar un ID")
        self.hidden_element = page.get_by_text("OMG, aparezco después de 3")
        self.addtext_input = page.get_by_placeholder("Ingresá texto")
        self.bool_radiobutton = page.get_by_label('Yes')
        self.sport_options = page.get_by_label("Dropdown")
        self.submit_sport_button = page.get_by_role("button", name="Enviar")

    def get_food_option(self, name: str):
        return self.page.get_by_label(name)

    def get_sport_option(self):
        return self.sport_options

    def click_dynamic_button(self) -> None:
        self.dynamicid_button.click()

    def fill_field_with_text(self, text: str) -> None:
        self.addtext_input.fill(text)

    def select_food_option(self, name: str) -> None:
        self.get_food_option(name).check()

    def deselect_food_option(self, name: str) -> None:
        self.get_food_option(name).uncheck()

    def select_sport(self, opt: str) -> None:
        self.get_sport_option().select_option(opt)

    def submit_sport(self) -> None:
        self.submit_sport_button.click()