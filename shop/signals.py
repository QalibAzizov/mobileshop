from django.db.models.signals import pre_save
from django.dispatch import receiver
from shop.models import *
from slugify import slugify



@receiver(pre_save, sender=Category)
def story_object_creation(sender,instance , **kwargs):
    print('instance', instance)
    instance.slug = slugify(instance.title)


@receiver(pre_save, sender = Brand)
def story_object_creation(sender,instance , **kwargs):
    instance.slug = slugify(instance.title)


@receiver(pre_save, sender = Discount)
def story_object_creation(sender,instance , **kwargs):
    instance.slug = slugify(instance.title)    


@receiver(pre_save, sender = Product)
def story_object_creation(sender,instance ,**kwargs):
    instance.slug = slugify(instance.title)