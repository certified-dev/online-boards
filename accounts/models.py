from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='st', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_img', blank=False)
    birth_day = models.DateField(null=True)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
