import pytest

from playwright.sync_api import Page, Playwright, APIRequestContext

@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> APIRequestContext:
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()

def test_get_hydrogen_status(api_request_context: APIRequestContext):
    response = api_request_context.get('https://rickandmortyapi.com/api/character/161')
    assert response.status == 200, 'Invalid status code.'

def test_check_hydrogen_data(api_request_context: APIRequestContext):
    response = api_request_context.get('https://rickandmortyapi.com/api/character/161')
    response_data = response.json()

    assert response.ok
    assert response.json() != {}
    assert "name" in response_data

def test_wait_for_service(page:Page):
    page.goto('https://playwright.dev/python/docs/intro')

    with page.expect_response('https://playwright-analytics.azurewebsites.net/api/impression?hash=&path=%2Fdocs%2Fintro&language=python') as response_info:
        page.get_by_title('Introduction').is_visible()

    response = response_info.value
    assert response.status == 200, f"La respuesta tiene un código de estado {response.status}, se esperaba 200"

    page.get_by_text('Network').click()

    with page.expect_response('https://playwright-analytics.azurewebsites.net/api/impression?hash=&path=%2Fdocs%2Fnetwork&language=python') as response_info:
        page.get_by_title('Network').first.is_visible()

    response = response_info.value
    assert response.status == 200, f"La respuesta tiene un código de estado {response.status}, se esperaba 200"
