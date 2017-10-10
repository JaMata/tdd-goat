from fabric.api import run
from fabric.context_managers import settings


def _get_manage_dot_py(host):
	# was {host}
	return f'~/sites/jfoste.gq/virtualenv/bin/python ~/sites/jfoste.gq/source/manage.py'


def reset_database(host):
	manage_dot_py = _get_manage_dot_py(host)
	with settings(host_string=f'ubuntu@{host}'):  
		run(f'{manage_dot_py} flush --noinput')  


def create_session_on_server(host, email):
	manage_dot_py = _get_manage_dot_py(host)
	with settings(host_string=f'ubuntu@{host}'):  
		session_key = run(f'{manage_dot_py} create_session {email}')  
		return session_key.strip()