from django.db import models

# Create your models here.
class Question(models.Model):
    qn = models.CharField(max_length = 1000000)
    mark = models.IntegerField(default=3)


class Osquestion(models.Model):
    qn = models.CharField(max_length = 1000000)
    mark = models.IntegerField(default=3)
    

class FilesAdmin(models.Model):
    adminupload =models.FileField(upload_to='media')
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
