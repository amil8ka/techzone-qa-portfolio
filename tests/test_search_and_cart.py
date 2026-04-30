import time

import pytest
from playwright.sync_api import sync_playwright, expect, Page

URL = "https://testgiftshark.work.gd/"
@pytest.mark.parametrize("search, expected", [("Смартфон ProMax X12", "Смартфон ProMax X12"),
                                              ("Ноутбук UltraBook Pro", "Ноутбук UltraBook Pro"),
                                              ('Планшет TabMax 11"', 'Планшет TabMax 11"'),
                                              ("Наушники SoundMax 500", "Наушники SoundMax 500"),
                                              ("Смарт-часы FitPro 3", "Смарт-часы FitPro 3"),
                                              ("Игровая мышь GamePro X", "Игровая мышь GamePro X"),
                                              ("Клавиатура MechType Pro", "Клавиатура MechType Pro"),
                                              ("SSD диск SpeedDrive 1TB", "SSD диск SpeedDrive 1TB"),
                                              ])
def test_search_positive(page: Page, search, expected):
    page.goto(URL)
    page.get_by_placeholder("Найти товар...").fill(search)
    products = page.locator(".product-name").first
    expect(products).to_contain_text(expected)
def test_item_add_to_basket(page: Page):
    page.goto(URL)
    item_locator = page.locator(".product-card").first
    item_locator.get_by_role("button", name="В корзину").click()
    cart_badge = page.locator("#cart-badge")
    expect(cart_badge).to_have_text("1")
def test_xss_search(page:Page):
    xss_detected = False
    def on_dialog(dialog):
        nonlocal xss_detected
        xss_detected = True
        dialog.accept()
    page.on("dialog", on_dialog)
    xss_payload = '<img src=x onerror=alert(1)>'
    page.goto(URL)
    page.get_by_placeholder("Найти товар...").fill(xss_payload)
    page.get_by_role("button", name="Найти").click()
    page.wait_for_timeout(2000)
    assert not xss_detected, f"XSS detected: {xss_payload}"