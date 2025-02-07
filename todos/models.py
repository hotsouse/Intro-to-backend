from django.db import models

class Todo(models.Model):
    STATUS_CHOICES = [
        (True, 'Completed'),
        (False, 'Not Completed')
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)  # Описание может быть пустым
    due_date = models.DateField(null=True, blank=True)  # Дата может быть пустой
    status = models.BooleanField(choices=STATUS_CHOICES, default=False)  # По умолчанию "Not Completed"

    def __str__(self):
        return self.title

# Create your models here.
