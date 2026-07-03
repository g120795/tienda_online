from django.test import TestCase

# Create your tests here.


"""❯ python manage.py runserver
Watching for file changes with StatReloader
Exception in thread django-main-thread:
Traceback (most recent call last):
  File "/usr/lib/python3.14/threading.py", line 1082, in _bootstrap_inner
    self._context.run(self.run)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/usr/lib/python3.14/threading.py", line 1024, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/deadpool/dev/templates/python_projects/tienda_online/venv/lib/python3.14/site-packages/django/utils/autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
    ~~^^^^^^^^^^^^^^^^^
  File "/home/deadpool/dev/templates/python_projects/tienda_online/venv/lib/python3.14/site-packages/django/core/management/commands/runserver.py", line 124, in inner_run
    autoreload.raise_last_exception()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/home/deadpool/dev/templates/python_projects/tienda_online/venv/lib/python3.14/site-packages/django/utils/autoreload.py", line 86, in raise_last_exception
    raise _exception[1]
  File "/home/deadpool/dev/templates/python_projects/tienda_online/venv/lib/python3.14/site-packages/django/core/management/__init__.py", line 395, in execute
    autoreload.check_errors(django.setup)()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/home/deadpool/dev/templates/python_projects/tienda_online/venv/lib/python3.14/site-packages/django/utils/autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
    ~~^^^^^^^^^^^^^^^^^
  File "/home/deadpool/dev/templates/python_projects/tienda_online/venv/lib/python3.14/site-packages/django/__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/deadpool/dev/templates/python_projects/tienda_online/venv/lib/python3.14/site-packages/django/apps/registry.py", line 91, in populate
    app_config = AppConfig.create(entry)
  File "/home/deadpool/dev/templates/python_projects/tienda_online/venv/lib/python3.14/site-packages/django/apps/config.py", line 178, in create
    mod = import_module(mod_path)
  File "/usr/lib/python3.14/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1406, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1371, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1314, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 491, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1406, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1371, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1314, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 491, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1406, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1371, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1342, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 938, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 759, in exec_module
  File "<frozen importlib._bootstrap>", line 491, in _call_with_frames_removed
  File "/home/deadpool/dev/templates/python_projects/tienda_online/apps/__init__.py", line 2, in <module>
    from .users import *
  File "/home/deadpool/dev/templates/python_projects/tienda_online/apps/users/__init__.py", line 1, in <module>
    from .models import Profile
  File "/home/deadpool/dev/templates/python_projects/tienda_online/apps/users/models.py", line 2, in <module>
    from django.contrib.auth.models import User
  File "/home/deadpool/dev/templates/python_projects/tienda_online/venv/lib/python3.14/site-packages/django/contrib/auth/models.py", line 5, in <module>
    from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
  File "/home/deadpool/dev/templates/python_projects/tienda_online/venv/lib/python3.14/site-packages/django/contrib/auth/base_user.py", line 43, in <module>
    class AbstractBaseUser(models.Model):
    ...<120 lines>...
            )
  File "/home/deadpool/dev/templates/python_projects/tienda_online/venv/lib/python3.14/site-packages/django/db/models/base.py", line 131, in __new__
    app_config = apps.get_containing_app_config(module)
  File "/home/deadpool/dev/templates/python_projects/tienda_online/venv/lib/python3.14/site-packages/django/apps/registry.py", line 260, in get_containing_app_config
    self.check_apps_ready()
    ~~~~~~~~~~~~~~~~~~~~~^^
  File "/home/deadpool/dev/templates/python_projects/tienda_online/venv/lib/python3.14/site-packages/django/apps/registry.py", line 138, in check_apps_ready
    raise AppRegistryNotReady("Apps aren't loaded yet.")
django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet."""