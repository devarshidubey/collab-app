from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'email', 'age', 'college', 'is_staff',]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age', 'college',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('age', 'college',)}),)


    
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)

