from django.conf import settings

TOKEN_MODEL = 'auth_remember.models.RememberToken'

COOKIE_NAME = 'remember_token'
COOKIE_AGE = 86400 * 28  # 4 weeks by default
SESSION_KEY = 'AUTH_REMEMBER_FRESH'
SECRET_KEY = '^6tnq74+d2u*=e1em1os6q%(14*0)3y^m$^)ew1v+^!awe&#73'

for k in dir(settings):
    if k.startswith('AUTH_REMEMBER_'):
        locals()[k.split('AUTH_REMEMBER_', 1)[1]] = getattr(settings, k)
