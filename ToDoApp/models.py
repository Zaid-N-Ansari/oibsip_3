from django.db import models

class ToDoItem(models.Model):
    ToDoItemTitle = models.CharField(max_length=30, primary_key=True)
    ToDoItemDesc = models.TextField(blank=False)