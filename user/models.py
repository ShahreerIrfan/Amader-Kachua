from django.db import models
from .constants import UNION_CHOICES
from .constants import BLOOD_GROUP_CHOICES
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phohne_number = models.CharField(max_length=20,null= True)
    village = models.CharField(max_length=80,null= True)
    photo = models.ImageField(upload_to="user/profile_photo",null= True)
    union = models.CharField(max_length=20, choices=UNION_CHOICES, null=True, blank=True)
    district = models.CharField(max_length=30,null= True)
    address = models.TextField(null=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, null=True, blank=True)
    occupation = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.user.username} {self.user.first_name} {self.user.last_name}"
    
    
    
    
    
    
    