from django.contrib import admin

from .models import InfoTodo


class InfoTodoAdmin(admin.ModelAdmin):
    list_display = (
        "__str__", "created", 'content', 'complete', 'date_of_end'
    )


admin.site.register(InfoTodo, InfoTodoAdmin)
