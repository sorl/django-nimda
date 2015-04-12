from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True)
    name = models.CharField(_('name'), max_length=500)
    slug = models.SlugField(_('slug'), max_length=500)
    description = models.TextField(_('description'), blank=True)
    position = models.IntegerField(_('position'), default=0)

    class Meta:
        app_label = 'products'
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('position',)

    def __str__(self):
        return self.name
