from django.contrib.auth.models import User
from django.db import models


class PasswordSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    use_special_characters = models.BooleanField(default=True)
    use_uppercase = models.BooleanField(default=True)
    use_numbers = models.BooleanField(default=True)
    password_length = models.PositiveIntegerField(default=12)

    def __str__(self):
        return self.user


class SavedPassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True, null=True)