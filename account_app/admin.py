from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from account_app.models import Logintable, Usertable, Councellortable

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "email",
                    "first_name",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "user_type",
                    "is_active",
                    "is_superuser",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("username", "password1", "password2")},
        ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ("pk", "username", "first_name", "user_type")
    search_fields = ("username", "first_name")
    ordering = ("username",)

# Register the models with the admin site
admin.site.register(Logintable, CustomUserAdmin)
admin.site.register(Usertable)
admin.site.register(Councellortable)
