from selenium.webdriver.common.by import By
from pageobject_sweetshop.pageobject.base_page import BasePage

class LoginPage(BasePage):
    LOGO = (By.CLASS_NAME,"d-inline-block align-top") #лого в виду конфеты в меню слева
    MENU_HOME = (By.CLASS_NAME, "navbar-brand") #домашняя стр
    MENU_SWEET = (By.LINK_TEXT, "Sweet")
    MENU_ABOUT = (By.LINK_TEXT, "About")
    MENU_BASKET = (By.LINK_TEXT, "Basket")
    PAGE_DESCRIPTION= (By.CLASS_NAME, "my-4")
    INPUT_USER_NAME = (By.ID, "exampleInputEmail")
    INPUT_PASSWORD = (By.ID, "exampleInputPassword")
    SUBMIT = (By.ID, "btn_9scxusxcg")
    ERROR = By.ID, "error"



    def __init__(self, driver):
        super().__init__(driver)

    def check_that_page_opened(self, description):
        self.should_be_visible(self.LOGO)
        self.should_be_visible(self.MENU_HOME)
        self.should_be_visible(self.MENU_SWEET)
        self.should_be_visible(self.MENU_ABOUT)
        self.should_be_visible(self.MENU_BASKET)
        self.should_be_visible(self.PAGE_DESCRIPTION)
        self.should_be_visible(self.INPUT_USER_NAME)
        self.should_be_visible(self.INPUT_PASSWORD)
        self.should_be_visible(self.SUBMIT)



        self.should_be_has_text(self.PAGE_DESCRIPTION, description)

        self.should_be_not_visible(self.ERROR)

    def login(self, username, password):
        self.fill(self.INPUT_USER_NAME, text=username)
        self.fill(self.INPUT_PASSWORD, text=password)
        self.click(self.SUBMIT)

    def check_that_error_is_visible(self, text):
        self.should_be_visible(self.ERROR)
        self.should_be_has_text(self.ERROR, text)