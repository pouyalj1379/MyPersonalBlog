from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("single-story/<int:id>", views.story),
    path("single-template/<int:id>", views.template)
]