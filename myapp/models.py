from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    groupName=models.CharField(max_length=30,verbose_name="نام گروه")
    members=models.ForeignKey(User,verbose_name="اعضا",null=True,on_delete=models.CASCADE)
    description=models.TextField(max_length=100,verbose_name="توضیحات گروه")
