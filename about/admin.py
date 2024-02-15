from django.contrib import admin
from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_on')
    search_fields = ('title', 'content')

# Register your models here.
admin.site.register(About, AboutAdmin)