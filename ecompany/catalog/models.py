from django.db import models
class Item(models.model):
   title = models.CharField(max_length= 200)
   price = models.IntegerField()
   Discount_price = models.IntegerField()
   slug = models.SlugField()

   def __str_(self):
        return self.user.title
   


class OrderItem(models.model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    Ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

     def __str_(self):
        return f"{self.quantity} of {self.item.title}"
    


    


class order(models.Model):
    user =  models.foreignkey(user, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    Ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add= True)
    ordered_date = models.DateTimeField()


    def __str_(self):
        return self.user.username
    