from django.conf import settings

TOKEN_MODEL = 'auth_remember.models.RememberToken'

COOKIE_NAME = 'remember_token'
COOKIE_AGE = 86400 * 28  # 4 weeks by default
SESSION_KEY = 'AUTH_REMEMBER_FRESH'


for k in dir(settings):
    if k.startswith('AUTH_REMEMBER_') and getattr(settings, k, None) is not None:
        locals()[k] = getattr(settings, k)
