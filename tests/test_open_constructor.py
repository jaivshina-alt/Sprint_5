from selenium.webdriver.support import expected_conditions 
from locators import HomePageLocators, LoginPageLocators, ProfilePageLocators


class TestOpenConstructor:

    # Тест проверяет переход из личного кабинета в конструктор по клику на кнопку "Конструктор" в хэдере
    def test_navigate_to_constructor_via_constructor_button(self, driver, wait, login):
   
        # Переходим в личный кабинет
        wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    
        # Кликаем на кнопку "Конструктор"
        wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.CONSTRUCTOR_BUTTON)).click()

        # Проверяем, что вернулись на страницу конструктора
        constructor_title = wait.until(expected_conditions.visibility_of_element_located(HomePageLocators.CONSTRUCTOR_TITLE))
        assert constructor_title.text == "Соберите бургер"




    # Тест проверяет переход из личного кабинета в конструктор по клику на лого
    def test_navigate_to_constructor_via_logo(self, driver, wait, login):
   
        # Переходим в личный кабинет
        wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    
        # Кликаем на логотип
        wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.LOGO_BUTTON)).click()
    
        # Проверяем, что вернулись на страницу конструктора
        constructor_title = wait.until(expected_conditions.visibility_of_element_located(HomePageLocators.CONSTRUCTOR_TITLE))
        assert constructor_title.text == "Соберите бургер"

