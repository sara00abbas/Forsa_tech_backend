from django.db import models
from devloper.models import User

class humanResources(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return str(self.user)