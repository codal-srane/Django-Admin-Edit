from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .forms import UserCreationAdminForm

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
	add_form = UserCreationAdminForm
	model = User
	add_fieldsets = (
		(None, {
            'fields': (
            	'email', 
            	'username', 
            	'password1', 
            	'password2', ),
		}),
	)

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)