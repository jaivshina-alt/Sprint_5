import pytest
from selenium.webdriver.support import expected_conditions 
from locators import HomePageLocators




class TestConstructorTabs:

    # Тест проверяет переходы по вкладкам «Булки», «Соусы», «Начинки» в конструкторе
    @pytest.mark.parametrize(
        "starter_tab, target_tab",
        [
            (HomePageLocators.SAUCES_TAB, HomePageLocators.BUNS_TAB),
            (HomePageLocators.FILLINGS_TAB, HomePageLocators.SAUCES_TAB),
            (HomePageLocators.SAUCES_TAB, HomePageLocators.FILLINGS_TAB),
        ]
    )
    def test_navigate_between_tabs(self, driver, wait, starter_tab, target_tab):
        # Переход на стартовую вкладку
        wait.until(expected_conditions.element_to_be_clickable(starter_tab)).click()
        wait.until(expected_conditions.text_to_be_present_in_element_attribute(
            starter_tab, "class", "current"
        ))
        # Переход на выбранную вкладку
        wait.until(expected_conditions.element_to_be_clickable(target_tab)).click()
        wait.until(expected_conditions.text_to_be_present_in_element_attribute(
            target_tab, "class", "current"
        ))
        # Проверка выбранной вкладки
        tab_element = driver.find_element(*target_tab)
        assert "current" in tab_element.get_attribute("class")