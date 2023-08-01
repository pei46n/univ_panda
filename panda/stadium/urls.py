from django.urls import path
from . import views


app_name = 'stadium'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('stadium_list/', views.IndexView.as_view(), name='list'),
    path('stadium_list/j1/', views.J1_View.as_view(), name='j1_list'),
    path('stadium_list/j2/', views.J2_View.as_view(), name='j2_list'),
    path('stadium_list/j3/', views.J3_View.as_view(), name='j3_list'),
    path('stadium/<int:pk>', views.DetailView.as_view(), name='details'),
    path('stadium/j1/<int:pk>', views.DetailView.as_view(), name='j1_details'),
    path('stadium/j2/<int:pk>', views.DetailView.as_view(), name='j2_details'),
    path('stadium/j3/<int:pk>', views.DetailView.as_view(), name='j3_details'),
]