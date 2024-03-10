
from .settings import *
from .settings import INSTALLED_APPS

INSTALLED_APPS += [
	'rest_framework',
	'drf_yasg',
]

REST_FRAMEWORK = {
'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.AllowAny'
],
'DEFAULT_PAGINATION_CLASS': 'core.pagination.CustomPagination',
}
