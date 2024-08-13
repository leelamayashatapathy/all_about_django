import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learningproj.settings")
django.setup()

from Home.models import Book, Author,Brand,Product,Person
# from django.db.models import Sum, Avg, Min, Max, Count,Q


# Product.objects.create(brand=Brand.objects.first(), product_name = "Samsung Moile with ultra hd display")

def get_person():
    print(Person.objects.all().count())
    
get_person()






