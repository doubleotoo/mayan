from django.conf import settings

SHOW_OBJECT_TYPE = getattr(settings, 'SEARCH_SHOW_OBJECT_TYPE', True)
