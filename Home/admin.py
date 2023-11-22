from django.contrib import admin
from.models import typeb,tamas,bookinfo


# Register your models here.


class siteadmin(admin.ModelAdmin):
    readonly_fields=['id']
    
admin.site.register(typeb,siteadmin)
admin.site.register(tamas)
admin.site.register(bookinfo,siteadmin)
    
