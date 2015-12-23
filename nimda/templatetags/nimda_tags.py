import random
from django import template
from django.apps import apps
from django.contrib.admin.helpers import Fieldline, Fieldset
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper, FilteredSelectMultiple
from django.forms import Select, SelectMultiple
from django.forms.utils import flatatt
from django.utils.html import conditional_escape, format_html
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from nimda.base import NimdaException


register = template.Library()


@register.filter
def label_tag(field):
    if 'label' in field.field:
        # read only field
        contents = format_html('<label>{}</label>', field.field['label'])
    else:
        contents = field.field.label
        widget = field.field.field.widget
        id_ = widget.attrs.get('id') or field.field.auto_id
        if id_:
            attrs = {}
            css_classes = []
            id_for_label = widget.id_for_label(id_)
            if id_for_label:
                attrs['for'] = id_for_label
            if field.field.field.required:
                css_classes.append('required')
            attrs['class'] = ' '.join(css_classes)
            attrs = flatatt(attrs)
            contents = format_html('<label{}>{}</label>', attrs, contents)
        else:
            contents = conditional_escape(contents)
    return mark_safe(contents)


@register.filter
def add_classes(field):
    css_classes = field.field.widget.attrs.get('class', '').split(' ')
    css_classes.append('form-control')
    widget = field.field.widget
    widget.attrs['class'] = ' '.join(css_classes)
    if not isinstance(widget, (Select, SelectMultiple, RelatedFieldWidgetWrapper)):
        return field
    if hasattr(field, 'no_select2') and widget.no_select2:
        return field
    rmthis = str(_('Hold down "Control", or "Command" on a Mac, to select more than one.'))
    field.help_text = str(field.help_text).replace(rmthis, '')
    css_classes.append('select2')
    if isinstance(field.field.widget, RelatedFieldWidgetWrapper):
        # make that ugly filter go away
        if isinstance(field.field.widget.widget, FilteredSelectMultiple):
            field.field.widget.widget = SelectMultiple()
        field.field.widget.widget.attrs['class'] = ' '.join(css_classes)
        id_ = field.field.widget.widget.attrs.get('id') or field.auto_id
    else:
        id_ = field.field.widget.attrs.get('id') or field.auto_id
    placeholder = _('Select %s') % str(field.label).lower()
    return mark_safe('%s<script>$(function() { $("#%s").select2({"placeholder": "%s"}) });</script>' % (field, id_, placeholder))


@register.filter
def inline_td_classes(field):
    css_classes = field.field.widget.attrs.get('class', '').split(' ')
    css_classes.append(field.field.widget.attrs.get('type', ''))
    if field.name:
        css_classes.append(field.name)
    return ' '.join(css_classes)


@register.inclusion_tag('admin/includes/sidebar_menu.html', takes_context=True)
def sidebar_menu(context):
    if 'app_list' in context:
        available_apps = context['app_list']
    elif 'available_apps' in context:
        available_apps = context['available_apps']
    elif 'request' in context:
        # big fat disclaimer, this will only work with default site
        from django.contrib.admin.sites import site
        res = site.index(context['request'])
        available_apps = res.context_data['app_list']
    else:
        raise NimdaException(
            'Cannot find app list. Add '
            '"django.template.context_processors.request" to you list of '
            'context context_processors to use the default admin site '
            'or better yet use nimda.base.NimdaSiteMixin for your admin site '
            'class.')
    return {'available_apps': available_apps}


@register.inclusion_tag('admin/includes/model_summary.html', takes_context=True)
def model_summary(context):
    if 'app_list' in context:
        colors = ['aqua', 'green', 'red', 'white', 'black']
        random.seed('nimdalhc')
        random.shuffle(colors)
        models = []
        for j, app in enumerate(context['app_list']):
            for m in app['models']:
                cidx = j % len(colors)
                model = apps.get_model(app['app_label'], m['object_name'])
                models.append({
                    'name': m['name'],
                    'count': model._default_manager.all().count(),
                    'color': colors[cidx],
                    'url': m['admin_url']
                })
        return {'models': models}
