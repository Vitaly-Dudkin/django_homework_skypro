from django.urls import path


from . import views
from .apps import CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home_page'),
    path('catalog/', views.CatalogListView.as_view(), name='catalog'),

]