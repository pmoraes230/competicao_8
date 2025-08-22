from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("home/", views.home, name="home"),
    
    # Event
    path("deteils_event/<int:id_event>/", views.deteils_event, name="deteils_event"),
    path("buy_ticket/<int:id_event>/", views.buy_ticket, name="buy_ticket"),
    path("list_tickets/<int:id_event>/", views.list_tickets, name="list_ticket"),
    path("ticket_export/<str:id_ticket>/", views.export_ticket, name="ticket_export")
]
