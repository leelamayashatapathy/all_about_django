from django.urls import path
from .views import homepage,contact,service,dynamic,thank_you,search_page

urlpatterns = [
    path('home/',homepage, name='home'),
    path('contact/',contact, name='contact'),
    path('service/',service, name='service'),
    path('thank-you/',thank_you, name = 'thank-you'),
    path('search/',search_page, name = 'search-page'),
    
    
    #dynamic-url
    path('dynamicurl/<str:email>',dynamic,name='dynamic'),
]