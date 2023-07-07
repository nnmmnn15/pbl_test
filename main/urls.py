from django.contrib import admin
from django.urls import path

from .views import index, result, ESJ, ESP, ENJ, ENP, ISJ, ISP, INJ, INP

app_name = 'main'

urlpatterns = [
    path('', index, name='index_2'),
    path('result/', result, name='result'),
    path('result/ESJ/', ESJ),
    path('result/ESP/', ESP),
    path('result/ENJ/', ENJ),
    path('result/ENP/', ENP),
    path('result/ISJ/', ISJ),
    path('result/ISP/', ISP),
    path('result/INJ/', INJ),
    path('result/INP/', INP),
]