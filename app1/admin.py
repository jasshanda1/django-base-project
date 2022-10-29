from django.contrib import admin
from app1.models.UserModel import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'user_name', 'email', 'password']