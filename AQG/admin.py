from django.contrib import admin
from .models import Os,FilesAdmin,Dbms,Es
# Register your models here.
admin.site.register(FilesAdmin)


@admin.register(Os)

@admin.register(Dbms)

@admin.register(Es)


class OsAdmin(admin.ModelAdmin):
    list_display = ('id','qn','mark')

class DbmsAdmin(admin.ModelAdmin):
    list_display = ('id','qn','mark')

class EsAdmin(admin.ModelAdmin):
    list_display = ('id','qn','mark')


