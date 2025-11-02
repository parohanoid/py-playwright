import pytest
import re
from playwright.sync_api import Page, expect, Route, APIRequestContext
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.signup_page import SignupPage
from pytest_csv_params.decorator import csv_params
import requests

@pytest.mark.parametrize("users", ["John", "Emma", "Liam"])
def test_like_and_notification(page: Page, social_media_url, users):
    page.goto(social_media_url)

    text = page.locator(f"xpath=//h6[contains(text(), '{users}')]/../..//button/following-sibling::p").inner_text()
    initial_likes = int(text.split(" likes")[0])

    initial_notifications = int(page.locator("xpath=//*[contains(@class,'MuiBadge-anchorOriginTopRightRectangular')]").inner_text() or 0)

    # Simulate user liking a post
    page.locator(f"xpath=//h6[contains(text(), '{users}')]/../..//button").click()

    expect(page.locator(f"xpath=//h6[contains(text(), '{users}')]/../..//button/following-sibling::p")).to_have_text(f"{str(initial_likes + 1)} likes")

    # Simulate user receiving a notification
    expect(page.locator("xpath=//*[contains(@class,'MuiBadge-anchorOriginTopRightRectangular')]")).to_have_text(str(initial_notifications + 1))

    # Click on the notification and verify the message
    page.locator("xpath=//*[contains(@class,'MuiBadge-anchorOriginTopRightRectangular')]/ancestor::button").click()

    expect(page.locator("xpath=//h6[contains(text(), 'Notifications')]/following-sibling::*//p").filter(has_text=f"You liked {users}'s post")).to_be_visible()
