from django.urls import path
from . import views

urlpatterns = [
    path("validation/", views.validation_ticket, name="validador")
]
