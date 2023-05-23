from django.db import models

# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    class meta:
        db_table="login"

class user(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    place=models.CharField(max_length=100)
    photo=models.CharField(max_length=300)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)
    class meta:
        db_table="user"

class product(models.Model):
    product=models.CharField(max_length=100)
    price=models.IntegerField()
    photo=models.CharField(max_length=300)
    class meta:
        db_table="product"

class cart(models.Model):
    USER=models.ForeignKey(user,on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(product,on_delete=models.CASCADE)
    qty=models.IntegerField()
    class meta:
        db_table="cart"


