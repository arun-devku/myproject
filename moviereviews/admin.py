from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)




admin.site.register(Movies2)

admin.site.register(Register)

# Register your models here.
