from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.profile = page.locator("xpath=//*[contains(@class,'shop-menu')]//*[contains(text(),'Logged in as')]")
        self.delete_account = page.locator("xpath=//*[contains(text(),'Delete Account')]")
        self.delete_account_confirmation = page.get_by_test_id('account-deleted')