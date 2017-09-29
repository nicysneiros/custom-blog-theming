from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User)
    header_color = models.CharField(max_length=50)
    header_text_color = models.CharField(max_length=50)
    bg_color = models.CharField(max_length=50)
    title_color = models.CharField(max_length=50)
    text_color = models.CharField(max_length=50)

    def __str__(self):
        return "{first_name} {last_name}'s Profile".format(
            first_name=self.user.first_name,
            last_name=self.user.last_name
        )

    def get_absolute_url(self):
        return reverse('user_profile')