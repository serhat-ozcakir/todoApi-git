from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=50)
    description = models.TextField(blank=True, null = True)
    
    TITLE = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    )
    
    priority = models.CharField(max_length=50, choices=TITLE, default='L')
    
    done = models.BooleanField(default=False)
    
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task