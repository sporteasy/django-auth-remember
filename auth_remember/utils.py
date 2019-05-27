import uuid
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.hashers import make_password

from .models import RememberToken


def create_token_string(user, token=None):
    """Create a new token object for the given `user` and return the
    token string.

    """
    token_value = uuid.uuid4().hex
    token_hash = make_password(token_value, hasher='sha1')
    token = RememberToken(
        token_hash=token_hash,
        created_initial=token.created_initial if token else None,
        user=user
    )

    # This is to make sure that created_initial == created incase there is no
    # token
    if token.created_initial is None:
        token.created_initial = token.created

    token.save()
    return '%d:%s' % (user.id, token_value)


def preset_cookie(request, token_string):
    """Create the cookie value for the token and save it on the request.

    The middleware will set the actual cookie (via `set_cookie`) on the
    response.

    """
    if token_string:
        request._auth_remember_token = token_string
    else:
        request._auth_remember_token = ''


def set_cookie(response, token):
    """Set the cookie with the remember token on the response object.

    The max_age value will be auto-calculated based on the datetime set via
    expires.

    """
    expires = datetime.utcnow() + timedelta(seconds=settings.COOKIE_AGE)

    response.set_cookie(
        settings.COOKIE_NAME, token,
        max_age=None, expires=expires,
        domain=settings.SESSION_COOKIE_DOMAIN,
        path=settings.SESSION_COOKIE_PATH,
        secure=settings.SESSION_COOKIE_SECURE or None,
        httponly=settings.SESSION_COOKIE_HTTPONLY or None
    )

    return response


def delete_cookie(response):
    response.set_cookie(
        settings.COOKIE_NAME, "deleted",
        max_age=0, expires='Thu, 01-Jan-1970 00:00:00 GMT',
        domain=settings.SESSION_COOKIE_DOMAIN,
        path=settings.SESSION_COOKIE_PATH,
        secure=settings.SESSION_COOKIE_SECURE or None,
        httponly=settings.SESSION_COOKIE_HTTPONLY or None)

    return response
