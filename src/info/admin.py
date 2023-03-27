from django.contrib import admin
from .models import *

class InfoTodoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "create", 'content', 'complete', 'date_of_end')


admin.site.register(InfoTodo, InfoTodoAdmin)