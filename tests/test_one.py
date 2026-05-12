import pytest
import re
from playwright.sync_api import Page, expect, Route, APIRequestContext
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.signup_page import SignupPage
from pytest_csv_params.decorator import csv_params
import requests


def test_one(page: Page):

    page.goto("https://www.automationexercise.com/")

    page.locator("css=a[href='/login']").click()

    # page.wait_for_load_state("networkidle", timeout=300000)

    page.get_by_test_id("login-email").fill("email@email.com")

    page.get_by_test_id("login-password").fill("password")


    page.get_by_test_id("login-button").click()

    expect(page.locator("css=form[action='/login'] p")).to_contain_text("Your email or password is incorrect!")



    