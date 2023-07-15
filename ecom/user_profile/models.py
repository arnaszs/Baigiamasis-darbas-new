from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from PIL import Image



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        verbose_name=_("user"),
        related_name='profile',
        on_delete=models.CASCADE,
        blank=True, null=True)
    picture = models.ImageField(_("picture"), upload_to='user_profile')
    

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        if self.picture:
            pic = Image.open(self.picture.path)
            if pic.width > 300 or pic.height > 300:
                new_size = (300, 300)
                pic.thumbnail(new_size)
                pic.save(self.picture.path)