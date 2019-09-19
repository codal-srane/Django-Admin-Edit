from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
	username_validator = UnicodeUsernameValidator()
	email = models.EmailField(_('email address'), unique=True, blank=False, 
    	help_text=_('Required.'))
	country = models.CharField(max_length=150, blank=False)
	first_name = models.CharField(_('first name'), max_length=150, blank=False)
	last_name = models.CharField(_('last name'), max_length=150, blank=False)
	username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        blank=False,
        help_text=_('Required. 150 characters or fewer. '
        	'Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
	)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __str__(self):
		return self.email