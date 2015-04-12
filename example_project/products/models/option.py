from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Option(models.Model):
    name = models.CharField(_('name'), max_length=500)
    position = models.IntegerField(_('position'), default=0)

    class Meta:
        app_label = 'products'
        verbose_name = _('option')
        verbose_name_plural = _('options')
        ordering = ('position', 'name')

    def __str__(self):
        return self.name
