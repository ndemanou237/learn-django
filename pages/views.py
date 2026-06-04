from django.shortcuts import render
from django.http import HttpResponse

def home_page_view(request):
    context = {
        'nom':'shadow',
        'age':19,
        'couleurs': ['noir','rouge','orange'],
        'est_connecte': True
    }
    return render(request,'home.html',context)


def contact_page_view(request):
    return render(request, 'contact.html')

def propos_page_view(request):
    return render(request,'propos.html')

