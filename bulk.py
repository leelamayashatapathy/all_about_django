import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learningproj.settings")
django.setup()

from Home.models import Person

from faker import Faker
fake = Faker()

def create_person(num):
    person_obj_lst =[Person(person_name = fake.name()) for _ in range (num) ]
    Person.objects.bulk_create(person_obj_lst)
# create_person(100)

def update_person(name):
    print(Person.objects.filter(person_name__icontains=name).count())
    print(Person.objects.filter(person_name__icontains=name).update(person_name =  "Leelamaya"))
    
    
# update_person('Donald')

def delete_person():
    Person.objects.all().delete()
delete_person()
    
        
        