from django.shortcuts import render, redirect
from .forms import ClientForm
from .models import Client



def candidate_application_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ClientForm()

    return render(request, 'application_form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def application_form_list_view(request):
    all_forms = Client.objects.all()
    return render(request, 'application_form_list.html', {'forms': all_forms})


def all_clients_view(request):
    # Query all client records
    clients = Client.objects.all()
    
    return render(request, 'all_clients.html', {'clients': clients})


def add_client(request):
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client_form.save()
            return redirect('client_list')
    else:
        client_form = ClientForm()

    return render(request, 'add_client.html', {'client_form': client_form})





def add_client_view(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()  # Save the client with its associated type
            return redirect('all_clients')  # Redirect to the list of all clients
    else:
        form = ClientForm()

    return render(request, 'add_client.html', {'form': form})
