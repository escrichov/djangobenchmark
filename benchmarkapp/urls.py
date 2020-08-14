from django.urls import path
from . import views


urlpatterns = [
    path('json/', views.view_json),
    path('render/', views.view_render),
    path('model/', views.view_model),
]
