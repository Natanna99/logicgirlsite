from django.contrib import admin
from django.urls import path, include
from .views import home, downloads, sugestao, equipe, sobre, baixar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name="home"),
    path('downloads',downloads,name="downloads"),
    path('equipe',equipe,name="equipe"),
    path('baixar/<int:id>',baixar,name="baixar"),
    path('sobre',sobre,name="sobre"),
    path('sugestao',sugestao,name="sugestao"),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
