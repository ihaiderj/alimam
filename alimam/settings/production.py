from .base import *

DEBUG = False

ALLOWED_HOSTS = ['immy66.pythonanywhere.com']

ROOT_URLCONF = 'alimam.urls'

SECRET_KEY = 'u97rfa!#(qlkqb@3vcim=dcl*4u12y_ntj#aw1u((beq#glafp'

try:
    from .local import *
except ImportError:
    pass
