from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Item

def index(request):
    items_list = Item.objects.order_by('-name')
    context = {'items_list': items_list}
    return render(request, 'products/index.html', context)

def detail(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'products/detail.html', {'item': item})