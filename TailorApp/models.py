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

class design_kameez_model(models.Model):
    dk_id = models.IntegerField(primary_key=True)
    dk_name = models.CharField(max_length=30)
    dk_neck = models.CharField(max_length=30,default = "")
    dk_type = models.CharField(max_length=30,default = "")
    dk_sleeve = models.CharField(max_length=30,default = "")
    dk_price = models.IntegerField()
    dk_image1 = models.ImageField(upload_to="design/design_kameez/images", default="")
    dk_image2 = models.ImageField(upload_to="design/design_kameez/images", default="")
    dk_image3 = models.ImageField(upload_to="design/design_kameez/images", default="")
    
    def __str__(self):
        return self.dk_name

class design_salowaar_model(models.Model):
    ds_id = models.IntegerField(primary_key=True)
    ds_name = models.CharField(max_length=30)
    ds_price = models.IntegerField()
    ds_image1 = models.ImageField(upload_to="design/design_salowaar/images", default="")
    
    def __str__(self):
        return self.ds_name

class design_shirt_model(models.Model):
    dsh_id = models.IntegerField(primary_key=True)
    dsh_name = models.CharField(max_length=30)
    dsh_hand = models.CharField(max_length=30,default = "")
    dsh_price = models.IntegerField()
    dsh_image1 = models.ImageField(upload_to="design/design_shirt/images", default="")
    dsh_image2 = models.ImageField(upload_to="design/design_/images", default="")
    
    
    def __str__(self):
        return self.dsh_name

class kameez_order_model(models.Model):
    f_id = models.ForeignKey(fabric_model, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dk_id = models.ForeignKey(design_kameez_model, on_delete=models.DO_NOTHING)
    o_id = models.IntegerField(primary_key=True)
    o_date = models.DateField()
    o_type = models.CharField(max_length=30)
    o_due = models.DateField()
    
class salowaar_order_model(models.Model):
    f_id = models.ForeignKey(fabric_model, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ds_id = models.ForeignKey(design_salowaar_model, on_delete=models.DO_NOTHING)
    o_id = models.IntegerField(primary_key=True)
    o_date = models.DateField()
    o_type = models.CharField(max_length=30)
    o_due = models.DateField()
    
class shirt_order_model(models.Model):
    f_id = models.ForeignKey(fabric_model, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dsh_id = models.ForeignKey(design_shirt_model, on_delete=models.DO_NOTHING)
    o_id = models.IntegerField(primary_key=True)
    o_date = models.DateField()
    o_type = models.CharField(max_length=30)
    o_due = models.DateField()
    
class type_model(models.Model):
    ty_id = models.IntegerField(primary_key=True)
    ty_name = models.CharField(max_length=50)
    ty_image = models.ImageField(upload_to="types/images", default="")
    
    def __str__(self):
        return self.ty_name

class payment_model(models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_method = models.CharField(max_length=20)
    

class measurementForShirt_model(models.Model):
    s_productID = models.IntegerField(primary_key=True)
    # s_neck = models.IntegerField()
    # s_sleeve = models.IntegerField()
    # s_chest = models.IntegerField()
    # s_waist = models.IntegerField()
    # s_length = models.IntegerField()
    s_collar_length = models.IntegerField()
    s_sleeve_length = models.IntegerField()
    s_shoulder_length = models.IntegerField()
    s_bicep = models.IntegerField()
    s_chest_length = models.IntegerField()
    s_hip_length = models.IntegerField()

class measurementForKameez_model(models.Model):
    k_productID = models.IntegerField(primary_key=True)
    # k_neckdep = models.IntegerField()
    # k_chest = models.IntegerField()
    # k_waist = models.IntegerField()
    k_length = models.IntegerField()
    k_body_length = models.IntegerField()
    k_shoulder_length = models.IntegerField()
    k_waist_length = models.IntegerField()
    k_hip_length = models.IntegerField()
    k_hand_width = models.IntegerField()
    k_neck_length = models.IntegerField()
    k_neck_width = models.IntegerField()
    
class measureForSalwar_model(models.Model):
    sl_productID = models.IntegerField(primary_key=True)
    # sl_hip = models.IntegerField()
    # sl_len = models.IntegerField()
    sl_length = models.IntegerField()
    sl_waist_length = models.IntegerField()
    sl_hip_length = models.IntegerField()
    sl_thigh_length = models.IntegerField()
    sl_width = models.IntegerField()
    
class measurementForPant_model(models.Model):
    pnt_len = models.IntegerField(primary_key=True)
    pnt_waist = models.IntegerField()
    pnt_inseam = models.IntegerField()
    pnt_hsize = models.IntegerField()
    
class feedback_model(models.Model):
    f_id = models.IntegerField(primary_key=True)
    f_review = models.IntegerField()
    f_comment = models.TextField()