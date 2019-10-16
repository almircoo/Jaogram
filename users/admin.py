#user admin classes
#django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
#models
from django.contrib.auth.models import User
from users.models import Profile

# Register your models here.
#admin.site.register(Profile)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """docstring forProfileAdmin."""

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'phone_number')

    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')

    fieldsets = (
         ('Profile', {
             'fields': (('user', 'picture'),),
         }),
         ('Extra info', {
             'fields': (('website', 'phone_number'), ('biography'))
         }),
         ('metadate', {
              'fields': (('created', 'modified'),),
         }),
    )

    readonly_fields = ('created', 'modified',)

class ProfileInline(admin.StackedInline):
    """docstring forProfileInline admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """docstring forUserAdmin. add profile to base user admin"""

    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
