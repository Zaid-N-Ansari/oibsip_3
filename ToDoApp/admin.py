from django.contrib import admin
from .models import ToDoItem

admin.site.register(ToDoItem)

class AdminToDoItem(admin.ModelAdmin):
    list_display = ('ToDoItem_title', 'ToDoItem_desc')
