from django.urls import path
from .views import dashboard, produtos, exportar_csv

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("produtos/", produtos, name="produtos"),
    path("relatorios/csv/", exportar_csv, name="exportar_csv"),
]
