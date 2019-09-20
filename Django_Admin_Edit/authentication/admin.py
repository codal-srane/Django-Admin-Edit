from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationAdminForm

User = get_user_model()

class UserAdmin(UserAdmin):
	#class Meta:
	#	model = User	
	add_form = UserCreationAdminForm
	list_display = ['id', '__str__', 'date_joined', 'last_login', 'is_staff', 'is_active']
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