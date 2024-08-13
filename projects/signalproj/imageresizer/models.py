from django.db import models
from .middleware import get_current_request
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import os
class Student(models.Model):
    gender_choices = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))
    student_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=15,choices=gender_choices)
    student_id = models.CharField(max_length=50,null=True,blank=True)
    
    
class ImageStore(models.Model):
    original_image = models.ImageField(upload_to='images/',null=True,blank=True)
    thumbnail_small = models.ImageField(upload_to='images/thumbnails',null=True,blank=True)
    thumbnail_medium = models.ImageField(upload_to='images/thumbnails',null=True,blank=True)
    thumbnail_large = models.ImageField(upload_to='images/thumbnails',null=True,blank=True)
    
@receiver(post_save, sender=ImageStore)    
def create_thumbnails(sender,instance,created, **kwargs):
    
    if created:
        sizes = {
            "thumbnail_small":(100,100),
            "thumbnail_medium":(300,300),
            "thumbnail_large": (600,600)
        }
        
        for fields,size in sizes.items():
            img = Image.open(instance.original_image.path)
            img.thumbnail(size, Image.Resampling.LANCZOS)
            thumb_name,thumb_extension = os.path.split(instance.original_image.name)
            thumb_extension = thumb_extension.lower()
            thmb_filename = f"{thumb_name}_{size[0]}X{size[1]}{thumb_extension}"
            thumb_path = f'thumbnails/{thmb_filename}'
            img.save(thumb_path)
            setattr(instance,fields,thumb_path)
        
        
        
        
@receiver(post_save,sender = Student)   
def save_student(sender,instance,created, **kwargs):
    
    print(sender,instance)
    if created:
        instance.student_id = f'STU-000{instance.id}'
        instance.save()
        
        request = get_current_request()
        if request and request.user:
            user = request.user
            print(f'Student object created by {user.username}')
        else:
            print('Request or user not found.')
    print('Student object created')
    
    
