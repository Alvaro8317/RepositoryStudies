from django.urls import path
from .views import list_view, CarListView

urlpatterns = [
    path("listar/", CarListView.as_view()),
    path("detalle/<int:identifier>", list_view),
    path("marcas/<str:brand>", list_view),
]
