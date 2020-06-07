from django.shortcuts import render
from .models import DetectionCase
from django.views import generic
# Create your views here.

class Index(generic.ListView):
    model = DetectionCase
    context_object_name = 'threat_list'   # ваше собственное имя переменной контекста в шаблоне
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'index.html'  # Определение имени вашего шаблона и его расположения
