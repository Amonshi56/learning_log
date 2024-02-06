from django.shortcuts import render

def index(request):
    '''Домашняя страница приложения Learning log'''
    return render(request, 'learning_logs/index.html')
