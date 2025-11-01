import pytest
import os
from playwright.sync_api import Playwright

os.environ["BASE_URL"] = "https://www.automationexercise.com/"

@pytest.fixture
def url():
    return os.getenv("BASE_URL")

@pytest.fixture(scope="session", autouse=True)
def set_test_id_attribute(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-qa")
    yield
