from django.db import models
from django.forms import ModelForm

class Items(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    in_stock_quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'items'

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(Items, db_column='item_id', on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    quantity = models.PositiveSmallIntegerField()
    order_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.buyer_name

    class Meta:
        managed = True
        db_table = 'orders'
