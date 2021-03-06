"""
Django settings for crabotter project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
from crabotter.settings.base import *
import os
import logging
import plotly.plotly as py

log = logging.getLogger(__name__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-rd$
if "RDS_HOSTNAME" in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ["RDS_TABLE_NAME"],
            'USER': os.environ["RDS_USERNAME"],
            'PASSWORD': os.environ["RDS_PASSWORD"],
            'HOST': os.environ["RDS_HOSTNAME"],
            'PORT': os.environ["RDS_PORT"],
        }
    }
else:
    log.warn("RDS_HOSTNAME not found in environment. Using sqlite as backup.")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

py.sign_in(os.environ["PLOTLY_USERNAME"], os.environ["PLOTLY_API_KEY"])
