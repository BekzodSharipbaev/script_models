from django.contrib import admin

from .models import SiteUser, Song, Concert

# Register your models here.
admin.site.register(SiteUser)
admin.site.register(Song)
admin.site.register(Concert)


