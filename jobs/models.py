from django.db import models
import uuid
from django.contrib.auth.models import User

class Job(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=250)
    description = models.TextField()
    salary = models.PositiveBigIntegerField()
    sold = models.PositiveIntegerField(default=0)
    qualification = models.TextField()
    image = models.ImageField(upload_to='product/')
    # user deletes profile, products delete too
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} == {self.id}'


class Apply(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    dob = models.DateField()
    school = models.CharField(max_length=250)
    qualification = models.TextField()
    years = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to='product/')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications', null=True, blank=True)

#  user deletes profile, products remain
# user=models.ForeignKey(User, on_delete=models.SET_NULL)
#  user deletes profile, products transfers to a default user
# user=models.ForeignKey(User, on_delete=models.SET_DEFAULT)
# Create your models here.
