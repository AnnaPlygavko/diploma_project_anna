from selenium.webdriver.common.by import By

from pageobject_sweetshop.pageobject.base_page import BasePage


class SuccessLoginPage(BasePage):
    TEXT = (By.CLASS_NAME, "display-3") # Your Account
    YOUR_BASKET = (By.CLASS_NAME, "col-md-4 order-md-2 mb-4") # Корзина

    def __init__(self, driver):
        super().__init__(driver)

    def check_that_page_opened(self, text):
        self.should_be_visible(self.TEXT)
        self.should_be_visible(self.YOUR_BASKET )

        self.should_be_has_text(self.TEXT, text)