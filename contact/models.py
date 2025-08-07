from django.db import models

# Create your models here.
class Info (models.Model):
    place = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

#now we want contact form to be sent to email 
#and not save in database