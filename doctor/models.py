from django.db import models

class Contact(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"Phone: {self.phone}, Email: {self.email}"

class Availability(models.Model):
    DAY_CHOICES = [
        ("সোমবার", "সোমবার"),
        ("মঙ্গলবার", "মঙ্গলবার"),
        ("বুধবার", "বুধবার"),
        ("বৃহস্পতিবার", "বৃহস্পতিবার"),
        ("শুক্রবার", "শুক্রবার"),
        ("শনিবার", "শনিবার"),
        ("রবিবার", "রবিবার"),
    ]

    doctor = models.ForeignKey('Doctor', related_name='availability', on_delete=models.CASCADE)
    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    time = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.day}: {self.time}"

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    contact = models.OneToOneField(Contact, related_name="doctor", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Doctor/doctor_photos/', null=True, blank=True) 

    def __str__(self):
        return f"{self.name} - {self.specialty}"
# 