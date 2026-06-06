from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactMessage
from .forms import ContactForm
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        
        return context
    
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"    

# def home_page_view(request):
#     context = {
#         'nom':'shadow',
#         'age':19,
#         'couleurs': ['noir','rouge','orange'],
#         'est_connecte': True
#     }
#     return render(request,'home.html',context)


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

class MessageListView(ListView):
    model = ContactMessage
    template_name = "message_list.html"
    context_object_name = 'message_list'

    def get_queryset(self):
        return ContactMessage.objects.filter(is_treated=False)

# def message_list_view(request):
#     messages = ContactMessage.objects.all()
#     context = {
#         'message_list': messages
#     }

#     return render(request, 'message_list.html',context)

