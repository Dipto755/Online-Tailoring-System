from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()
class user_model(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # u_id = models.IntegerField(primary_key=True)
    # u_name = models.CharField(max_length=30)
    # u_email = models.EmailField(max_length=30)
    u_address = models.TextField()
    u_cont_number = models.CharField(max_length=11)
    u_gender = models.CharField(max_length=10)
    # password = models.CharField(max_length=30)
    updateon = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username

class fabric_model(models.Model):
    f_id = models.IntegerField(primary_key=True)
    f_name = models.CharField(max_length=30)
    # f_color = models.CharField(max_length=20)
    f_type = models.CharField(max_length=30)
    f_price = models.IntegerField()
    f_image = models.ImageField(upload_to="fabric/images", default="")
    
    def __str__(self):
        return self.f_name

class design_model(models.Model):
    d_id = models.IntegerField(primary_key=True)
    d_name = models.CharField(max_length=30)
    d_image1 = models.ImageField(upload_to="design/images", default="")
    d_image2 = models.ImageField(upload_to="design/images", default="")
    d_image3 = models.ImageField(upload_to="design/images", default="")
    
    def __str__(self):
        return self.d_name

class order_model(models.Model):
    o_id = models.IntegerField(primary_key=True)
    o_date = models.DateField()
    o_type = models.CharField(max_length=30)
    o_due = models.DateField()

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

class measurementForKameez_model(models.Model):
    k_productID = models.IntegerField(primary_key=True)
    k_neckdep = models.IntegerField()
    k_chest = models.IntegerField()
    k_waist = models.IntegerField()
    k_len = models.IntegerField()
    
class measureForSalwar_model(models.Model):
    sl_hip = models.IntegerField(primary_key=True)
    sl_len = models.IntegerField()
    
class measurementForPant_model(models.Model):
    pnt_len = models.IntegerField(primary_key=True)
    pnt_waist = models.IntegerField()
    pnt_inseam = models.IntegerField()
    pnt_hsize = models.IntegerField()
    
class feedback_model(models.Model):
    f_id = models.IntegerField(primary_key=True)
    f_review = models.IntegerField()
    f_comment = models.TextField()