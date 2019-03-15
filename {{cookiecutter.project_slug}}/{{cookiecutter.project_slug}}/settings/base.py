"""
Django settings for {{cookiecutter.project_slug}} project.

"""
import os

from django.utils.translation import ugettext_lazy as _

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.settings',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.contrib.styleguide',
    'modelcluster',
    'taggit',

    'widget_tweaks',
    'easy_thumbnails',
    'capture_tag',
    'ckeditor',
    'ckeditor_uploader',
    'background_task',

    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'autofixture',
    'rules.apps.AutodiscoverRulesConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'adhocracy4.categories',
    'adhocracy4.ckeditor',
    'adhocracy4.dashboard',
    'adhocracy4.filters',
    'adhocracy4.forms',
    'adhocracy4.administrative_districts',
    'adhocracy4.images',
    'adhocracy4.maps',
    'adhocracy4.rules',
    'adhocracy4.organisations',
    'adhocracy4.phases',
    'adhocracy4.projects',
    'adhocracy4.ratings',
    'adhocracy4.reports',
    'adhocracy4.modules',
    'adhocracy4.comments',

    'cms.home',
    'cms.snippets',

    'apps.contrib',
    'apps.ideas',
    {% if cookiecutter.use_maps_and_mapideas == 'y' %}
    'apps.mapideas',
    {% endif %}
    'apps.organisations',
    'apps.projects',
    'apps.users'
]

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
)

SITE_ID = 1

ROOT_URLCONF = '{{cookiecutter.project_slug}}.urls'

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '{{cookiecutter.project_slug}}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
        }
    }
}


AUTHENTICATION_BACKENDS = (
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_ALLOW_NONIMAGE_FILES = False

CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink']
        ]
    },
    'image-editor': {
        'width': '100%',
        'title': _('Rich text editor'),
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['Image'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink']
        ]
    },
    'collapsible-image-editor': {
        'width': '100%',
        'title': _('Rich text editor'),
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['Image'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ['CollapsibleItem']
        ]
    }
}

