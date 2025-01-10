from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('camioneros', views.camioneros, name='camioneros'),
    path('camioneros/crear', views.crear, name='crear'),
    path('camioneros/editar/<str:cedula>/', views.editar, name='editar'),
    path('camioneros/borrar/<str:cedula>/', views.borrar, name='borrar'),
    path('camiones', views.camiones, name='camiones'),
    path('camiones/crear_camion', views.crear_camion, name='crear_camion'),
    path('camiones/editar_camion/<str:placa>/', views.editar_camion, name='editar_camion'),
    path('camiones/borrar_camion/<str:placa>/', views.borrar_camion, name='borrar_camion'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
