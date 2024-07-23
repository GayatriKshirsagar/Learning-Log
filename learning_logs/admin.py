from django.contrib import admin

# To register Topic with the admin site
# The dot before models tells Django to look for models.py in same dir as admin.py
from .models import Topic, Entry
# To manage our model through the admin site
admin.site.register(Topic)
admin.site.register(Entry)
# Register your models here.
