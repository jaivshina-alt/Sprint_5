import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import HomePageLocators, LoginPageLocators
from urls import HOME_PAGE_URL
from helpers import generate_email, generate_password
from data import USER_CREDENTIALS



# Фикстура для создания и закрытия браузера Chrome
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get(HOME_PAGE_URL)
    yield driver
    driver.quit()


# Фикстура для явного ожидания элементов 
@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 5)


# Фикстура с данными нового пользователя для тестов регистрации
@pytest.fixture
def new_user_credentials():
    return {
        "name": "Юля",
        "email": generate_email(),
        "password": generate_password()
    }


# Фикстура для автоматического логина пользователя перед тестом
@pytest.fixture
def login(driver, wait):
    wait.until(expected_conditions.element_to_be_clickable(
        HomePageLocators.LOGIN_TO_ACCOUNT_BUTTON
    )).click()

    wait.until(expected_conditions.visibility_of_element_located(
        LoginPageLocators.EMAIL_FIELD
    )).send_keys(USER_CREDENTIALS["email"])

    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(
        USER_CREDENTIALS["password"]
    )
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    wait.until(expected_conditions.visibility_of_element_located(
        HomePageLocators.PLACE_ORDER_BUTTON
    ))