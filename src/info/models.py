from django.db import models

class InfoTodo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Дела')
    date_of_end = models.DateTimeField()
    complete = models.BooleanField(default=False)
    content = models.TextField()

