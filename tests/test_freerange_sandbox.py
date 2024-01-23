import pytest

from playwright.sync_api import Page, expect
from pages.page_freerange_sandbox import FreeRangePage


@pytest.fixture(scope="function", autouse=True)
def before_each(page: Page):
    page.goto("https://thefreerangetester.github.io/sandbox-automation-testing/")

@pytest.fixture
def user(page: Page):
    return FreeRangePage(page)

def test_dynamic_id(user):
    current_id = user.dynamicid_button.get_attribute("id")
    user.click_dynamic_button()

    new_id = user.dynamicid_button.get_attribute("id")
    assert current_id != new_id

def test_hidden_element_is_visible(user):
    user.click_dynamic_button()
    expect(user.hidden_element).to_be_visible()

def test_fill_field_with_text(user):
    text = 'turtle'
    expect(user.addtext_input).to_be_editable()

    user.fill_field_with_text(text)
    expect(user.addtext_input, 'text not found').to_have_value(text)

def test_select_and_deselect_food_option(user):
    pizza_option = 'Pizza'

    # Select
    user.select_food_option(pizza_option)
    expect(user.get_food_option(pizza_option)).to_be_checked()

    # Deselect
    user.deselect_food_option(pizza_option)
    expect(user.get_food_option(pizza_option)).not_to_be_checked()

def test_select_sport_and_submit(user):
    basketball_option = 'Basketball'

    user.select_sport(basketball_option)
    expect(user.get_sport_option()).to_have_value(basketball_option)

    user.submit_sport()
    expect(user.get_sport_option()).to_have_value('Seleccioná un deporte')