from django.contrib import admin
from Storages.models import Gallery


class ImageAdmin(admin.ModelAdmin):
     list_display = ('title', 'raiting', 'image')
admin.site.register(Gallery, ImageAdmin)
# Register your models here.
