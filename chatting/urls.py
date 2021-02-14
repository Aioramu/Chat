from django.urls import path,include

from . import views
app_name='chatting'
urlpatterns = [
    path('', views.index, name='index'),
    path('search',views.search,name='sea'),
    path('<str:room_name>/', views.room, name='room'),
]
