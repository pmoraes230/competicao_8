from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import logout
from django.db.models import Q
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import models
import uuid
import pdfkit

# Create your views here.
def get_user_profile(request):
    user_id = request.session.get("user_id")
    if user_id:
        try:
            user = models.User.objects.select_related("profile").get(id=user_id)
            return {
                'user_id': user.id,
                'user_name': user.name,
                'user_role': user.profile.name,
                'is_authenticated': True
            }
        except models.User.DoesNotExist:
            return {"user_name": "", "is_authenticated": False}
    return {"user_name": "", "is_authenticated": False}

def login(request):
    if request.method == "GET":
        return render(request, "login/login.html")
    
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")
    
        if not all([login, password]):
            messages.error(request, "Insira seu login e seu senha antes de enviar.")
            return redirect("login")
        
        if models.User.objects.filter(email=login).first() or models.User.objects.filter(cpf=login).first():
            user = models.User.objects.filter(email=login).first() or models.User.objects.filter(cpf=login).first()
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                request.session['user_role'] = user.profile.name
                
                if user.profile.name == "Totem":
                    return redirect("validador")
                return redirect("home")
            else:
                messages.error(request, "Senha incorreta")
                return redirect("login")
        else:
            messages.error(request, "Usuário não encontrado")
            return redirect("login")
            
def logout_view(request):
    logout(request)
    messages.success(request, "Você saiu do sistema")
    return redirect("login")
                
def home(request):
    context = get_user_profile(request)
    context['events'] = models.Event.objects.all()
    return render(request, "home/home.html", context)

def deteils_event(request, id_event):
    context = get_user_profile(request)
    
    event = models.Event.objects.get(id=id_event)
    sector = models.Sector.objects.filter(event=event)
    client = None
    search_client = None
    
    if request.method == "POST" and 'search_clients' in request.POST:
        input_name = request.POST.get("name_client")
        if input_name:
            search_client = models.Client.objects.filter(
                Q(name__icontains=input_name)
            )[:10]
            if not search_client:
                messages.error(request, f"Nome {input_name} não encontrado no sistema")
                return redirect("deteils_event", id_event=id_event)
            else:
                messages.success(request, f"{search_client.count()} nomes encontrado")
        else:
            messages.error(request, "Digite um nome antes de enviar")
            return redirect("deteils_event", id_event=id_event)
    
    if request.method == 'POST' and 'client_selected' in request.POST:
        client_id = request.POST.get("client_id")
        request.session['client_id'] = client_id
        try:
            client = models.Client.objects.get(id=client_id)
            messages.success(request, f"{client.name} selecionado para venda de ingresso.")
        except models.Client.DoesNotExist:
            messages.error(request, "Cliente não encontrado")
            
    context.update({
        'event': event,
        'search_client': search_client,
        'client': client,
        'sectors': sector
    })
    return render(request, "event/deteils_event.html", context)

def buy_ticket(request, id_event):
    context = get_user_profile(request)
    
    event = models.Event.objects.get(id=id_event)
    sector = models.Sector.objects.filter(event=event)
    client = None
    search_client = None
    
    if request.method == "POST" and "buy_ticket" in request.POST:
        client_id = request.session.get("client_id")
        if not client_id:
            messages.error(request, "Escolha um cliente antes de continuar")
            return redirect("buy_ticket", id_event=id_event)
        try:
            client = models.Client.objects.get(id=client_id)
        except models.Client.DoesNotExist:
            messages.error(request, "Cliente não encontrado")
            return redirect("buy_ticket", id_event=id_event)
        
        sector_id = request.POST.get("sector_event")
        amount_ticket = int(request.POST.get("ticket_event", 0))
        
        if not all([sector_id, amount_ticket]):
            messages.error(request, "Informe o setor e a quantidade de ingresso antes de enviar.")
            return redirect("buy_ticket", id_event=id_event)
        
        try:
            sector_event = models.Sector.objects.get(id=sector_id)
        except models.Sector.DoesNotExist:
            messages.error(request, "Setor não existente no sistema")
            return redirect("buy_ticket", id_event=id_event)
        
        if amount_ticket == 0:
            messages.info(request, "A quantidade mínima para venda de ingresso é uma unidade")
            return redirect("buy_ticket", id_event=id_event)
        elif amount_ticket > 10:
            messages.info(request, "A quantidade máxima de ingresso por cliente é 10 unidades")
            return redirect("buy_ticket", id_event=id_event)
        else:
            tickets = []
            for _ in range(amount_ticket):
                ticket = models.Ticket.objects.create(
                    client=client,
                    event=event,
                    sector=sector_event,
                    id_ticket=str(uuid.uuid4()),
                    date_issue=timezone.now(),
                    status='emitido'
                )
                tickets.append(ticket)
            
            messages.success(request, f"{amount_ticket} ingresso(s) gerado(s).")
            del request.session['client_id']
            # Redireciona com a lista de ticket_ids como query string
            ticket_ids = [ticket.id_ticket for ticket in tickets]
            url = reverse("ticket_list") + "?" + "&".join([f"ticket_ids={ticket_id}" for ticket_id in ticket_ids])
            return HttpResponseRedirect(url)
    
    context.update({
        'event': event,
        'search_client': search_client,
        'client': client,
        'sectors': sector
    })
    return render(request, "event/details_event.html", context)

def list_ticket_generate(request):
    ticket_ids = request.GET.getlist("ticket_ids")
    ticket = models.Ticket.objects.filter(id_ticket__in=ticket_ids)
    context = {
        'tickets': ticket,
        **get_user_profile(request)
    }
    return render(request, "event/list_ticket_generate.html", context)

