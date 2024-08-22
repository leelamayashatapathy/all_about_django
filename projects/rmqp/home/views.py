from django.shortcuts import render
import random
from .rmq import publish_message

from faker import Faker
fake = Faker() 


def index(request):
    message = f"This is a dummy message- {random.randint(0,100)}"
    data = [{"name":fake.name(), "address":fake.address()} for i in range(0,10)]
    
    publish_message(data)
    return render(request,'index.html')
