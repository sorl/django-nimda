from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class CartItem(models.Model):
    cart = models.ForeignKey('carts.Cart', verbose_name=_('cart'), related_name='cartitems')
    variant = models.ForeignKey('products.Variant', verbose_name=_('variant'))
    quantity = models.PositiveIntegerField(_('quantity'), default=1)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return '%s - %s' % (self.cart, self.variant)

    class Meta:
        app_label = 'carts'
        verbose_name = _('cart item')
        verbose_name_plural = _('cart items')
        ordering = ('-created',)
