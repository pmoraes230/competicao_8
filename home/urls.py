from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("home/", views.home, name="home"),
    
    # Event
    path("deteils_event/<int:id_event>/", views.deteils_event, name="deteils_event"),
    path("buy_ticket/<int:id_event>/", views.buy_ticket, name="buy_ticket"),
    path("list_ticket_generate/", views.list_ticket_generate, name="ticket_list"),
    path("generate_ticket/<str:id_ticket>/", views.export_ticket, name="export_ticket"),
    path("list_tickets/<int:id_event>/", views.list_ticket, name="list_ticket"),
    
    # Users
    path("list_users/", views.list_users, name="list_users"),
    path("register_user/", views.register_users, name="register_user"),
    path("update_user/<int:id_user>/", views.update_user, name="update_user"),
    path("delete_user/<int:id_user>/", views.delete_user, name="delete_user"),
]