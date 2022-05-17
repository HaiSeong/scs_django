
from django.shortcuts import render
from django.views import generic


# Create your views here.
def boss(reqest):

    context = {

    }

    return render(reqest, 'boss.html', context=context)

