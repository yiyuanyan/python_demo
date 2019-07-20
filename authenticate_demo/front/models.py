from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.


# class Person(User):
#     class Meta:
#         proxy = True
#
#     @classmethod
#     def get_blacklist(cls):
#         return cls.objects.filter(is_active=False)


class UserExtension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extension')
    telephone = models.CharField(max_length=11)
    school = models.CharField(max_length=100)

@receiver(post_save, sender=User)
def handler_user_extension(sender, instance, created, **kwargs):
    if created:
        UserExtension.objects.create(user=instance)
    else:
        instance.extension.save()