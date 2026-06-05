from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactMessage
from .forms import ContactForm

def home_page_view(request):
    context = {
        'nom':'shadow',
        'age':19,
        'couleurs': ['noir','rouge','orange'],
        'est_connecte': True
    }
    return render(request,'home.html',context)


def contact_page_view(request):
    success_msg = None
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success_msg = "votre message a été bien envoyé !"
            form = ContactForm()
    else:
        form = ContactForm()
    context = {
        'form':form,
        'success_msg':success_msg
    }    
    return render(request, 'contact.html',context)

def propos_page_view(request):
    return render(request,'propos.html')

def message_list_view(request):
    messages = ContactMessage.objects.all()
    context = {
        'message_list': messages
    }

    return render(request, 'message_list.html',context)

