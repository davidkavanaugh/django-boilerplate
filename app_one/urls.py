from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('route-one', views.route_one),
    path('route-two/<str:name>', views.route_two),
    path('route-three', views.route_three),
]
