from django.urls import path


from . import views
from .apps import CatalogConfig

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home_page'),
    # path('catalog/', views.career_plan, name='catalog'),

]