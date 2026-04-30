import time
from datetime import datetime
from playwright.sync_api import Page, expect
from .base_page import BasePage
MAIN_URL = "https://testgiftshark.work.gd/index.html"
class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        login_form = page.locator("#tab-login") #Форма логина
        self.email_login_input = login_form.get_by_role("textbox", name="Email")
        self.password_login_input = login_form.get_by_role("textbox", name="Пароль")
        self.button_login_input = login_form.get_by_role("button", name="Войти")

        self.open_registration_form_locator = page.get_by_role("button", name="Регистрация") #Открыть форму регистрации

        register_form = page.locator("#tab-register") #Форма регистрации
        self.name_registration_input = register_form.get_by_role("textbox", name="Имя и фамилия")
        self.email_registration_input = register_form.get_by_role("textbox", name="Email")
        self.password_registration_input = register_form.get_by_role("textbox", name="Пароль")
        self.button_registration_input = register_form.get_by_role("button", name="Создать аккаунт")

        self.alert = page.locator("#login-alert") #алерт об успешном входе
        self.reg_alert = page.locator("#reg-alert")
    def login(self, email, password): #Логин
        self.fill_when_ready(self.email_login_input, email)
        self.fill_when_ready(self.password_login_input, password)
        self.click_when_ready(self.button_login_input)
    def open_registration_form(self): #Открыть форму регистрации
        self.click_when_ready(self.open_registration_form_locator)
    def register_test_random_email(self,name, password): #Регистрация с рандомным email
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        email = f"test_qa{timestamp}@gmail.com"
        self.fill_when_ready(self.name_registration_input, name)
        self.fill_when_ready(self.email_registration_input, email)
        self.fill_when_ready(self.password_registration_input, password)
        self.click_when_ready(self.button_registration_input)
    def register(self,name,email, password): #Регистрация
        self.fill_when_ready(self.name_registration_input, name)
        self.fill_when_ready(self.email_registration_input, email)
        self.fill_when_ready(self.password_registration_input, password)
        self.click_when_ready(self.button_registration_input)
    def check_success_login(self):
        expect(self.alert).to_contain_text("выполнен")
        expect(self.page).to_have_url(MAIN_URL)
    def check_error_login(self):
        expect(self.alert).not_to_contain_text("выполнен")
        expect(self.page).not_to_have_url(MAIN_URL)
    def check_success_register(self):
        expect(self.reg_alert).to_contain_text("создан!")
        expect(self.page).to_have_url(MAIN_URL)
    def check_error_register(self):
        expect(self.reg_alert).to_contain_text("все")
        expect(self.page).not_to_have_url(MAIN_URL)