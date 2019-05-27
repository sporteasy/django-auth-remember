from django.contrib import admin
from auth_remember import models


class RememberTokenAdmin(admin.ModelAdmin):
    class Meta:
        app_label = 'auth_remember'
        db_table = 'remembertokenadmin'

    list_display = ('user', 'token_hash', 'created', 'created_initial')


admin.site.register(models.RememberToken, RememberTokenAdmin)
