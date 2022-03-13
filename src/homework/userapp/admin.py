from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User
from .forms import UserInfoForm

admin.site.unregister(Group)


@admin.register(User)
class UserAdminRep(admin.ModelAdmin):
    date_hierarchy = 'date_joined'
    list_display = ('username', 'first_name', 'last_name', 'user_type')
    list_filter = ('user_type', )
    search_fields = ('username', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'first_name', 'last_name',
                       'date_joined', 'last_login', 'user_type'),
            }),
    )

    def get_form(self, request, obj=None, change=None, **kwargs):
        if obj is None:
            return UserInfoForm
        return super().get_form(request, obj=obj, change=change, **kwargs)
