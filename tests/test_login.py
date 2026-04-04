from selenium.webdriver.support import expected_conditions 
from locators import HomePageLocators, LoginPageLocators, ProfilePageLocators, RegisterPageLocators, ForgotPasswordPageLocators
from data import USER_CREDENTIALS


class TestLogin:
    
    # Тест проверяет логин по кнопке "Войти в аккаунт" на главной странице
    def test_login_via_login_account_button(self, driver, wait):

        # Нажимаем кнопку "Войти в аккаунт"
        wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.LOGIN_TO_ACCOUNT_BUTTON)).click()

        # Вводим email и пароль
        wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD)).send_keys(USER_CREDENTIALS["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(USER_CREDENTIALS["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Ждем, пока кнопка "Оформить заказ" станет видимой (признак успешного логина)
        wait.until(expected_conditions.visibility_of_element_located(HomePageLocators.PLACE_ORDER_BUTTON))

        # Переходим в личный кабинет и проверяем, что в поле Email указан нужный email
        wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        email_input = wait.until(expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGIN_INPUT))
        assert email_input.get_attribute("value") == USER_CREDENTIALS["email"]




 # Тест проверяет вход через кнопку "Личный Кабинет" в хедере
    def test_login_via_personal_account_button(self, driver, wait):

        # Нажимаем кнопку "Личный Кабинет"
        wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.PERSONAL_ACCOUNT_BUTTON)).click()

        # Вводим email и пароль
        wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD)).send_keys(USER_CREDENTIALS["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(USER_CREDENTIALS["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Ждем, пока кнопка "Оформить заказ" станет видимой (признак успешного логина)
        wait.until(expected_conditions.visibility_of_element_located(HomePageLocators.PLACE_ORDER_BUTTON))

        # Переходим в личный кабинет и проверяем, что в поле Email указан нужный email
        wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        email_input = wait.until(expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGIN_INPUT))
        assert email_input.get_attribute("value") == USER_CREDENTIALS["email"]




 # Тест проверяет вход через кнопку "Войти" в форме регистрации
    def test_login_from_register_page(self, driver, wait):

        # Переходим на страницу регистрации
        wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()

        # Нажимаем ссылку "Войти"
        wait.until(expected_conditions.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK)).click()

        # Вводим email и пароль
        wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD)).send_keys(USER_CREDENTIALS["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(USER_CREDENTIALS["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Ждем, пока кнопка "Оформить заказ" станет видимой (признак успешного логина)
        wait.until(expected_conditions.visibility_of_element_located(HomePageLocators.PLACE_ORDER_BUTTON))

        # Переходим в личный кабинет и проверяем, что в поле Email указан нужный email
        wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        email_input = wait.until(expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGIN_INPUT))
        assert email_input.get_attribute("value") == USER_CREDENTIALS["email"]



# Тест проверяет вход через кнопку "Войти" в форме восстановления пароля
    def test_login_from_forgot_password_page(self, driver, wait):

        # Переходим на страницу восстановления пароля
        wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(expected_conditions.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK)).click()

        # Нажимаем ссылку "Войти"
        wait.until(expected_conditions.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)).click()

        # Вводим email и пароль
        wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD)).send_keys(USER_CREDENTIALS["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(USER_CREDENTIALS["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Ждем, пока кнопка "Оформить заказ" станет видимой (признак успешного логина)
        wait.until(expected_conditions.visibility_of_element_located(HomePageLocators.PLACE_ORDER_BUTTON))

        # Переходим в личный кабинет и проверяем, что в поле Email указан нужный email
        wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        email_input = wait.until(expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGIN_INPUT))
        assert email_input.get_attribute("value") == USER_CREDENTIALS["email"]

