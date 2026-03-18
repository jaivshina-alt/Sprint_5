import random
import string
import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import HomePageLocators, LoginPageLocators


HOME_PAGE_URL = "https://stellarburgers.education-services.ru/"



# Генерация уникального email в формате julia_ivshina_42_XXX@yandex.ru
def generate_email():
    random_digits = random.randint(100, 999)
    return f"julia_ivshina_42_{random_digits}@yandex.ru"


# Генерация пароля 
def generate_password(length=10):
    if length < 6:
        length = 6
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


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


# Фикстура с данными существующего пользователя для тестов логина
@pytest.fixture
def user_credentials():
    return {
        "email": "julia_ivshina_42_555@yandex.ru",
        "password": "1234567890"
    }


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
def login(driver, wait, user_credentials):
    wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.LOGIN_TO_ACCOUNT_BUTTON)).click()
    wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD)).send_keys(
        user_credentials["email"]
    )
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user_credentials["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    # Ждем, пока кнопка "Оформить заказ" станет видимой (признак успешного логина)
    wait.until(expected_conditions.visibility_of_element_located(HomePageLocators.PLACE_ORDER_BUTTON))