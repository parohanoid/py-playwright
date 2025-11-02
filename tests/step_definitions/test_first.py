# from pytest_bdd import scenarios, given, when, then
# from playwright.sync_api import Page

# scenarios('../features/first.feature')

# LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"
# USERNAME = "student"
# PASSWORD = "Password123"

# @given("the user is on the login page")
# def open_login_page(page: Page):
#     page.goto(LOGIN_URL)

# @when("the user enters valid credentials")
# def login_user(page: Page):
#     page.fill("#username", USERNAME)
#     page.fill("#password", PASSWORD)
#     page.click("#submit")

# @then("the user should be logged in")
# def check_login(page: Page):
#     header = page.locator("h1")
#     assert "Logged In Successfully" in header.text_content()