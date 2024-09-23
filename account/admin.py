from django.contrib import admin

from .models import Note, UserAccount

# Register account models
admin.site.register(UserAccount)
admin.site.register(Note)