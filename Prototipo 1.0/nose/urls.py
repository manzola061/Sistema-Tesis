from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('camioneros', views.camioneros, name='camioneros'),
    path('camioneros/crear', views.crear, name='crear'),
    path('camioneros/editar/<str:cedula>/', views.editar, name='editar'),
    path('camioneros/borrar/<str:cedula>/', views.borrar, name='borrar'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]