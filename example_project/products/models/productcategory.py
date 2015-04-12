from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class ProductCategory(models.Model):
    category = models.ForeignKey('Category', verbose_name=_('category'))
    product = models.ForeignKey('products.Product', verbose_name=_('product'))
    position = models.IntegerField(_('position'), default=0)

    class Meta:
        app_label = 'products'
        verbose_name = _('product category link')
        verbose_name_plural = _('product category links')
        ordering = ('position',)

    def __str__(self):
        return '%s - %s' % (self.product, self.category)
