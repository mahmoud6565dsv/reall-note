from django.contrib import admin

# Register your models here.
from .models import Note ,Comment

admin.site.register(Note)
admin.site.register(Comment)