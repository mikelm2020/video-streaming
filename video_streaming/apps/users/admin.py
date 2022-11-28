from apps.users.models import User
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):

    list_display = ("id", "email", "name", "last_name")
    search_fields = ("id", "email", "name", "last_name")
    ordering = ("name",)


admin.site.register(User, UserAdmin)
