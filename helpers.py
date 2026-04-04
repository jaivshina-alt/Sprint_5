import random
import string


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