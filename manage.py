#!/usr/bin/env python
import os
from subprocess import check_output
import sys

# Add GAE libs to path
try:
    appserver_location = check_output("which dev_appserver.py", shell=True).strip()
    appserver_path = os.path.split(os.path.realpath(appserver_location))[0]
    sys.path.insert(0, appserver_path)
    sys.path.insert(0, os.path.join(os.path.join(appserver_path,'lib'),'django-1.5'))
except:
    print "Cant find appserver, probably going to fail"

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
