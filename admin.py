from django.contrib import admin

from .models import Category,Actor,Films,Genre
admin.site.register(Category)

admin.site.register(Actor)

admin.site.register(Films)

admin.site.register(Genre)