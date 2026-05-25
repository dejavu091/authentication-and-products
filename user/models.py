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






