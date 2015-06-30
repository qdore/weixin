#!/usr/bin/env python
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(os.path.curdir)), "third-party"))

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', 'django'])
    finally:
        globals()[package] = importlib.import_module(package)

install_and_import('django')
        
if __name__ == "__main__":
    if os.path.isfile("project/localsettings.py"):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.localsettings")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
