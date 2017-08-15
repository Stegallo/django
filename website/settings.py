from decouple import config
from unipath import Path
import dj_database_url

PROJECT_DIR = Path(__file__).parent


SECRET_KEY = config('SECRET_KEY')


DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social_django',
    'website.apps.core',
    # 'website.apps.stravauth',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    # 'social_django.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ PROJECT_DIR.child('templates') ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect', # <--
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'



DATABASES = {
    'default': dj_database_url.config(
        default = config('DATABASE_URL')
    )
}



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_ROOT = PROJECT_DIR.parent.parent.child('static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
)

MEDIA_ROOT = PROJECT_DIR.parent.parent.child('media')
MEDIA_URL = '/media/'

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'



AUTHENTICATION_BACKENDS = (
    # 'social_core.backends.github.GithubOAuth2',
    # 'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    # 'social_core.backends.strava.StravaOAuth',
    # 'social_core.backends.moves.MovesOAuth2',
    # 'website.apps.stravauth.backend.StravaV3Backend',
    'social_core.backends.tripit.TripItOAuth',

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = config('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = config('SOCIAL_AUTH_FACEBOOK_SECRET')


SOCIAL_AUTH_TRIPIT_KEY = config('SOCIAL_AUTH_TRIPIT_KEY')
SOCIAL_AUTH_TRIPIT_SECRET = config('SOCIAL_AUTH_TRIPIT_SECRET')

# SOCIAL_AUTH_STRAVA_KEY = config('CLIENT_ID')
# SOCIAL_AUTH_STRAVA_SECRET = config('CLIENT_SECRET')

# SOCIAL_AUTH_MOVES_KEY = config('MOVES_ID')
# SOCIAL_AUTH_MOVES_SECRET = config('MOVES_SECRET')

# SOCIAL_AUTH_MOVES_SCOPE = ['activity', 'location']

SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/settings/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
