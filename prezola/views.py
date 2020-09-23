from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Items, Orders
from .forms import ItemForm, OrderForm

def index(request):
    gift_list = Items.objects.order_by('-id')

    return render(request, 'prezola/items.html', { 'gift_list' : gift_list })


def report(request):
    sold_items = Orders.objects.select_related('item_id')
    unsold_items = Items.objects.filter(in_stock_quantity__gt = 0)

    return render(request, 'prezola/report.html', { 'sold_items' : sold_items, 'unsold_items' : unsold_items })


def order(request, gift_id):
    item = get_object_or_404(Items, pk=gift_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            item.in_stock_quantity = item.in_stock_quantity - 1
            item.save()
            return HttpResponseRedirect("/")
    else:
        form = OrderForm()

    return render(request, 'prezola/order.html', {'form' : form, 'gift_id' : gift_id})


def add(request):

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ItemForm()

    return render(request, 'prezola/new_item.html', {'form' : form})


def delete(request, gift_id):
    item = get_object_or_404(Items, pk=gift_id)

    item.delete()

    return HttpResponseRedirect("/")
