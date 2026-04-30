import re, time

import pytest
from playwright.sync_api import Page

@pytest.fixture
def login_page(page: Page):
    URL = "https://testgiftshark.work.gd/"
    page.goto(URL)
    page.get_by_role("button", name="Войти").click()
    login_form = page.locator("#tab-login")
    login_form.get_by_label("Email").fill("user@test.com")
    login_form.get_by_label("Пароль").fill("user123")
    login_form.get_by_role("button", name="Войти").click()
    alert = page.locator("#login-alert")
    alert.wait_for(state="visible", timeout=5000)
    return page
timestamp = time.strftime("%Y%m%d%H%M%S")
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            safe_name = re.sub(r'[<>:"/\\|?*]', '_', item.name)
            safe_name = safe_name[:50]
            filename = f"{safe_name}_{timestamp}.png"
            page.screenshot(path=filename, full_page=True)
