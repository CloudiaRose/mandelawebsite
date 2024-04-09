from django.contrib import admin
# Register your models here.
from .models import Biography, Quote, Legacy

admin.site.register(Biography)
admin.site.register(Quote)
admin.site.register(Legacy)
