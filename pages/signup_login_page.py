from pages.base_page import BasePage

class SignupLoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.signup_title = page.locator("xpath=//h2[text()='New User Signup!']")
        self.name_field = page.get_by_test_id('signup-name')
        self.email_field = page.get_by_test_id('signup-email')
        self.signup_button = page.get_by_test_id('signup-button')