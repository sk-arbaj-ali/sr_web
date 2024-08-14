from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    topics = models.TextField()
    start_date = models.DateField()
    first_revision = models.DateField()
    second_revision = models.DateField()
    third_revision = models.DateField()
    fourth_revision = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} : {self.start_date}"
    
    def save(self, *args, **kwargs):
        self.first_revision = self.start_date + timedelta(days=3)
        self.second_revision = self.start_date + timedelta(days=7)
        self.third_revision = self.start_date + timedelta(days=15)
        self.fourth_revision = self.start_date + timedelta(days=21)
        # call the parent class method
        super().save(*args,**kwargs)