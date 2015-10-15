from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.contrib.admin.options import csrf_protect_m
from django.utils.text import capfirst


class ModelAdmin(admin.ModelAdmin):
    def get_add_title(self, request, obj=None):
        if hasattr(self, 'add_title'):
            return self.add_title
        return _('Add %s') % self.model._meta.verbose_name

    def get_change_title(self, request, obj=None):
        if hasattr(self, 'change_title'):
            return self.change_title
        return self.model._meta.verbose_name

    def get_list_title(self, request):
        if hasattr(self, 'list_title'):
            return self.list_title
        return self.model._meta.verbose_name_plural

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = capfirst(self.get_list_title(request))
        return super(ModelAdmin, self).changelist_view(
            request, extra_context
        )

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        if add:
            context['title'] = capfirst(self.get_add_title(request, obj))
        else:
            context['title'] = capfirst(self.get_change_title(request, obj))
        return super(ModelAdmin, self).render_change_form(
            request, context, add, change, form_url, obj
        )
