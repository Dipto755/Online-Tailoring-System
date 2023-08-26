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
