# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import RememberToken


class RememberTokenAdmin(admin.ModelAdmin):
    class Meta:
        app_label = 'auth_remember'
        db_table = 'remembertokenadmin'

    list_display = ('user', 'token_hash', 'created', 'created_initial')


admin.site.register(RememberToken, RememberTokenAdmin)
