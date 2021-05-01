from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='index'),
    path('fetch_data_hist/',views.fetch_data_hist,name = "fetch_data_hist"),
    path('fetch_data_loc/',views.fetch_data_loc,name = "fetch_data_loc"),
    path('fetch_data_key/',views.fetch_data_key,name = "fetch_data_key")

]
