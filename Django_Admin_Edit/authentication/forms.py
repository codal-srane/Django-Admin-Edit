from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext, gettext_lazy as _

from django.contrib.auth import get_user_model

class UserCreationAdminForm(UserCreationForm):
	class Meta:
		model = get_user_model()
		fields = ()