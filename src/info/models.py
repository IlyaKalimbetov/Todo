from django.db import models
from datetime import date

class InfoTodo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Дела')
    date_of_end = models.DateTimeField()
    create = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    content = models.TextField()

    class Meta:
        verbose_name = 'Список дел'
        verbose_name_plural = 'Список дел'
