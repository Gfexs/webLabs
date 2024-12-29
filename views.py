from django.shortcuts import render
from django.views import View
from .models import Client  # Импорт модели Client

class Index(View):
    def get(self, request):
        # Извлекаем все данные
        clients = Client.objects.all()
        print(clients)  # Вывод в консоль для проверки
        return render(request, 'profileapp/index.html', {'clients': clients})


