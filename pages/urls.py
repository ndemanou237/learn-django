from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('contact/', views.contact_page_view, name="contact"),
    path('propos/', views.propos_page_view),
    path('message/', views.MessageListView.as_view(), name="messages"),
    
]