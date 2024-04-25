from django.db import models
from django.utils.translation import gettext_lazy as _

from filebrowser.fields import FileBrowseField
from tinymce.models import HTMLField

# Create your models here.


class Company(models.Model):
    name = models.CharField(_('company name'), max_length=255)
    logo = FileBrowseField(_('company logo'), max_length=255, extensions=['.png'])
    phone = models.CharField(_('company phone'), max_length=255)
    email = models.EmailField(_('company email'), max_length=255)
    about = HTMLField(_('about company'))

    class Meta:
        verbose_name = _('company')
        verbose_name_plural = _('companies')

    def __str__(self):
        return self.name


class Activity(models.Model):
    title = models.CharField(_('activity title'), max_length=255)
    description = models.TextField(_('activity description'))
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='activities'
    )

    class Meta:
        verbose_name = _('activity')
        verbose_name_plural = _('activities')

    def __str__(self):
        return self.title
