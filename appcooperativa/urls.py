from django.urls import path
from .views import ClienteViews, UsuarioViews
from . import views

urlpatterns=[
    path('cliente/',ClienteViews.as_view(), name="Listar"),
    path('cliente/<int:doc>', ClienteViews.as_view(), name="Update"),

    path('usuarios/',UsuarioViews.as_view(), name="Listar"),
    path('usuarios/<int:doc>', UsuarioViews.as_view(), name="Update"),

    path('login/',views.loginUser, name="Login"),

    path('newuser/', views.formRegister, name="Formulario Nuevo Usuario"),

    path('actualizar/<int:doc>', views.formUpdate , name="Formulario Actualizar Usuario"),

    path('actualizarc/', views.updateCliente  ,name="Actualiza el cliente"),

    path('eliminar/<int:doc>', views.deleteCliente , name="Eliminar Usuario"),

    path('consultajoin/<int:doc>', views.exampleJoin, name="Ejemplo JOin")
    
]
