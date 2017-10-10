from fabric.api import run, env
from fabric.context_managers import settings

env.user = 'ubuntu'
env.key_filename = '~/.ssh/django-foster.pem'

def _get_manage_dot_py(host):
	return f'~/sites/{host}/virtualenv/bin/python ~/sites/{host}/source/manage.py'


def reset_database(host):
	manage_dot_py = _get_manage_dot_py(host)
	with settings(host_string='ec2-34-226-196-38.compute-1.amazonaws.com'):  
		run(f'{manage_dot_py} flush --noinput')  


def create_session_on_server(host, email):
	manage_dot_py = _get_manage_dot_py(host)
	with settings(host_string='ec2-34-226-196-38.compute-1.amazonaws.com'):  
		session_key = run(f'{manage_dot_py} create_session {email}')  
		return session_key.strip()