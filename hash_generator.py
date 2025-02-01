from passlib.hash import bcrypt

# Функция для создания хеша пароля
def hash_password(password):
    return bcrypt.hash(password)

# Список пользователей и их паролей
users = {
    "user1": "пароль",
    "user2": "пароль",
    "user3": "пароль"
}

# Генерация хешей
passwords = {user: hash_password(pwd) for user, pwd in users.items()}

# Вывод результатов
for user, hashed_password in passwords.items():
    print(f"User: {user}, Hashed Password: {hashed_password}")
