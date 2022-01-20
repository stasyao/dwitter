from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    # Демонстрируем только поле `username` модели User
    fields = ["username"]
    inlines = [ProfileInline]


admin.site.unregister([Group, User])
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)
