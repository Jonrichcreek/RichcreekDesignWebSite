from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name='portfolio'),
    path('<int:portfolio_id>', views.gallery_single, name='gallery_single'),
    path('search', views.search, name='search'),
]
