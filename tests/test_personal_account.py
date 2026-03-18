from selenium.webdriver.support import expected_conditions 
from locators import HomePageLocators, LoginPageLocators, ProfilePageLocators


# Тест проверяет переход в личный кабинет по клику на кнопку "Личный Кабинет" в хэдере
def test_navigate_to_personal_account(driver, wait, login):

    # Нажимаем кнопку "Личный Кабинет"
    wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.PERSONAL_ACCOUNT_BUTTON)).click()

    # Проверяем, что перешли на страницу профиля и URL заканчивается на /account
    wait.until(expected_conditions.url_contains("/account"))
    assert driver.current_url.endswith("/account")




