# Generated by Django 4.1.4 on 2022-12-08 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
