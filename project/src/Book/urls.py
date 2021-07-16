from django.urls import path
from. import views

urlpatterns = [
    path('', views.All_Books, name='Books'),
    path('<int:Book_id>/', views.One_Book, name='Book'),

]