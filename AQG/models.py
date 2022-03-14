from email.policy import default
from random import choices
from secrets import choice
from tkinter.tix import ButtonBox
from django.db import models
from django import forms
from django.utils.html import format_html

# Create your models here.
Subject_choice=(
    ('dbms','Dbms'),
    ('es','Embedded System'),
    ('os','operating System')
)

class FilesAdmin(models.Model):
    Subject = models.CharField(max_length=20,default="Dbms",choices=Subject_choice)
    Pdf_file=models.FileField()
    Pdf_Name=models.CharField(max_length=100)
    Scan_Link=models.URLField(max_length=10000,default="http://127.0.0.1:8000/ocr_signal")
    
    
    def __str__(self):
        return self.Pdf_Name


class Os(models.Model):
    qn = models.CharField(max_length = 1000000)
    mark = models.IntegerField(default=3)


class Dbms(models.Model):
    qn = models.CharField(max_length = 1000000)
    mark = models.IntegerField(default=3)
    

class Es(models.Model):
    qn = models.CharField(max_length = 1000000)
    mark = models.IntegerField(default=3)
