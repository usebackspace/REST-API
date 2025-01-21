from django.contrib import admin
from . models import Marvel
# Register your models here.

@admin.register(Marvel)
class MarvelAdmin(admin.ModelAdmin):
    list_display=['id','f_name','heroic_name']