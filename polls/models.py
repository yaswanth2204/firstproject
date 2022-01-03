from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=122)
    name=models.CharField(max_length=122)
    contact=models.CharField(max_length=12)
    report=models.TextField()

    def __str__(self):
        return self.name

