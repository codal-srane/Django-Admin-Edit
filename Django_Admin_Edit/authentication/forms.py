from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

class UserCreationAdminForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('email','username')