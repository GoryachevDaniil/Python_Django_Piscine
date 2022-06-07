from django.contrib import admin
from django.urls import path
from . import views

handler404 = "moviemon.views.error404"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.titlescreen, name="titlescreen"),
    path('worldmap/', views.worldmap, name='worldmap'),
    path('battle/<str:moviemon_id>', views.battle, name='battle'),
    path('moviedex/', views.moviedex, name='moviedex'),
    path('moviedex/detail/<str:moviemon_id>', views.detail, name='detail'),
    path('options/', views.option, name='option'),
    path('options/save_game/', views.save, name='save'),
    path('options/load_game/', views.load, name='load'),
]
