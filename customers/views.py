from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Interaction
from .forms import CustomerForm, InteractionForm

def dashboard(request):
    customers = Customer.objects.all()
    return render(request, 'customers/dashboard.html', {'customers': customers})

def add_customer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'customers/customer_form.html', {'form': form})

def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'customers/customer_form.html', {'form': form, 'edit': True})

def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('dashboard')

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    interactions = customer.interactions.all()
    form = InteractionForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        interaction = form.save(commit=False)
        interaction.customer = customer
        interaction.save()
        return redirect('customer_detail', pk=pk)
    return render(request, 'customers/customer_detail.html', {
        'customer': customer,
        'interactions': interactions,
        'form': form
    })


