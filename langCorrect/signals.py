from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Correction, Post


@receiver(post_save, sender=Correction)
def add_correction(sender, instance, created, **kwargs):
    if isinstance(instance, Correction) and created:
        instance.post.correctionsQuantity += 1
        instance.post.save()
        print('+1 исправление')
    else:
        print("Ошибка: Невозможно добавить исправление, пост не указан")


@receiver(pre_save, sender=Post)
def replace_spaces_with_underscores(sender, instance, **kwargs):
    instance.verbose_title = instance.title
    print(instance.verbose_title)
    instance.title = instance.title.replace(' ', '_')
