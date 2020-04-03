from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _


UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    in_newsletter = models.BooleanField(_("In newsletter?"), default=False)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return "{}, {}: {}".format(self.user.email, _('in newsletter'),
                                   self.in_newsletter)


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # runs only if user was created
        Profile.objects.create(user=instance)


@receiver(post_save, sender=UserModel)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except:
        Profile.objects.create(user=instance)
