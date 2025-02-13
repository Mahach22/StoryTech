# Задания
1. Мониторинг. Дашборды должны быть публичными
  - Дашборд активности пользователей в юпитер (количество операций в день)
  - Дашборд по топовым тетрадкам (сколько подъедают)
  - Дашборд топовых таблиц в постресе с их владельцами
2. Алерты
  - Настроить алерт при заходе пользователя на сервер по ssh на почту.
  - Настроить почтовый алерт при потребление общим количеством контейнеров мощности более чем на 80 % - алертить.

## Мониторинг
Для упрощения развертывания я сделал [баш скрипт](jupyterhub/deploy.sh).
Процесс развертывания jupyterhub включает в себя 2 этапа:
1. Идёт сборка образа jupyter notebook с необходимыми нам предустановленными библиотеками из следующего [dockerfile](jupyterhub/dockerfile.notebook).
2. С использованием [docker compose](jupyterhub/docker-compose.yml) идёт сборка jupyterhub из [dockerfile](jupyterhub/dockerfile) и [конфига jupyterhub](jupyterhub/config/jupyterhub_config.py)



## Алерт ssh
Postgres устанавливаем командой `docker compose up -d` в директории нашего [docker compose](postgres/docker-compose.yml). Также для удобства тестрирования сразу создается таблица [файлом init.sql](postgres/init.sql)


## Алерт containers hight cpu usage
После развертывания всех контейнеров и запуска jupyter notebook, мы можем проверить подключение к postgres используя [python скрипт](connect_to_postgres.py). Так как psycopg2 у нас предустановлен, отдельно его устанавливать в юпитер ноутбук не нужно.

![sql](img/jupyter-notebook.png)
