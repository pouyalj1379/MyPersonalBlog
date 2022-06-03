from django.urls import path
from . import views


urlpatterns = [
    path("single-story/<int:id>", views.story)
]