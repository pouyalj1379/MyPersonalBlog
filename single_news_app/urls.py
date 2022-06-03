from django.urls import path
from single_news_app import views

urlpatterns = [
    path("single-new/<int:id>", views.new)
]
