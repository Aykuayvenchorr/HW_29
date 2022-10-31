from django.contrib import admin

# Register your models here.
from user.models import Location, User

admin.site.register(Location)
admin.site.register(User)
