import django.db
from django.shortcuts import redirect, render
from shop.forms import BuyForm
from shop.models import Good, Customer
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login



def Shop_list_view(request):
    if request.method == 'POST':
        input_names = request.POST.getlist('input_name')
        input_quantities = request.POST.getlist('input_quantity')
        inputtotal = request.POST.get('inputtotal')
        request.session['input_names'] = input_names
        request.session['input_quantities'] = input_quantities
        request.session['inputtotal'] = inputtotal
        return redirect('order')

    goods = Good.objects.all()
    return render(request, 'shoplist.html', {'goods': goods})

def Order_view(request):
    input_names = request.session.get('input_names', [])  # Отримати кешовані дані з сесії
    input_quantities = request.session.get('input_quantities', [])
    inputtotal = request.session.get('inputtotal')
    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            form.save(input_names, input_quantities, inputtotal)
            return redirect('home')
    else:
        initial_data = {
            'input_name': input_names,
            'input_quantities': input_quantities,
            'inputtotal': inputtotal,
        }
        if request.user.is_authenticated:
            user = request.user
            initial_data2 = {
                'fn': user.first_name,
                'ln': user.last_name,
                'em': user.email,
            }
            initial_data.update(initial_data2)
        form = BuyForm(initial=initial_data) 

    return render(request, 'order.html', {'form': form, 'input_names': input_names, 'input_quantities': input_quantities, 'inputtotal': inputtotal})


