import time
from selenium.webdriver.support import expected_conditions
from locators import HomePageLocators, LoginPageLocators, RegisterPageLocators, ProfilePageLocators


# Тест проверяет успешную регистрацию нового пользователя
def test_successful_registration(driver, wait, new_user_credentials):
   
    # Переходим на страницу регистрации
    wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()

    # Заполняем форму регистрации
    wait.until(expected_conditions.visibility_of_element_located(RegisterPageLocators.NAME_FIELD)).send_keys(
        new_user_credentials["name"]
    )
    driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(new_user_credentials["email"])
    driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(new_user_credentials["password"])
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    # После регистрации автоматически переходим на страницу логина. Ждем появления формы логина и вводим данные

    time.sleep(3)
  
    email_field = wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))
    email_field.send_keys(new_user_credentials["email"])

    password_field = wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.PASSWORD_FIELD))
    password_field.send_keys(new_user_credentials["password"])

    wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()

    # Проверяем успешный логин - появляется кнопка "Оформить заказ" вместо "Войти в аккаунт"
    wait.until(expected_conditions.visibility_of_element_located(HomePageLocators.PLACE_ORDER_BUTTON))




# Тест проверяет ошибку при регистрации с невалидным паролем (менее 6 символов)
def test_registration_with_invalid_password(driver, wait, new_user_credentials):
    
    # Переходим на страницу регистрации
    wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()

    # Заполняем форму с некорректным паролем (5 символов)
    wait.until(expected_conditions.visibility_of_element_located(RegisterPageLocators.NAME_FIELD)).send_keys(
        new_user_credentials["name"]
    )
    driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(new_user_credentials["email"])
    driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys("12345")
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    # Проверяем, что появилась ошибка
    error = wait.until(expected_conditions.visibility_of_element_located(RegisterPageLocators.INVALID_PASSWORD_ERROR))
    assert "Некорректный пароль" in error.text

