import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '(b*%j%7mqfgnxa*acz$opc0gj++mksj$&rgaqmf&0(vnk4+@d&'

DEBUG = True

REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': [
		'rest_framework_simplejwt.authentication.JWTAuthentication',
	],
}
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'accounts.apps.AccountsConfig',
	'posts.apps.PostsConfig',
	'chanel.apps.ChanelConfig',
	'comment.apps.CommentConfig',
	'like.apps.LikeConfig',
	'notify.apps.NotifyConfig',
	'files.apps.FilesConfig',
	'rest_framework',
	'corsheaders',
]
MIDDLEWARE = [

	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sosial.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
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
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

WSGI_APPLICATION = 'sosial.wsgi.application'

AUTH_USER_MODEL = 'accounts.User'
SIMPLE_JWT = {
	'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=360),
	'ROTATE_REFRESH_TOKENS': True,
	'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=365),
	'SLIDING_TOKEN_LIFETIME': datetime.timedelta(days=360),
	'SLIDING_TOKEN_REFRESH_LIFETIME': datetime.timedelta(days=365),
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.mysql',
# 		'NAME': 'social',
# 		'USER': 'root',
# 		'PASSWORD': '123',
# 		'HOST': '127.0.0.1',
# 		'PORT': '3306',
# 	}
# }

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_ROOT = os.path.join(BASE_DIR,'static','media')
MEDIA_URL = '/media/'


AUTH_PASSWORD_VALIDATORS = [
	{
		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
	},
	{
		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
	},
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'vahidtwotwotwo22@gmail.com'
EMAIL_HOST_PASSWORD = 'FJfWGhvDfs7Y6yY'