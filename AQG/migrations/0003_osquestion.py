# Generated by Django 4.0.2 on 2022-02-25 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AQG', '0002_filesadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Osquestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qn', models.CharField(max_length=1000000)),
                ('mark', models.IntegerField(default=3)),
            ],
        ),
    ]