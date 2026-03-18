# Проект автоматизации тестирования сервиса Stellar Burgers

1. Проект реализован с использованием:
- **Selenium WebDriver** для автоматизации браузера
- **pytest** - фреймворк для написания и запуска автотестов
- **Python 3** - язык программирования

2. Установить виртуальное окружение и зависимости

```bash
# Создание виртуального окружения
python3 -m venv venv

# Активация виртуального окружения
# На macOS/Linux:
source venv/bin/activate
# На Windows:
venv\Scripts\activate

# Установка зависимости
pip install -r requirements.txt
```

3. Команда для запуска автотестов 

```bash
pytest -v
```

4. Проект использует генераторы для создания уникальных тестовых данных:

- **generate_email()** - генерирует уникальный email в формате `julia_ivshina_42_XXX@yandex.ru`
- **generate_password()** - генерирует случайный пароль (по умолчанию 10 символов, минимум 6)

Эти функции находятся в файле `conftest.py` и используются в фикстурах.

5. Проект использует следующие pytest-фикстуры (определены в `conftest.py`):

- **driver** - создает и закрывает браузер Chrome для каждого теста
- **wait** - предоставляет объект WebDriverWait с таймаутом 5 секунд
- **user_credentials** - данные существующего пользователя для тестов логина
- **new_user_credentials** - данные нового пользователя для тестов регистрации
- **login** - автоматически логинит пользователя перед тестом

6. Все локаторы элементов страниц организованы в классы в файле `locators.py`:

- **HomePageLocators** - элементы главной страницы и конструктора https://stellarburgers.education-services.ru/
- **LoginPageLocators** - элементы страницы входа https://stellarburgers.education-services.ru/login
- **RegisterPageLocators** - элементы страницы регистрации https://stellarburgers.education-services.ru/register
- **ForgotPasswordPageLocators** - элементы страницы восстановления пароля https://stellarburgers.education-services.ru/forgot-password
- **ProfilePageLocators** - элементы страницы профиля https://stellarburgers.education-services.ru/account/profile