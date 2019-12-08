import random
from datetime import datetime
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run, sudo,task, prefix
from fabric.utils import fastprint, abort
from contextlib import contextmanager
from configparser import RawConfigParser

# ----------------------------------------------------------------------
config = RawConfigParser()
config.read('maximebn/settings.ini')
USER_FOLDER = config.get('fabfile', 'USER_FOLDER')
SITE_FOLDER = config.get('fabfile', 'SITE_FOLDER')
PROD_SETTINGS = config.get('fabfile', 'PROD_SETTINGS')
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Optional : status decorators
# ----------------------------------------------------------------------
def print_status(description):
    def print_status_decorator(fn):
        def print_status_wrapper():
            now = datetime.now().strftime('%H:%M:%S')
            fastprint('({time}) {description}{suffix}'.format(
                time=now,
                description=description.capitalize(),
                suffix='...\n')
            )
            fn()
            now = datetime.now().strftime('%H:%M:%S')
            fastprint('({time}) {description}{suffix}'.format(
                time=now,
                description='...finished '+description,
                suffix='.\n')
            )
        return print_status_wrapper
    return print_status_decorator


# ----------------------------------------------------------------------
# Main deployment task
# ----------------------------------------------------------------------
@task(alias='deploy')
def update_and_deploy_on_remote():
    with cd(USER_FOLDER):
        #_run_tests()
        _get_latest_source()
        _update_virtualenv()
        _update_static_files()
        _update_database()
        _restart_application()


# ----------------------------------------------------------------------
# Sub tasks
# ----------------------------------------------------------------------

# Reclaim latest source from git repo : either cloning it or updating it
@print_status('getting the latest source code')
def _get_latest_source():
    with cd(SITE_FOLDER):
        result = run('git fetch origin master')
        current_commit = local("git log -n 1 --format=%H", capture=True)  
        run(f'git reset --hard {current_commit}')  
        if result.failed:
            abort('No git repository')



# Running tests
def _run_tests():
    with cd(SITE_FOLDER):
        test_command = '../venv/bin/coverage run manage.py test'
        result = local(test_command + ' --settings=maximebn.settings.settings-prod')
        if result.failed:
            abort('Coverage tests failed')

# Update virtual environment
@print_status('installing new required dependencies in virtual env')
def _update_virtualenv():
    with cd(SITE_FOLDER):
        run('../venv/bin/pip3 install -r requirements.txt')

# Updating static files
@print_status('updating static files')
def _update_static_files():
    with cd(SITE_FOLDER):
        run(f'../venv/bin/python3 manage.py collectstatic --noinput --settings={PROD_SETTINGS} --noinput')

# Migrating database
@print_status('operating database migration operations')
def _update_database():
    with cd(SITE_FOLDER):
        run(f'../venv/bin/python3 manage.py makemigrations --settings={PROD_SETTINGS} --noinput')
        run(f'../venv/bin/python3 manage.py migrate --settings={PROD_SETTINGS} --noinput')

# Restarting application
@print_status('restarting application')
def _restart_application():
    sudo('supervisorctl reread')
    sudo('supervisorctl reload')
    sudo('service nginx restart')