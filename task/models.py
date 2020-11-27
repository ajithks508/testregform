from django.db import models

# Create your models here.
class Login(models.Model):
	username=models.CharField(max_length=50, unique=True)
	password=models.CharField(max_length=50)
	option=models.CharField(max_length=50)
class Registeruser(models.Model):
	firstname=models.CharField(max_length=50, unique=True)
	lastname=models.CharField(max_length=50)
	age=models.CharField(max_length=50)
	gender=models.CharField(max_length=10)
	mobile1=models.CharField(max_length=50)
	option=models.CharField(max_length=50)
	address=models.CharField(max_length=100)
	city=models.CharField(max_length=100)
	country=models.CharField(max_length=100)
	location=models.CharField(max_length=100)
	login=models.ForeignKey(Login,null=True,on_delete=models.CASCADE,related_name='login_id')

