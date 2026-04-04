
from selenium.webdriver.common.by import By


class HomePageLocators:
    # Кнопка "Конструктор" в хэдере
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")

    # Логотип Stellar Burgers
    LOGO_BUTTON = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]")

    # Кнопка "Личный кабинет" в хэдере
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")

    # Заголовок конструктора "Соберите бургер"
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")

    # Вкладка "Булки"
    BUNS_TAB = (By.XPATH, ".//span[text()='Булки']/parent::*")

    # Вкладка "Соусы"
    SAUCES_TAB = (By.XPATH, ".//span[text()='Соусы']/parent::*")

    # Вкладка "Начинки"
    FILLINGS_TAB = (By.XPATH, ".//span[text()='Начинки']/parent::*")

    # Кнопка "Войти в аккаунт"
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")

     # Кнопка "Оформить заказ"
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")



class LoginPageLocators:
    # Заголовок логин формы "Вход"
    LOGIN_TITLE = (By.XPATH, ".//h2[text()='Вход']")

    # Поле Email
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")

    # Поле Пароль
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")

    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")

    # Ссылка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")



class RegisterPageLocators:
    # Поле Имя
    NAME_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")

    # Поле Email
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")

    # Поле Пароль
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")

    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")

    # Ссылка "Войти"
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")

    # Ошибка "Некорректный пароль"
    INVALID_PASSWORD_ERROR = (By.XPATH, ".//p[contains(text(),'Некорректный пароль')]")



class ForgotPasswordPageLocators:
    # Ссылка "Войти"
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")



class ProfilePageLocators:
    # Поле Email
    LOGIN_INPUT = (By.XPATH, ".//label[text()='Логин']/following-sibling::input")
    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

