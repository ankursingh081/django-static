from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Club(models.Model):
    status = models.CharField(max_length=50)
    count = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.status, self.count)


class Detail(models.Model):
    task = models.CharField(max_length=50)
    assign_date = models.DateField(default=timezone.now)
    assign_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.task

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
