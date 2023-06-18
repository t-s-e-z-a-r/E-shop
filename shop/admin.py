from django.contrib import admin
from .models import Good, Customer, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    
class OrderInline(admin.StackedInline):
    model = Order

class CustomerAdmin(admin.ModelAdmin):
    inlines = [OrderInline]

admin.site.register(Good)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)