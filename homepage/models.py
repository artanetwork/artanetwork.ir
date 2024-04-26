from django.db import models
from django.utils.translation import gettext_lazy as _

from filebrowser.fields import FileBrowseField

# Create your models here.


class Slider(models.Model):
    title = models.CharField(_('slider title'), max_length=255)
    subtitle = models.CharField(_('slider subtitle'), max_length=255)

    class Meta:
        verbose_name = _('slider')
        verbose_name_plural = _('sliders')

    def __str__(self):
        return self.title


class Slide(models.Model):
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE, related_name='slides')
    image = FileBrowseField(
        _('slide image'), max_length=255, directory='slides/', extensions=['.jpg']
    )
