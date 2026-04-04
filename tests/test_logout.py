from selenium.webdriver.support import expected_conditions 
from locators import HomePageLocators, LoginPageLocators, ProfilePageLocators
from data import USER_CREDENTIALS

class TestLogout:

# Тест проверяет выход из аккаунта по клику на кнопку "Выход" в личном кабинете
    def test_logout(self, driver, wait, login):
    
        # Переходим в личный кабинет
        wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    
        # Проверяем, что пользователь залогинен
        email_input = wait.until(expected_conditions.visibility_of_element_located(ProfilePageLocators.LOGIN_INPUT))
        assert email_input.get_attribute("value") == USER_CREDENTIALS["email"]

        # Выходим из аккаунта
        wait.until(expected_conditions.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)).click()
    
        # Проверяем, что произошел редирект на страницу логина
        login_title = wait.until(expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE))
        assert login_title.text == "Вход"

