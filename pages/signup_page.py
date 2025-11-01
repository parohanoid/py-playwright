from pages.home_page import HomePage
from playwright.sync_api import Page

class SignupPage(HomePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.signup_form_title = page.locator("xpath=//*[text()='Enter Account Information']")
        self.mr_radio = page.get_by_role("radio", name="Mr.")
        self.name = page.get_by_test_id('name')
        self.email = page.get_by_test_id('email')
        self.password = page.get_by_test_id('password')
        self.days = page.get_by_test_id('days')
        self.months = page.get_by_test_id('months')
        self.years = page.get_by_test_id('years')
        self.newsletter = page.get_by_role("checkbox", name="Sign up for our newsletter!")
        self.optin = page.get_by_role("checkbox", name="Receive special offers from our partners!")
        self.fname = page.get_by_test_id('first_name')
        self.lname = page.get_by_test_id('last_name')
        self.company = page.get_by_test_id('company')
        self.address = page.get_by_test_id('address')
        self.address2 = page.get_by_test_id('address2')
        self.country = page.get_by_test_id('country')
        self.state = page.get_by_test_id('state')
        self.city = page.get_by_test_id('city')
        self.zipcode = page.get_by_test_id('zipcode')
        self.mobile_number = page.get_by_test_id('mobile_number')
        self.create_account_button = page.get_by_test_id('create-account')

        self.account_created_title = page.get_by_test_id('account-created')
        self.continue_button = page.get_by_test_id('continue-button')