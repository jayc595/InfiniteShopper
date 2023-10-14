from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class AdminAccount(UserAdmin):
    # the below is this list of columns displayed in the Users grid in Admin.
    list_display = ('email', 'firstname', 'lastname', 'username', 'last_login', 'created_at', 'is_active')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, AdminAccount)
