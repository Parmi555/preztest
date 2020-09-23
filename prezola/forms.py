from django.forms import ModelForm
from .models import Items, Orders

class ItemForm(ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'brand', 'price', 'in_stock_quantity']

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['item_id', 'buyer_name', 'address', 'quantity']
