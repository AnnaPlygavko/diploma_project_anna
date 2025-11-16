import pytest

from pageobject_sweetshop.pageobject.login_page import LoginPage
from pageobject_sweetshop.pageobject.success_login_page import SuccessLoginPage


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def success_page(driver):
    return SuccessLoginPage(driver)


@pytest.mark.only
def test_check_all_elements(login_page):
    login_page.open("https://sweetshop.netlify.app/login")
    login_page.check_that_page_opened(description="Login")


@pytest.mark.smoke
def test_positive_login(login_page, success_login_page):
    login_page.open("https://sweetshop.netlify.app/login")

    login_page.login("student@ll.ll", "Password123")
    success_login_page.check_that_page_opened("Your Account")


@pytest.mark.smoke
@pytest.mark.parametrize(
    "user, password, expect",
        ("1", "Password123", "Please enter a valid email address."),
)

def test_negative_username(login_page, user, password, expect):
    login_page.open("https://sweetshop.netlify.app/login")
    login_page.login(user, password)
    login_page.check_that_error_is_visible(expect)


