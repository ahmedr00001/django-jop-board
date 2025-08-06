from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class City (models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return str(self.name)



class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15 , blank=True, null=True)
    image = models.ImageField(upload_to='profile/')
    city = models.ForeignKey(City , related_name='user_city' , on_delete=models.CASCADE , null=True , blank=True)

    def __str__(self):
        return str(self.user)

#create new empty profile for each new user after create new user
#using django signals

@receiver(post_save, sender=User)

#post_save mean it will recive signal after click on save 
#sender = User mean it work only when click save from user model sothat work only when add new user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    #sender always will be User
    #instance return user actually ctrated
    #created return True if user create and false if update


