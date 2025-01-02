from django.db import models

class FireStation(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True)
    image  = models.ImageField(upload_to="Fire_service/images",null=True,blank=True)
    location = models.CharField(max_length=255,null=True, blank=True)
    phone = models.CharField(max_length=15,null=True, blank=True)
    mobile = models.CharField(max_length=15,null=True, blank=True)
    telMobile = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return self.name
