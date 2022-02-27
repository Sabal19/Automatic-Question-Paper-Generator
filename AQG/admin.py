from django.contrib import admin
from .models import Question,FilesAdmin,Osquestion
# Register your models here.
admin.site.register(FilesAdmin)
@admin.register(Question)

@admin.register(Osquestion)

class OsquestionAdmin(admin.ModelAdmin):
    list_display = ('id','qn','mark')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','qn','mark')