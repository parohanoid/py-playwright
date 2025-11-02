import pytest
import re
from playwright.sync_api import Page, expect, Route, APIRequestContext
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.signup_page import SignupPage
from pytest_csv_params.decorator import csv_params
import requests

# reporting done
# read test data done

# mock APIs for UI tests

# Key challenging automation scenarios
# dataclass, pydantic
# locator strategies
# 5 suggestions to make test repo reliable, maintainable, scalable, testable and early bug detection
# BDD / Cucumber
# README
# Authentication strategies / Automation and API
# Error handling
# validate response against JSON schema / pytest, requests
# REST API methods
# DB check
# Various Response codes
# Check idempotency

# performance testing / locust, WLM, SLAs, P95 and P99, reporting as per SLAs

# self - review presentation

# Argo CD for locust load generation
# Spin up test environments using Terraform / Ansible for all the test suite
# Gating logic for test environments / application code deployments
# IAM roles and policies and secrets management for test environments

# Observability / monitoring, gathering new relic, expose prometheus metrics with grafana, set alerts:
# P95 and P99, error rates, SLA breaches, throughput, resource utilization
# resilience testing / chaos engineering (partial failures, degraded latency

# Testability suggestions (API-first features, instrumentation).
# Bug prevention: static analysis, contract checks, mutation tests (awareness).
# Test coverage vs risk coverage: choose the right levels.
# Release gating and risk-based test selection.)

# negotiating and influencing product and dev for better quality and testability
# documentation practices for bugs, test cases and test strategies
# Risk mitigation strategies for production issues, bugs, bug prioritization strategies


@csv_params(data_file="data/test_data.csv", data_casts = {
    "name": str,
    "email": str,
    "password": str
})
def test_register_user(page: Page, url, name, email, password):
    page.goto(url)

    home_page = HomePage(page)

    expect(home_page.logo).to_be_visible()

    home_page.signup_login.click()

    signup_login_page = SignupLoginPage(page)
    expect(signup_login_page.signup_title).to_be_visible()
    signup_login_page.name_field.fill(name)
    signup_login_page.email_field.fill(email)
    signup_login_page.signup_button.click()

    signup_page = SignupPage(page)
    expect(signup_page.signup_form_title).to_be_visible()
    signup_page.mr_radio.check()
    signup_page.name.fill(name)
    signup_page.password.fill(password)
    signup_page.days.select_option(value="1")
    signup_page.months.select_option(value="1")
    signup_page.years.select_option(value="2000")
    signup_page.newsletter.check()
    signup_page.optin.check()

    signup_page.fname.fill(name[:2])
    signup_page.lname.fill(name[2:])
    signup_page.company.fill("apple")
    signup_page.address.fill("123 street")
    signup_page.address2.fill("456 avenue")
    signup_page.country.select_option(value="Canada")
    signup_page.state.fill("Ontario")
    signup_page.city.fill("Toronto")
    signup_page.zipcode.fill("A1B2C3")
    signup_page.mobile_number.fill("1234567890")

    signup_page.create_account_button.click()
    expect(signup_page.account_created_title).to_be_visible()
    signup_page.continue_button.click()

    home_page = HomePage(page)
    expect(home_page.profile).to_be_visible()
    expect(
        home_page.profile.locator(f"xpath=//*[contains(text(),'{name}')]")
    ).to_be_visible()

    home_page.delete_account.click()
    expect(home_page.delete_account_confirmation).to_be_visible()

# Mock an API
def test_mock_the_fruit_api(page: Page):
    def handle(route: Route):
        json = [{"name": "Strawberry", "id": 21}]
        # fulfill the route with the mock data
        route.fulfill(json=json)

    # Intercept the route to the fruit API
    page.route("*/**/api/v1/fruits", handle)

    # Go to the page
    page.goto("https://demo.playwright.dev/api-mocking")

    # Assert that the Strawberry fruit is visible
    expect(page.get_by_text("Strawberry")).to_be_visible()



# Log or spy on network API responses
def test_log_api_response(page: Page):

    with page.expect_response(lambda response: "/openapi.json" in response.url) as resp_info:
        page.goto("https://petstore3.swagger.io/")
    
        response = resp_info.value  # this is the Response object

        try:
            data = response.json()
            print(data)
        except Exception as e:
            print(f"Could not parse JSON: {e}")