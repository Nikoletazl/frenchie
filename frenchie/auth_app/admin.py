from django.contrib import admin

from frenchie.auth_app.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', )
