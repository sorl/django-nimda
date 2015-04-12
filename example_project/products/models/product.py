from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class ProductAvailableManager(models.Manager):
    def get_queryset(self):
        qs = super(ProductAvailableManager, self).get_queryset()
        return qs.filter(removed=False)


@python_2_unicode_compatible
class Product(models.Model):
    removed = models.BooleanField(_('removed'), default=False)
    name = models.CharField(_('name'), max_length=500)
    slug = models.SlugField(_('slug'), max_length=500)
    description = models.TextField(_('description'), blank=True)
    list_description = models.TextField(_('list description'), blank=True, help_text=_('short description shown in the list view'))
    list_image = models.ImageField(_('list image'), upload_to='products', blank=True, help_text=_('image shown in the list view'))
    list_image_alt = models.CharField(_('list image alt'), max_length=500, blank=True, help_text=_('alt text for the list image'))
    display_price = models.FloatField(_('display price'), help_text=_('displayed price for the product in list view and before choosing variant'))
    variant_count = models.PositiveIntegerField(editable=False)  # denorm variant count
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    objects = models.Manager()
    available = ProductAvailableManager()

    class Meta:
        app_label = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ('-updated',)

    def __str__(self):
        return self.name
