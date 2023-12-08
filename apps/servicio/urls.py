from django.urls import path
# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import servicioList, servicioCreate, servicioUpdate , servicioDelete
from . import views
urlpatterns = [
    path('listar_servicio/', servicioList.as_view(), name="servicio_list"),
    path('crear_servicio/', servicioCreate.as_view(), name="servicio_form"),
    path('editar_servicio/<int:pk>', servicioUpdate.as_view(), name="servicio_update"),
    path('borrar_servicio/<int:pk>', servicioDelete.as_view(), name="servicio_borrar"),
    path('serviciocliente_vista/', views.servicios_disponibles, name='servicios_disponibles'),
]
