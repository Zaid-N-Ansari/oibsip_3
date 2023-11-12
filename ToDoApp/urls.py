from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<slug:itmt>', views.delete , name='delete'),
]
