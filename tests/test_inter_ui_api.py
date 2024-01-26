import pytest
from playwright.sync_api import Page, Playwright, APIRequestContext, expect

@pytest.fixture(scope='session', autouse=True)
def beforeEach(page:Page):
    page.goto('https://playwright.dev/python/docs/input')

@pytest.fixture(scope='session')
def api_context(p: Playwright):
    context = p.request.new_context()
    yield context
    context.dispose()

def test_action_ui(page: Page):
    title = page.get_by_title('Action')
    title.is_visible()

    expect(title).to_have_text('Action')

def test_api(api: APIRequestContext):
    response = api.get('https://playwright.dev/python/docs/input')
    assert response.status == 200

def test_interception_api(page: Page):
    with page.expect_response('https://playwright.dev/python/docs/input') as r:
        page.get_by_title('Actions').is_visible()

    response = r.value
    assert response.status == 200


