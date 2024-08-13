from django.urls import path

from .views import index,deleteTransaction,registration_user,login_user,logout_user

urlpatterns = [
    path('registration/',registration_user,name='user-registration'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('',index,name='index' ),
    
    path('delete-transaction/<uuid>/',deleteTransaction,name='deleteTransaction' ),
    
]