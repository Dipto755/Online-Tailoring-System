from django.dispatch import receiver
from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from TailorApp.models import user_model, kameez_order_model


user = get_user_model()

@receiver(post_save, sender = user)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        user_model.objects.create(
            user = instance
        )
        # kameez_order_model.objects.create(
        #     user = instance
        # )