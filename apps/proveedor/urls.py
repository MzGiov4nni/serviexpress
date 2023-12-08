from django.urls import path
# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import proveedorList, proveedorCreate, proveedorUpdate , proveedorDelete
urlpatterns = [
    path('listar_proveedor/', proveedorList.as_view(), name="proveedor_list"),
    path('crear_proveedor/', proveedorCreate.as_view(), name="proveedor_form"),
    path('editar_proveedor/<int:pk>', proveedorUpdate.as_view(), name="proveedor_update"),
    path('borrar_proveedor/<int:pk>', proveedorDelete.as_view(), name="proveedor_borrar"),
]
