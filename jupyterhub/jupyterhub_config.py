from dockerspawner import DockerSpawner
import os, nativeauthenticator

c = get_config()

c.JupyterHub.authenticator_class = 'native'
c.JupyterHub.template_paths = [f"{os.path.dirname(nativeauthenticator.__file__)}/templates/"]
c.NativeAuthenticator.open_signup = True
c.NativeAuthenticator.check_common_password = True
c.NativeAuthenticator.allowed_failed_logins = 3
c.NativeAuthenticator.seconds_before_next_try = 1200
c.NativeAuthenticator.allowed_users = {'ekaterina'}
c.NativeAuthenticator.admin_users = {'ekaterina'}

c.JupyterHub.spawner_class = DockerSpawner
c.DockerSpawner.extra_host_config = {
    'runtime': 'nvidia',
    'device_requests': [{
        'Driver': 'nvidia',
        'Count': -1,
        'Capabilities': [['gpu']]
    }]
}
c.DockerSpawner.network_name = 'fintech_network'
c.DockerSpawner.remove = True
c.Spawner.http_timeout = 180
c.JupyterHub.shutdown_no_activity_timeout = 600
c.JupyterHub.shutdown_on_logout = True
c.DockerSpawner.environment = {
    'NVIDIA_VISIBLE_DEVICES': 'all'
}

c.DockerSpawner.image = "cschranz/gpu-jupyter:v1.7_cuda-12.2_ubuntu-22.04_python-only"

c.JupyterHub.log_level = 'DEBUG'
c.JupyterHub.hub_ip = '0.0.0.0'

c.JupyterHub.metrics_enabled = True
c.JupyterHub.metrics_port = 8000
c.JupyterHub.authenticate_prometheus = False

notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = {
    'jupyterhub-user-{username}': notebook_dir
}
c.JupyterHub.db_url = 'sqlite:////srv/jupyterhub/data/jupyterhub.sqlite'

