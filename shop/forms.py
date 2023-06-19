from django import forms
from .models import Customer, Order, OrderItem, Good



class BuyForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    number = forms.IntegerField()
    Address = forms.CharField(max_length=500)
    def __init__(self, *args, **kwargs):
        super(BuyForm, self).__init__(*args, **kwargs)
        fn = self.initial.get('fn', '')  
        ln = self.initial.get('ln', '')  
        em = self.initial.get('em', '')  
        self.fields['first_name'].initial = fn  
        self.fields['last_name'].initial = ln  
        self.fields['email'].initial = em
    def save(self, input_names, input_quantities, inputtotal):
        data = self.cleaned_data
        try:
            customer = Customer.objects.get(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], number=data['number'])
        except Customer.DoesNotExist:
            customer = Customer.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], number=data['number'])

        order_instance = Order(Address=data['Address'], customer=customer, Total_Sum=round(float(inputtotal)))
        order_instance.save()

        for i in range(len(input_names)):
            goods_instance = Good.objects.get(Name=input_names[i])
            order_item_instance = OrderItem(order=order_instance, good=goods_instance, quantity=input_quantities[i])
            order_item_instance.save()