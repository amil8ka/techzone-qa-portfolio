from playwright.sync_api import expect, Page
from pages.login_page import LoginPage

URL = "https://testgiftshark.work.gd/login.html"
password = "lolkekcheburek23!"


def test_login_positive(page: Page):
    login_page = LoginPage(page)
    login_page.open(URL)
    login_page.login("user@test.com", "user123")
    login_page.check_success_login()


def test_login_with_bad_password(page: Page):
    login_page = LoginPage(page)
    login_page.open(URL)
    login_page.login("user@test.com", "wrongpassword")
    login_page.check_error_login()


def test_register(page: Page):
    login_page = LoginPage(page)
    login_page.open(URL)
    login_page.open_registration_form()
    login_page.register_test_random_email("Иван Петров", password)
    login_page.check_success_register()


def test_register_with_empty_email(page: Page):
    login_page = LoginPage(page)
    login_page.open(URL)
    login_page.open_registration_form()
    login_page.register("Иван Петров", "", password)
    login_page.check_error_register()
