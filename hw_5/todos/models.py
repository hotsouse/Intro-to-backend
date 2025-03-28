from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    STATUS_CHOICES = [
        (True, 'Completed'),
        (False, 'Not Completed')
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)  # Описание может быть пустым
    due_date = models.DateField(null=True, blank=True)  # Дата может быть пустой
    status = models.BooleanField(choices=STATUS_CHOICES, default=False)  # По умолчанию "Not Completed"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
