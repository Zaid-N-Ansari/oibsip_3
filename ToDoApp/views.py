from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoItem
from django.contrib import messages

def index(req):
    if req.method == 'POST':
        title = req.POST.get('title')
        desc = req.POST.get('desc')
        if title == '' or desc == '':
            messages.info(req, 'Both are Required Fields')
            return redirect('/')
        else:
            if ToDoItem.objects.filter(ToDoItemTitle=title).exists():
                messages.info(req, 'Item Name Used')
                return redirect('/')
            else:
                ToDoItem.objects.create(ToDoItemTitle=title, ToDoItemDesc=desc)
                return redirect('/')
    else:
        data = ToDoItem.objects.all()
        res = { 'items': data }
        return render(req, 'index.html', res)

def delete(req, itmt):
    if req.method == "POST":
        item = get_object_or_404(ToDoItem, pk=itmt)
        item.delete()
    return redirect('/')