from django.contrib import admin
from homepage.views import homepagede, showpost
from django.urls import path

urlpatterns = [
    path('', homepagede), 
    path('post/<slug:slug>/', showpost), # <slug:slug>此部分是將slug當作第二個參數(第一個參數預設為request)輸入進showpost函式
    path('admin/', admin.site.urls),
]