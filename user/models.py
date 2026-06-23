from django.db import models
import uuid
class contactMessage(models.Model):
    # id= models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False)

    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    attended_to = models.BooleanField(default=False)
    def __str__(self):
        return f' Name= {self.name} Email= {self.email}'

from django.contrib.auth.models import User

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
    ('prefer_not_to_say', 'Prefer not to say'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=120, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=24, choices=GENDER_CHOICES, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'




