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
  реализовано с помощью [баш скрипта](./check_volumes.sh), который записывает данные контейнеров юпитер ноутбуков. Обновление данных через крон, сбор с помощью нод экспортера, прометеуса и вывод в графану.
- [Дашборд топовых таблиц постгрес с их владельцами](https://grafana.story-tech.ru/public-dashboards/034c81d55254466caf571622cbafd515)
  реализация через прямое подключение постгреса в графану и запросы в постгрес.


## Алерт вход по ssh
Устанавливаем mailutils, который включает в себя postfix
```
sudo apt install mailutils
```
настраиваем данные сервера и аутентификации в файле postfix/main.cf
```
sudo nano /etc/postfix/main.cf
```
```
relayhost = [smtp.mail.ru]:465
smtp_tls_wrappermode = yes
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
smtp_sasl_security_options = noanonymous
smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt  
smtp_use_tls = yes                 #мыло.ру приходится использовать с тлс
smtp_tls_security_level = encrypt
```
настраиваем логин и пароль в файле postfix/sasl_passwd
```
[smtp.mail.ru]:465 emaillogin:password
```
устанавливаем доступ к данным логина и пароля только для рута
```
sudo chmod 600 /etc/postfix/sasl_passwd
```
перезапускаем postfix
```
sudo systemctl restart postfix
```
Настраиваем запуск [нашего скрипта](./ssh_alert.sh) при входе по ssh
```
sudo nano /etc/pam.d/sshd 
```
```
session    required   pam_exec.so /wolf/docker/StoryTech/3-task_grafana_and_alerts/ssh_alert.sh $PAM_USER $PAM_HOST
```
![alert_container](img/alert_ssh.png)

## Алерт использование процессора контейнерами выше 80%А
Алерты 



![alert_container](img/alet_container_cpu_usage.png)
<img src="img/alet_container_cpu_usage.png" alt="alert_container" width="300" height="200">
