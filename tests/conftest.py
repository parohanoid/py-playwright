import pytest
import os
from playwright.sync_api import Playwright, APIRequestContext
from typing import Generator

os.environ["BASE_URL"] = "https://www.automationexercise.com/"

@pytest.fixture
def url():
    return os.getenv("BASE_URL")

@pytest.fixture
def social_media_url():
    return "https://www.cnarios.com/challenges/social-media-feed#challenge"

@pytest.fixture(scope="session", autouse=True)
def set_test_id_attribute(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-qa")
    yield

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    headers = {
        # We set this header per GitHub guidelines.
        "Accept": "application/vnd.github.v3+json",
        # Add authorization token to all requests.
    }
    request_context = playwright.request.new_context(
        base_url="https://api.github.com", extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()