from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class OptionValue(models.Model):
    variant = models.ForeignKey('products.Variant', verbose_name=_('variant'), related_name='option_values')
    option = models.ForeignKey('products.Option', verbose_name=_('option'))
    value = models.CharField(_('value'), max_length=500)
    position = models.IntegerField(_('position'), default=0)

    class Meta:
        app_label = 'products'
        verbose_name = _('option value')
        verbose_name_plural = _('option value')
        unique_together = (('variant', 'option'),)
        ordering = ('position',)

    def __str__(self):
        return '%s - %s' % (self.option, self.value)
