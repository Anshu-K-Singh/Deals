from django.shortcuts import render
#import the database
from item.models import Category, Item

# Create your views here.

def index(request):
    #showing new products in data \base
    items = Item.objects.filter(is_sold = False) [0:10]
    Categories = Category.objects.all()
    #to be able to use them in template go in the return render
    return render(request, 'core\index.html', {'categories':Categories, 'items':items})#adding category and item context here 

def contact(request):
    return render(request, 'core\contact.html')