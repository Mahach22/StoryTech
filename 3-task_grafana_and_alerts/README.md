# Задания
1. Мониторинг. Дашборды должны быть публичными
  - Дашборд активности пользователей в юпитер (количество операций в день)
  - Дашборд по топовым тетрадкам (сколько подъедают)
  - Дашборд топовых таблиц в постресе с их владельцами
2. Алерты
  - Настроить алерт при заходе пользователя на сервер по ssh на почту.
  - Настроить почтовый алерт при потребление общим количеством контейнеров мощности более чем на 80 % - алертить.

## Мониторинг
- [Дашбород активности пользователей JupyterHub](https://grafana.story-tech.ru/public-dashboards/68f835b78d6848d5bde2eda44bf77863)
  Реализация через прямой сбор метрик с юпитерхаба прометеусом.
- [Дашбород топовых тетрадок(по размеру) юпитер ноутбуков](https://grafana.story-tech.ru/public-dashboards/58614ae327a4487aa84d6dc0192b7c2a)
  реализовано с помощью баш скрипта, который записывает данные контейнеров юпитер ноутбуков. Обновление данных через крон, сбор с помощью нод экспортера, прометеуса и вывод в графану.
- [Дашборд топовых таблиц постгрес с их владельцами](https://grafana.story-tech.ru/public-dashboards/034c81d55254466caf571622cbafd515)
  реализация через прямое подключение постгреса в графану и запросы в постгрес.


## Алерт ssh
Postgres устанавливаем командой `docker compose up -d` в директории нашего [docker compose](postgres/docker-compose.yml). Также для удобства тестрирования сразу создается таблица [файлом init.sql](postgres/init.sql)
sudo apt install mailutils postfix
sudo nano /etc/postfix/main.cf



## Алерт использование процессора контейнерами выше 80%
После развертывания всех контейнеров и запуска jupyter notebook, мы можем проверить подключение к postgres используя [python скрипт](connect_to_postgres.py). Так как psycopg2 у нас предустановлен, отдельно его устанавливать в юпитер ноутбук не нужно.

relayhost = [smtp.mail.ru]:465
smtp_tls_wrappermode = yes
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
smtp_sasl_security_options = noanonymous
smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt
smtp_use_tls = yes
smtp_tls_security_level = encrypt


sasl_passwd
[smtp.mail.ru]:465 emaillogin:password

sudo chmod 600 /etc/postfix/sasl_passwd

sudo systemctl restart postfix

sudo nano /etc/pam.d/sshd
session    required   pam_exec.so /wolf/docker/StoryTech/3-task_grafana_and_alerts/ssh_alert.sh $PAM_USER $PAM_HOST
sudo systemctl restart

![sql](img/jupyter-notebook.png)
