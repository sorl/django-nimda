from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class OrderLine(models.Model):
    order = models.ForeignKey('Order', verbose_name=_('order'), related_name='orderlines')
    variant = models.ForeignKey('products.Variant', verbose_name=_('variant'), blank=True, null=True)  # for reference
    name = models.CharField(_('name'), max_length=500)
    quantity = models.PositiveIntegerField(_('quantity'), default=1)
    price_tax_excl = models.FloatField(_('price tax excluded'))
    tax_rate_percent = models.FloatField(_('tax rate'))
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        app_label = 'orders'
        verbose_name = _('order line')
        verbose_name_plural = _('order lines')
        ordering = ('created',)

    def __str__(self):
        return '%s - %s' % (self.order, self.name)

    @property
    def total_tax_excl(self):
        return self.quantity * self.price_tax_excl

    @property
    def total_tax_incl(self):
        return self.quantity * self.price_tax_incl
