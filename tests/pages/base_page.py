from playwright.sync_api import Page
class BasePage:
    def __init__(self, page:Page):
        self.page = page
        self.default_timeout = 5000
    def open(self,url:str):
        self.page.goto(url)
        return self
    def wait_for_element(self, locator, timeout: int = None):
        if timeout is None:
            timeout = self.default_timeout
        locator.wait_for(state="visible", timeout=timeout)
        return locator
    def click_when_ready(self,locator,timeout: int = None):
        if timeout is None:
            timeout = self.default_timeout
        self.wait_for_element(locator,timeout).click()
    def fill_when_ready(self, locator,text: str, timeout: int = None):
        if timeout is None:
            timeout = self.default_timeout
        self.wait_for_element(locator,timeout).fill(text)
