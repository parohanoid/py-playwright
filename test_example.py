import pytest
import re
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("before test runs")
    page.goto('https://www.playwright.dev')
    yield
    print('after the test')


def test_has_title(page: Page):
    # page.goto("https://www.playwright.dev")
    expect(page).to_have_title(re.compile("Fast and reliable"))

def test_get_started_link(page: Page):
    # page.goto("https://www.playwright.dev")
    page.get_by_role("link", name="Get started").click()

    expect(page.get_by_role("heading", name="Installation")).to_be_visible

