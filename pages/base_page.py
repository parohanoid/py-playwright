from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

        self.logo = page.get_by_alt_text(text="Website for automation practice")
        self.products = page.locator("xpath=//*[contains(@class,'shop-menu')]//*[contains(text(),'Products')]")
        self.carts = page.locator("xpath=//*[contains(@class,'shop-menu')]//*[contains(text(),'Carts')]")
        self.signup_login = page.locator("xpath=//*[contains(@class,'shop-menu')]//*[contains(text(),'Signup / Login')]")
        self.test_cases = page.locator("xpath=//*[contains(@class,'shop-menu')]//*[contains(text(),'Test Cases')]")