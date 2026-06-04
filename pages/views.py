from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactMessage

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

def message_list_view(request):
    messages = ContactMessage.objects.all()
    context = {
        'message_list': messages
    }

    return render(request, 'message_list.html',context)

