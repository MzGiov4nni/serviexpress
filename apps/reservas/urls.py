from django.urls import path
# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('hacer_reserva/', views.hacer_reserva, name='hacer_reserva'),
]