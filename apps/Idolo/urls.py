from django.urls import path
# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import IdoloList, IdoloCreate, IdoloUpdate , IdoloDelete, consulta_cocktail_view, buscar_cocktail_view, contacto_view
urlpatterns = [
    path('listar_idolo/', IdoloList.as_view(), name="idolo_list"),
    path('crear_idolo/', IdoloCreate.as_view(), name="idolo_form"),
    path('editar_idolo/<int:pk>', IdoloUpdate.as_view(), name="idolo_update"),
    path('borrar_idolo/<int:pk>', IdoloDelete.as_view(), name="idolo_borrar"),
    path('consulta-cocktail/', consulta_cocktail_view, name='consulta_cocktail'),
    path('buscar-cocktail/', buscar_cocktail_view, name='buscar_cocktail'),
    path('contacto/', contacto_view, name='contacto'),
]


