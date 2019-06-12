from django.db import models

# Create your models here.


class UserGroup(models.Model):
    uuid = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=32)


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)
    ug = models.ForeignKey('UserGroup', null=True, on_delete=models.CASCADE)

