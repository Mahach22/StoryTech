CREATE TABLE test_table (
    name VARCHAR(10) NOT NULL CHECK (length(name) >= 4),
    surname VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    age INTEGER NOT NULL CHECK (age > 0 AND age <= 150)
);
INSERT INTO test_table (name, surname, city, age)
VALUES
    ('Иван', 'Иванов', 'Москва', 25),
    ('Мария', 'Петрова', 'Санкт-Петербург', 30),
    ('Александр', 'Сидоров', 'Екатеринбург', 28),
    ('Екатерина', 'Кузнецова', 'Казань', 22),
    ('Дмитрий', 'Смирнов', 'Нижний Новгород', 35),
    ('Ольга', 'Морозова', 'Волгоград', 20),
    ('Павел', 'Васильев', 'Омск', 29),
    ('Елена', 'Павлова', 'Ростов-на-Дону', 27),
    ('Андрей', 'Соколов', 'Челябинск', 24),
    ('Светлана', 'Попова', 'Уфа', 32),
    ('Николай', 'Лебедев', 'Самара', 21),
    ('Татьяна', 'Козлова', 'Красноярск', 26),
    ('Сергей', 'Михайлов', 'Пермь', 23),
    ('Анна', 'Новикова', 'Воронеж', 31),
    ('Максим', 'Зайцев', 'Калининград', 33),
    ('Юлия', 'Медведева', 'Тюмень', 18),
    ('Артем', 'Яковлев', 'Ижевск', 19),
    ('Виктория', 'Сорокина', 'Томск', 34),
    ('Игорь', 'Макаров', 'Кемерово', 17),
    ('Евгения', 'Беляева', 'Новосибирск', 36);
