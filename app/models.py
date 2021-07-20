from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime

# Create your models here.
class myCustomeUser(AbstractUser):
    username = models.CharField(max_length=50, unique="True", blank=False)
    password = models.CharField(max_length=200, blank=False)
    isStudent = models.BooleanField(default=False)
    isQuestionSetter = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(myCustomeUser, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    studentID = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class QuestionSetter(models.Model):
    user = models.OneToOneField(myCustomeUser, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    rank = models.CharField(max_length=50, blank=True)
    isVarified = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Admin(models.Model):
    user = models.OneToOneField(myCustomeUser, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name
