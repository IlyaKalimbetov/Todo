from django.contrib import admin
from .models import *

class InfoTodoAdmin(admin.ModelAdmin):
    pass


admin.site.register(InfoTodo, InfoTodoAdmin)