from amazon_app.settings.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Static files via Amazon S3 (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

INSTALLED_APPS += ('storages',)
AWS_STORAGE_BUCKET_NAME = "b-django-foster"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL