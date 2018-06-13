from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from . import USERNAME_INVALID_MESSAGE
from . import USERNAME_REGEX


USERNAME_NOT_UNIQUE = _('A user with that username already exists.')
USERNAME_HELP = _('Required. 60 characters or fewer. Letters, digits, spaces '
                  'and @/./+/-/_ only.')
USERNAME_VALIDATOR = validators.RegexValidator(USERNAME_REGEX,
                                               USERNAME_INVALID_MESSAGE,
                                               'invalid')

EMAIL_NOT_UNIQUE = _('A user with that email address already exists.')

IS_STAFF_HELP = _('Designates whether the user can log into this admin site.')
IS_ACTIVE_HELP = _('Designates whether this user should be treated as active. '
                   'Unselect this instead of deleting accounts.')


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    username = models.CharField(_('username'),
                                max_length=60, unique=True,
                                help_text=USERNAME_HELP,
                                validators=[USERNAME_VALIDATOR],
                                error_messages={
                                    'unique': _(USERNAME_NOT_UNIQUE),
    })

    email = models.EmailField(_('email address'), unique=True,
                              error_messages={
                                  'unique': EMAIL_NOT_UNIQUE,
    })
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=IS_STAFF_HELP)
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=IS_ACTIVE_HELP)
    date_joined = models.DateTimeField(editable=False, default=timezone.now)

    objects = auth_models.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
