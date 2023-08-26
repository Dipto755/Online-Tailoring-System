from django.db import models

# Create your models here.

class user_model(models.Model):
    u_id = models.IntegerField(primary_key=True)
    u_name = models.CharField(max_length=30)
    u_email = models.EmailField(max_length=30)
    u_address = models.TextField()
    u_cont_number = models.CharField(max_length=11)
    u_gender = models.CharField(max_length=10)
    password = models.CharField(max_length=30)

class fabric_model(models.Model):
    f_id = models.IntegerField(primary_key=True)
    f_name = models.CharField(max_length=30)
    f_color = models.CharField(max_length=20)
    f_type = models.CharField(max_length=30)
    f_price = models.IntegerField()
    
class payment_model(models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_method = models.CharField(max_length=20)
    

class measurementForShirt_model(models.Model):
    s_productID = models.IntegerField(primary_key=True)
    s_neck = models.IntegerField()
    s_sleeve = models.IntegerField()
    s_chest = models.IntegerField()
    s_waist = models.IntegerField()
    s_length = models.IntegerField()