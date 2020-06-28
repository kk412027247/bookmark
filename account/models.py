from django.db import models
from django.conf import settings


class Profile(models.Model):
    # You use CASCADE for the on_delete parameter so that its related profile also gets deleted when a user is deleted.
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user/%y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
