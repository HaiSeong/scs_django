
from django.shortcuts import render
from django.views import generic
from .models import Category, Store


# Create your views here.
def index(reqest):

    store = Store.objects.order_by("name")[:8]

    context = {
        "store": store
    }

    return render(reqest, 'index.html', context=context)


class StoreDetailView(generic.DetailView):
    model = Store
