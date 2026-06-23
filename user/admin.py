from django.contrib import admin
from user.models import UserProfile, contactMessage

admin.site.register(contactMessage)
admin.site.register(UserProfile)

# Register your models here.
