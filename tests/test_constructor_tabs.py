from selenium.webdriver.support import expected_conditions 
from locators import HomePageLocators


# Тест проверяет переход к вкладке  "Булки" в конструкторе
def test_navigate_to_buns_section(driver, wait):

    # Сначала переходим к вкладке "Соусы"
    wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.SAUCES_TAB)).click()
    wait.until(expected_conditions.text_to_be_present_in_element_attribute(
        HomePageLocators.SAUCES_TAB, "class", "current"
    ))

    # Затем переходим к вкладке "Булки"
    wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.BUNS_TAB)).click()
    wait.until(expected_conditions.text_to_be_present_in_element_attribute(
        HomePageLocators.BUNS_TAB, "class", "current"
    ))



# Тест проверяет переход к вкладке "Соусы" в конструкторе
def test_navigate_to_sauces_section(driver, wait):
    
    # Сначала переходим к вкладке "Начинки"
    wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.FILLINGS_TAB)).click()
    wait.until(expected_conditions.text_to_be_present_in_element_attribute(
        HomePageLocators.FILLINGS_TAB, "class", "current"
    ))

    # Затем переходим к вкладке "Соусы"
    wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.SAUCES_TAB)).click()
    wait.until(expected_conditions.text_to_be_present_in_element_attribute(
        HomePageLocators.SAUCES_TAB, "class", "current"
    ))


# Тест проверяет переход к вкладке "Начинки" в конструкторе
def test_navigate_to_fillings_section(driver, wait):
    
    # Сначала переходим к вкладке "Соусы" 
    wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.SAUCES_TAB)).click()
    wait.until(expected_conditions.text_to_be_present_in_element_attribute(
        HomePageLocators.SAUCES_TAB, "class", "current"
    ))

    # Затем переходим к вкладке "Начинки"
    wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.FILLINGS_TAB)).click()
    wait.until(expected_conditions.text_to_be_present_in_element_attribute(
        HomePageLocators.FILLINGS_TAB, "class", "current"
    ))

