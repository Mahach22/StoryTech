from dockerspawner import DockerSpawner
import os, nativeauthenticator

c = get_config()

# Используем NativeAuthenticator для аутентификации пользователей
c.JupyterHub.authenticator_class = 'nativeauthenticator.NativeAuthenticator'
c.JupyterHub.template_paths = [f"{os.path.dirname(nativeauthenticator.__file__)}/templates/"]
c.NativeAuthenticator.open_signup = True  # включение регистрации
c.NativeAuthenticator.check_common_password = True  # Проверка на использование распространенных паролей
c.NativeAuthenticator.allowed_failed_logins = 5     # Максимум 5 неудачных попыток входа
c.NativeAuthenticator.seconds_before_next_try = 1200  # Заблокировать пользователя на 20 минут после 3 неудачных попыток
c.Authenticator.admin_users = {'mahach'}  # Администраторы системы
c.Authenticator.allowed_users = {'mahach', 'user2', 'user3'} # Список разрешенных пользователей (3 учетные записи)

# Использование DockerSpawner для создания контейнеров для каждого пользователя
c.JupyterHub.spawner_class = DockerSpawner

c.DockerSpawner.image = "storytech-jupyter-notebook"  # кастомный образ с нужными библиотеками
c.DockerSpawner.network_name = 'storytech_network'
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
