from django.urls import path
# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import empleadoList, empleadoCreate, empleadoUpdate , empleadoDelete
urlpatterns = [
    path('listar_empleado/', empleadoList.as_view(), name="empleado_list"),
    path('crear_empleado/', empleadoCreate.as_view(), name="empleado_form"),
    path('editar_empleado/<int:pk>', empleadoUpdate.as_view(), name="empleado_update"),
    path('borrar_empleado/<int:pk>', empleadoDelete.as_view(), name="empleado_borrar"),
]
