from django.contrib import admin
from .models import Biography, Quote, Legacy

"""
Register Django admin classes for models Biography, Quote, and Legacy.
"""

admin.site.register(Biography)
admin.site.register(Quote)
admin.site.register(Legacy)