def list_ticket(request, id_event):
    context = get_user_profile(request)
    ticket = models.Ticket.objects.filter(event=id_event)
    event = models.Event.objects.get(id=id_event)
    context["event"] = event
    context['tickets'] = ticket
    return render(request, "event/list_ticket.html", context)

def export_ticket(request, id_ticket):
    ticket = get_object_or_404(models.Ticket, id_ticket=id_ticket)
    page_html = render_to_string("event/ticket_pdf.html", {'ticket': ticket})
    configuration = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    
    options = {
        'page-size': 'A5',
        'page-width': "80mm",
        'page-height': "140mm",
        'encoding': "UTF-8",
    }
    
    pdf = pdfkit.from_string(page_html, False, configuration=configuration, options=options)
    
    try:
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f"attachment; filename=ingresso_show_{ticket.event.event_name}_cliente_{ticket.client.name}.pdf"
        response.write(pdf)
    
        return response
    except Exception as ex:
        return HttpResponse(f"Erro ao gerar ingresso: {str(ex)}")
    
def list_users(request):
    context = get_user_profile(request)
    context['users'] = models.User.objects.all()
    return render(request, "users/list_users.html", context)

def register_users(request):
    context = get_user_profile(request)
    context['profiles'] = models.Profile.objects.all()
    
    if request.method == "POST":
        name_user = request.POST.get("name_user")
        email_user = request.POST.get("email_user")
        cpf_user = request.POST.get("cpf_user").replace(".", "").replace("-", "")
        perfil_user = request.POST.get("perfil_user")
        password_user = request.POST.get("password_user")
        Confirmation_password = request.POST.get("Confirmation_password")
        
        if not all([name_user, email_user, cpf_user, perfil_user, password_user, Confirmation_password]):
            messages.info(request, "Todos os campos são de preenchimento obrigatórios antes de enviar o cadastro.")
            return redirect("register_user")
        
        if models.User.objects.filter(cpf=cpf_user).exists():
            messages.info(request, "CPF informado já cadastro no sistema.")
            return redirect("register_user")
        
        if models.User.objects.filter(email=email_user).exists():
            messages.info(request, "Email informado já cadastro no sistema.")
            return redirect("register_user")
        
        if password_user != Confirmation_password:
            messages.info(request, "Senha não coincide com a senha colocada em campo de confirmação")
            return redirect("register_user")
        
        try: 
            profile = models.Profile.objects.get(id=perfil_user)
        except models.Profile.DoesNotExist:
            messages.error(request, "Perfil não existente no sistema.")
            return redirect("register_user")
        
        try:
            hashers = make_password(Confirmation_password)
            new_user = models.User.objects.create(
                name=name_user,
                email=email_user,
                cpf=cpf_user,
                password=hashers,
                profile=profile
            )
            new_user.full_clean()
            new_user.save()
            
            messages.success(request, f"Usuário {new_user.name} cadastrado com sucesso.")
            return redirect("list_users")
        except ValueError as ve:
            messages.error(request, f"Erro ao cadastrar novo usuário: {str(ve)}")
            
    return render(request, "users/create_user.html", context)

def update_user(request, id_user):
    context = get_user_profile(request)
    try:
        user = models.User.objects.get(id=id_user)
    except models.User.DoesNotExist:
        messages.error(request, "Usuário não encontrado no sistema.")
        return redirect("update_user")
    
    if request.method == "POST":
        name_user = request.POST.get("name_user")
        email_user = request.POST.get("email_user")
        cpf_user = request.POST.get("cpf_user").replace(".", "").replace("-", "")
        perfil_user = request.POST.get("perfil_user")
        
        if not all([name_user, email_user, cpf_user, perfil_user]):
            messages.info(request, "Todos os campos são de preenchimento obrigatórios antes de enviar o cadastro.")
            return redirect("update_user", id_user=id_user)
        
        if models.User.objects.filter(cpf=cpf_user).exclude(id=id_user).exists():
            messages.info(request, "CPF informado já cadastro no sistema.")
            return redirect("update_user", id_user=id_user)
        
        if models.User.objects.filter(email=email_user).exclude(id=id_user).exists():
            messages.info(request, "Email informado já cadastro no sistema.")
            return redirect("update_user", id_user=id_user)
        
        try: 
            profile = models.Profile.objects.get(id=perfil_user)
        except models.Profile.DoesNotExist:
            messages.error(request, "Perfil não existente no sistema.")
            return redirect("update_user", id_user=id_user)
        
        try:
            user.name = name_user
            user.email = email_user
            user.cpf = cpf_user
            user.profile = profile
            
            user.full_clean()
            user.save()
            
            messages.success(request, f"Cadastro do usuário {user.name} atualizado com sucesso.")
            return redirect("list_users")
        except ValueError as ve:
            messages.error(request, f"Erro ao atualizar o cadastro do usuário: {str(ve)}")
    
    context.update({
        'user': user,
        'profiles': models.Profile.objects.all() 
    })
    return render(request, "users/update_user.html", context)

def delete_user(request, id_user):
    try:
        user = models.User.objects.get(id=id_user)
        if request.method == "POST":
            user.delete()
            messages.success(request, "Usuário apagado do sistema com sucesso.")
            return redirect("list_users")
        context = {
            'user': user,
            **get_user_profile(request)
        }
        return render(request, "users/delete_user.html", context)
    except models.User.DoesNotExist:
        messages.error(request, "Usuário não encontrado.")
        return redirect("list_users")