from django.db import models
from multiselectfield import MultiSelectField
class Account(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    contact_no=models.IntegerField()
    describe_yourself=models.CharField(max_length=100)
    Choose_a_profile_picture=models.ImageField()
    what_are_you_in_interested=models.CharField(max_length=100)
    LANGUAGES_CHOICES=(
        ('Eng','English'),
        ('Tel','Telugu'),
        ('Hin','Hindi'),
        ('Kan','Kannada'),
    )
    Preferred_Languages=MultiSelectField(max_length=150,choices=LANGUAGES_CHOICES)
class test2(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


