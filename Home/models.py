from typing import Iterable
from django.db import models
from django.template.defaultfilters import slugify
from Home.utils import generate_slug
from django.db.models import CheckConstraint,Q


class Student(models.Model):
    gender_choices = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=gender_choices,max_length=10,default='Male')
    age = models.IntegerField(null=True,blank=True)
    dob = models.DateField()
    file = models.FileField(upload_to='files/')
    profile_image = models.ImageField(null=True, blank=True, upload_to='student_images/')
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Student2(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    phone = models.CharField(max_length=12)
    
    class Meta:
        constraints = [
            CheckConstraint(check=Q(age__gte=18),name = 'age_gte_18')
        ]

# class CollegeStudent(Student2):
#     class Meta:
#         proxy = True
#         constraints = [
#             CheckConstraint(check=Q(age__gte=18),name = 'age_gte_18')
#         ]
       

    
# >>> from Home.models import * 
# >>> Author.objects.create(author_name = "Lee")
# <Author: Author object (1)>
# >>> Author.objects.create(author_name = "Shatapathy") 
# <Author: Author object (2)>
# >>> a1 = Author.objects.get(id = 1) 
# >>> Book.objects.create(author=a1,book_name="Preeti ek prem katha") 
# <Book: Book object (1)>


class Brand(models.Model):
    brand_name = models.CharField(max_length=255)
    country = models.CharField(max_length=50, default='India')
    # #dunder str
    def __str__(self):
        return self.brand_name
    class Meta:
        unique_together = ('brand_name','country')


#Product model uses for generation of slug field and override of save method.. 
class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100,null=True,blank=True)
    
    
    def save(self,*args, **kwargs) -> None:
        if not self.id:
            self.slug = generate_slug(self.product_name,Product)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.product_name
    
    
#Person table used for bulk create bulk update bulk delete and soft deletion

class DeletionManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_delete=False)

class Person(models.Model):
    person_name = models.CharField(max_length=255)
    skill = models.CharField(max_length=255,blank=True,null=True)
    is_delete = models.BooleanField(default=False)
    objects = DeletionManager()
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=120)
    message  = models.TextField()
    is_delete = models.BooleanField(default=False)   
    
# CRUD
#C-Create
# python manage.py shell
# >>> from Home.models import * 
# >>> Author.objects.create(author_name = "New Bee")
# <Author: Author object (3)>
# >>> author = Author(author_name= "Stainlee")
# >>> authr.save()

# Read
# >>> brands = Brand.objects.all()
# >>> brands
# <QuerySet [<Brand: Brand object (1)>, <Brand: Brand object (2)>, <Brand: Brand object (3)>, <Brand: Brand object (4)>]>
# >>> for brand in brands:
# ...      print(brand) 
# ...
# Brand object (1)
# Brand object (2)
# Brand object (3)
# Brand object (4)
# >>> for brand in brands:
# ...     print(brand.brand_name)
# ...
# ITC
# Apple
# Patanjali
# LG

# >>> brands = Brand.objects.all().order_by('brand_name') 
# >>> for brand in brands:
# ...     print(brand.brand_name) 
# ...
# Apple
# ITC
# LG
# Patanjali
# >>> brand = Brand.objects.get(id=1)
# >>> print(brand.brand_name) 
# ITC

###Update


# >>> brand = Brand.objects.get(brand_name = "LG")
# >>> brand.country = "China" 
# >>> brand.save()
# >>> brands = Brand.objects.all()          
# >>> for brand in brands:
# ...     if brand.brand_name == "LG": 
# ...             brand.country = "Taiwan"  
# ...             brand.save()


#Delete
# p1 = Products.objects.get(id=2)                             
# >>> p1.product_name = "pump12" 
# >>> p1.save()
# >>> b1=Brand.objects.get(id=1)
# >>> b1.delete()
# (4, {'Home.Products': 3, 'Home.Brand': 1})
# >>> 


# #Foreignkey(One to one relation)
# # Ex:
# # One college and its department
# # We have to define two tables One is for college and second one is for Departments
# #College Table
# class College(models.Model):
#     clg_name = models.CharField(max_length=255)
#     estd = models.DateField()
#     address = models.TextField()
#     naac_grade = models.CharField(max_length=5)
#     is_university = models.BooleanField(default=False)
#     registered_dt = models.DateTimeField(auto_created=True)
    
# class Department(models.Model):
#     department_choices = (("Sciene","Sciene"),("Commerce","Commerce"),("Arts","Arts"))
#     college = models.ForeignKey(College,on_delete=models.CASCADE)
#     dept_name = models.CharField(choices=department_choices)
#     hod = models.OneToOneField('Hod', on_delete=models.SET_NULL, null=True, blank=True)
    
# class Hod(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     age = models.IntegerField()
#     qualification = models.CharField(max_length=255, null=True, blank=True)
#     specification = models.CharField(max_length=255, null=True, blank=True)
#     department = models.OneToOneField(Department, on_delete=models.CASCADE)
#     is_retired = models.BooleanField(default=False)
    

    
# class Course(models.Model):
#     name = models.CharField(max_length=100)
#     code = models.CharField(max_length=10)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
    
# class Subject(models.Model):
#     sub_type = (("Cumpolsary","Cumpolsary"),("Elective","Elective"))
#     name = models.CharField(max_length=100)
#     code = models.CharField(max_length=10)
#     subject_type = models.CharField(choices=sub_type,default="Cumpolsary")
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
# class Student(models.Model):
#     gender_choices = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))
#     college = models.ForeignKey(College,on_delete=models.CASCADE)
#     department = models.ForeignKey(Department,on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=12)
#     email = models.EmailField(unique=True)
#     gender = models.CharField(choices=gender_choices,max_length=10,default='Male')
#     age = models.IntegerField(null=True,blank=True)
#     dob = models.DateField()
#     file = models.FileField(upload_to='files/')
#     prfile_image = models.ImageField(null=True, blank=True, upload_to='student_images/')
#     bio = models.TextField()
#     subject = models.ManyToManyField(Subject, on_delete = models.SET_NULL)
#     created_at = models.DateTimeField(auto_created=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
    
    
# Testing Faker model

class CollegeFaker(models.Model):
    college_name = models.CharField(max_length=255)
    college_address = models.CharField(max_length=255)
    

class StudentFaker(models.Model):
    gender_choices = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))
    college = models.ForeignKey(CollegeFaker,on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=gender_choices,max_length=10,default='Male')
    age = models.IntegerField(null=True,blank=True)
    dob = models.DateField()
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
class Author(models.Model):
    author_name = models.CharField(max_length=255)
    
class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publish_date = models.DateField()
    
    class Meta:
        db_table = "book"
        ordering =("price","book_name")
        
        
        
#Example of abstract model


class Human(models.Model):
    gender_choices = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(choices=gender_choices,max_length=10)
    
    class Meta:
        abstract = True
        
class Engineer(Human):
    skills=models.CharField(max_length=100)
    designation= models.CharField(max_length=100)
    
class Hr(Human):
    branch = models.CharField(max_length=100)
    
class Investors(Human):
    money = models.CharField(max_length=20)
    
    
    
    



    

    

    

    
    
    
    