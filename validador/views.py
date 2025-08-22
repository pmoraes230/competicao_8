from django.shortcuts import render, redirect
from django.contrib import messages
from home.views import get_user_profile
from home import models

# Create your views here.
def validador(request):
    context = get_user_profile(request)
    if request.method == "POST":
        input_ticket = request.POST.get("id_ticket").strip()
        try:
            ticket = models.Ticket.objects.get(id_ticket=input_ticket)
            if ticket.status == "validado":
                messages.info(request, "Ingresso já validado antes, valide outro.")
                return redirect("validador")
            elif ticket.status == "cancelado":
                messages.info(request, "Ingresso cancelado, valide um ingresso valido.")
                return redirect("validador")
            else:
                ticket.status = "validado"
                ticket.save()
                messages.success(request, "Ingresso validado com sucesso, bom show!")
                return redirect("validador")
        except models.Ticket.DoesNotExist:
            messages.error(request, "Ingresso não encontrado")
            return redirect("validador")
    return render(request, "validador.html", context)