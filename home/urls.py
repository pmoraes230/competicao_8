from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("home/", views.home, name="home"),
    path("deteils_event/<int:id_event>/", views.deteils_event, name="deteils_event"),
    path("buy_ticket/<int:id_event>/", views.buy_ticket, name="buy_ticket"),
    path("list_ticket_generate/", views.list_ticket_generate, name="ticket_list"),
    path("generate_ticket/<str:id_ticket>/", views.export_ticket, name="export_ticket")
]