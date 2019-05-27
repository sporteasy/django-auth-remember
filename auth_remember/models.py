# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import check_password

from django.conf import settings


class RememberTokenManager(models.Manager):

    def get_by_string(self, token_string):
        """Return the token for the given token_string"""
        try:
            user_id, token_raw = token_string.split(':')
        except ValueError:
            return

        max_age = timezone.now() - timedelta(seconds=settings.COOKIE_AGE)
        for token in self.filter(created_initial__gte=max_age, user=user_id):
            if check_password(token_raw, token.token_hash):
                return token

    def clean_remember_tokens(self):
        max_age = timezone.now() - timedelta(seconds=settings.COOKIE_AGE)
        return self.filter(created_initial__lte=max_age).delete()


class RememberToken(models.Model):

    class Meta:
        app_label = 'auth_remember'

    token_hash = models.CharField(max_length=165, blank=False, primary_key=True)

    created = models.DateTimeField(editable=False, null=True, default=timezone.now)

    created_initial = models.DateTimeField(editable=False, blank=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="remember_me_tokens")

    objects = RememberTokenManager()
