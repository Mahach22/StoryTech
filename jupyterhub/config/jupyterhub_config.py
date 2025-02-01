from dockerspawner import DockerSpawner
import os

c = get_config()

# Используем NativeAuthenticator для аутентификации пользователей
c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'

# Настройка безопасности аутентификации
c.NativeAuthenticator.check_common_password = True  # Проверка на использование распространенных паролей
c.NativeAuthenticator.allowed_failed_logins = 3     # Максимум 3 неудачных попытки входа
c.NativeAuthenticator.seconds_before_next_try = 1200  # Заблокировать пользователя на 20 минут после 3 неудачных попыток

# Список разрешенных пользователей (3 учетные записи)
c.Authenticator.allowed_users = {'user1', 'user2', 'user3'}

# Пароли для пользователей 
# Хешированные пароли для пользователей
c.Authenticator.users = [
    {
        "name": "user1",
        "password": "$2b$12$OWW.h8ZYFKMAUXyv/Ch7HOtxtcFPFyqjT3EzWNJqF0hY6ZmHAZmnS"  
    },
    {
        "name": "user2",
        "password": "$2b$12$0WqTiw23qg2vXbZZNttVEuiCLdpMoOnwde15fl50ylDy3ycwHMKHy"  
    },
    {
        "name": "user3",
        "password": "$2b$12$VSS0pF0LTlbDwn6cua8kUuR2SBslhpwt/.z1gnZIEtLKv52NB7ty6"  
    }
]


# Администраторы системы
c.Authenticator.admin_users = {'user1'}  # Например, user1 будет иметь права администратора

# Использование DockerSpawner для создания контейнеров для каждого пользователя
c.JupyterHub.spawner_class = DockerSpawner

c.DockerSpawner.image = "jupyter/base-notebook:latest"  # Базовый образ без GPU
c.DockerSpawner.network_name = 'jupyter_network'
c.DockerSpawner.remove = True  # Удалять контейнеры после выхода пользователя
c.Spawner.http_timeout = 180   # Таймаут для HTTP-запросов

# Настройка директории для ноутбуков
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir

# Монтирование томов для хранения данных пользователей
c.DockerSpawner.volumes = {
    'jupyterhub-user-{username}': notebook_dir
}

# Настройка базы данных
c.JupyterHub.db_url = 'sqlite:////srv/jupyterhub/data/jupyterhub.sqlite'

# Логирование
c.JupyterHub.log_level = 'DEBUG'

# Настройки хоста
c.JupyterHub.hub_ip = '0.0.0.0'

# Настройки простоя
c.JupyterHub.shutdown_no_activity_timeout = 600  # Автоматическое завершение работы через 10 минут простоя
c.JupyterHub.shutdown_on_logout = True  # Завершать работу сервера при выходе пользователя

# Prometheus метрики (если нужны)
c.JupyterHub.metrics_enabled = True
c.JupyterHub.metrics_port = 8000
c.JupyterHub.authenticate_prometheus = False
