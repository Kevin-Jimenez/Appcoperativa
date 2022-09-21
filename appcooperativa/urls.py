from django.urls import path
from .views import ClienteViews, UsuarioViews
from . import views

urlpatterns=[
    path('cliente/',ClienteViews.as_view(), name="Listar"),
    path('cliente/<int:doc>', ClienteViews.as_view(), name="Update"),

    path('usuarios/',UsuarioViews.as_view(), name="Listar"),
    path('usuarios/<int:doc>', UsuarioViews.as_view(), name="Update"),

    path('login/',views.loginUser, name="Login"),

    path('newuser/', views.formRegister, name="Formulario Nuevo Usuario")
    
]
