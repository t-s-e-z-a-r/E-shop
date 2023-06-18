from django.db import models

class Good(models.Model):
    Name = models.CharField(max_length=255)
    Price = models.PositiveIntegerField()
    Image = models.ImageField()

    def __str__(self):
        return self.Name

class Customer(models.Model):
    first_name = models.CharField(max_length=255, default=0)
    last_name = models.CharField(max_length=255, default=0)
    email = models.EmailField(unique=True)
    number = models.IntegerField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Order(models.Model):
    Address = models.CharField(max_length=500)
    Total_Sum = models.PositiveIntegerField(default=0)
    goods = models.ManyToManyField(Good, through='OrderItem')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Order #{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order #{self.order.id}, Good: {self.good.Name}, Quantity: {self.quantity}"