BLEACH_LIST = {
    'default' : {
        'tags': ['p','strong','em','u','ol','li','ul','a'],
        'attributes': {
            'a': ['href', 'rel'],
        },
    },
    'image-editor': {
        'tags': ['p','strong','em','u','ol','li','ul','a','img'],
        'attributes': {
            'a': ['href', 'rel'],
            'img': ['src', 'alt', 'style']
        },
        'styles': [
            'float',
            'margin',
            'padding',
            'width',
            'height',
            'margin-bottom',
            'margin-top',
            'margin-left',
            'margin-right',
        ],
    },
    'collapsible-image-editor': {
        'tags': ['p', 'strong', 'em', 'u', 'ol', 'li', 'ul', 'a', 'img',
                 'div'],
        'attributes': {
            'a': ['href', 'rel'],
            'img': ['src', 'alt', 'style'],
            'div': ['class']
        },
        'styles': [
            'float',
            'margin',
            'padding',
            'width',
            'height',
            'margin-bottom',
            'margin-top',
            'margin-left',
            'margin-right',
        ]
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('de', _('German'))
]

# The default language is used for emails and strings
# that are stored translated to the database.
DEFAULT_LANGUAGE = 'de'

# fixtures

FIXTURE_DIRS = [ os.path.join(PROJECT_DIR, 'fixtures') ]

IMAGE_ALIASES = {
    '*': {
        'max_size': 5*10**6,
        'fileformats': ('image/png', 'image/jpeg', 'image/gif')
    },
    'tileimage': {'min_resolution': (500, 300)},
    'heroimage': {'min_resolution': (1300, 600)},
    'logo': {'min_resolution': (200, 200), 'aspect_ratio': (1, 1)},
    'avatar': {'min_resolution': (200, 200)},
    'idea_image': {'min_resolution': (800, 200)},
}

THUMBNAIL_ALIASES = {
    '': {
        'heroimage': {'size': (1500, 500), 'crop': 'smart'},
        'thumbnail': {'size': (240, 240), 'crop': 'smart'},
        'avatar': {'size': (60, 60), 'crop': 'smart'},
        'heroimage_preview': {'size': (880, 220), 'crop': 'smart'},
        'project_thumbnail': {'size': (520, 330), 'crop': 'smart'},
        'idea_image': {'size': (800, 0), 'crop': 'scale'},
        'idea_thumbnail': {'size': (240, 240), 'crop': 'smart'},
        'map_thumbnail': {'size': (400, 200), 'crop': 'smart'},
        'organisation_thumbnail': {'size': (740, 540), 'crop': 'smart'},
        'avatar_small': {'size': (60, 60), 'crop': 'smart'},
        'org_avatar_small': {'size': (60, 60), 'crop': 'scale'},
        'org_avatar_medium': {'size': (200, 200), 'crop': 'scale'},
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': False,
        'BUNDLE_DIR_NAME': '/static/', # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}


STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Wagtail settings
WAGTAIL_SITE_NAME = "{{cookiecutter.project_slug}}"


# Authentification

AUTH_USER_MODEL = '{{cookiecutter.project_app_prefix}}_users.User'

LOGIN_URL = 'account_login'
LOGOUT_URL = 'account_logout'
LOGIN_REDIRECT_URL = '/'

#ACCOUNT_ADAPTER = 'apps.users.adapters.AccountAdapter'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300  # seconds
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

# Rest framework

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

#A4 based Settings
A4_ORGANISATIONS_MODEL = "{{ cookiecutter.project_app_prefix }}_organisations.Organisation"

A4_COMMENTABLES = (
    ('a4comments', 'comment'),
    ('{{ cookiecutter.project_app_prefix }}_ideas', 'idea'),
{% if cookiecutter.use_maps_and_mapideas == 'y' %}
    ('{{ cookiecutter.project_app_prefix }}_mapideas', 'mapidea'),
{% endif %}
)

A4_RATEABLES = (
    ('a4comments', 'comment'),
    ('{{ cookiecutter.project_app_prefix }}_ideas', 'idea'),
{% if cookiecutter.use_maps_and_mapideas == 'y' %}
    ('{{ cookiecutter.project_app_prefix }}_mapideas', 'mapidea'),
{% endif %}
)

A4_REPORTABLES = (
    ('a4comments', 'comment'),
    ('{{ cookiecutter.project_app_prefix }}_ideas', 'idea'),
{% if cookiecutter.use_maps_and_mapideas == 'y' %}
    ('{{ cookiecutter.project_app_prefix }}_mapideas', 'mapidea'),
{% endif %}
)

ACTIONABLE = [
    ('a4comments', 'comment'),
    ('{{ cookiecutter.project_app_prefix }}_ideas', 'idea'),
{% if cookiecutter.use_maps_and_mapideas == 'y' %}
    ('{{ cookiecutter.project_app_prefix }}_mapideas', 'mapidea'),
{% endif %}
]

A4_CATEGORIZABLE = (
    ('{{ cookiecutter.project_app_prefix }}_ideas', 'idea'),
{% if cookiecutter.use_maps_and_mapideas == 'y' %}
    ('{{ cookiecutter.project_app_prefix }}_mapideas', 'mapidea'),
{% endif %}
)

A4_PROJECT_TOPICS = ()

A4_MAP_BASEURL = 'https://{s}.tile.openstreetmap.org/'
A4_MAP_ATTRIBUTION = '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors'
A4_MAP_BOUNDING_BOX = ([[54.983, 15.016], [47.302, 5.988]])

A4_DASHBOARD = {
    'PROJECT_DASHBOARD_CLASS': 'adhocracy4.dashboard.ProjectDashboard',
    'BLUEPRINTS': 'apps.dashboard.blueprints.blueprints'
}
