import psycopg2

# Параметры подключения
db_params = {
    'dbname': 'dbname',
    'user': 'user',
    'password': 'password',
    'host': 'container_name',  
    'port': 5432
}

# Подключение к базе данных
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Выполнение SQL-запроса
    cursor.execute("SELECT * FROM test_table;")
    
    # Получение результатов
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Закрытие соединения
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")
