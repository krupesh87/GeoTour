from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime
from uuid import uuid4
def create_id():
    now = datetime.datetime.now()
    now1 = datetime.datetime.now().timestamp()
    return str(now1)+str(now.year)+str(now.month)+str(now.day)+str(uuid4())[:7]
class Video(models.Model):
    id = models.CharField(primary_key=True, default=create_id, editable=False,max_length=1000)
    name=models.CharField(max_length=100,null=True)
    video=models.FileField(upload_to="video/%y")
    collegename=models.CharField(max_length=100,null=True)
    establishin=models.IntegerField(null=True)
    address=models.CharField(max_length=200,null=True)
    branch=models.CharField(max_length=200,null=True)
    information=models.CharField(max_length=200,null=True)
    otherfaculty=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=False)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    number=models.CharField(max_length=12)
    qualification=models.CharField(max_length=100)
    gender=models.CharField(max_length=20,default="Male")

   







 