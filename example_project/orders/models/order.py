from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


ORDER_STATES = (
    ('cart', 'cart'),  # One or more products have been added to the shopping cart.
    ('address', 'address'),  # The store is ready to receive the billing and shipping address information for the order.
    ('delivery', 'delivery'),  # The store is ready to receive the shipping method for the order.
    ('payment', 'payment'),  # The store is ready to receive the payment information for the order.
    ('confirm', 'confirm'),  # The order is ready for a final review by the customer before being processed.
    ('complete', 'complete'),  # The order has successfully completed all of the previous states and is now being processed.
)


PAYMENT_STATES = (
    ('checkout', 'checkout'),  # The checkout has not been completed.
    ('processing', 'processing'),  # The payment is being processed.
    ('pending', 'pending'),  # The payment has been processed but is not yet complete (ex. authorized but not captured).
    ('failed', 'failed'),  # The payment was rejected (ex. credit card was declined).
    ('void', 'void'),  # The payment should not be applied against the order.
    ('completed', 'completed'),  # The payment is completed. Only payments in this state count against the order total.
)

SHIPMENT_STATES = (
    ('pending', 'pending'),  # The shipment has backordered inventory units and/or the order is not paid for.
    ('ready', 'ready'),  # The shipment has no backordered inventory units and the order is paid for.
    ('shipped', 'shipped'),  # The shipment is on its way to the buyer.
    ('cancelled', 'cancelled'),  # When an order is cancelled, all of its shipments will also be cancelled. When this happens, all items in the shipment will be restocked. If an order is "resumed", then the shipment will also be resumed.
)


class OrderManager(models.Manager):
    def get_queryet(self):
        qs = super(OrderManager, self).get_queryet()
        return qs.prefetch_related('orderlines')


@python_2_unicode_compatible
class Order(models.Model):
    number = models.CharField(_('order number'), max_length=500)
    state = models.CharField(_('state'), max_length=500, choices=ORDER_STATES, default='cart')
    payment_state = models.CharField(_('payment state'), max_length=500, choices=PAYMENT_STATES, default='checkout')
    shipment_state = models.CharField(_('shipping state'), max_length=500, blank=True, choices=SHIPMENT_STATES, default='')
    shipping_method = models.CharField(_('shipping method'), max_length=500, blank=True)
    special_instructions = models.TextField(_('special instructions'), blank=True)
    shipping_total_tax_excl = models.FloatField(_('shipping total tax excluded'), default=0)
    shipping_total_tax_incl = models.FloatField(_('shipping total tax included'), default=0)
    grand_total_tax_incl = models.FloatField(_('grand total with tax excluded'), default=0)
    grand_total_tax_excl = models.FloatField(_('grand total with tax included'), default=0)
    discount = models.FloatField(_('discount'), default=0)

    email = models.EmailField(_('email'), max_length=500, blank=True)
    phone = models.CharField(_('phone number'), max_length=500, blank=True)

    billing_first_name = models.CharField(_('billing first name'), max_length=500, blank=True)
    billing_last_name = models.CharField(_('billing last name'), max_length=500, blank=True)
    billing_company = models.CharField(_('billing company'), max_length=500, blank=True)
    billing_address1 = models.CharField(_('billing address'), max_length=500, blank=True)
    billing_address2 = models.CharField(_('billing address'), max_length=500, blank=True)
    billing_city = models.CharField(_('billing city'), max_length=500, blank=True)
    billing_state = models.CharField(_('billing state'), max_length=500, blank=True)
    billing_country = models.CharField(_('billing country'), max_length=500, blank=True)

    shipping_first_name = models.CharField(_('shipping first name'), max_length=500, blank=True)
    shipping_last_name = models.CharField(_('shipping last name'), max_length=500, blank=True)
    shipping_company = models.CharField(_('shipping company'), max_length=500, blank=True)
    shipping_address1 = models.CharField(_('shipping address'), max_length=500, blank=True)
    shipping_address2 = models.CharField(_('shipping address'), max_length=500, blank=True)
    shipping_city = models.CharField(_('shipping city'), max_length=500, blank=True)
    shipping_state = models.CharField(_('shipping state'), max_length=500, blank=True)
    shipping_country = models.CharField(_('shipping country'), max_length=500, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    objects = OrderManager()

    class Meta:
        app_label = 'orders'
        verbose_name = _('order')
        verbose_name_plural = _('orders')
        ordering = ('-created',)

    def __str__(self):
        return self.number
