import random
from django import template
from nimda.base import NimdaException
from django.apps import apps
from django.utils.html import conditional_escape, format_html
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def label_tag(field):
    if 'label' in field.field:
        contents = format_html('<label>{}</label>', field.field['label'])
    else:
        contents = field.field.label
        widget = field.field.field.widget
        id_ = widget.attrs.get('id') or field.field.auto_id
        if id_:
            attrs = {}
            id_for_label = widget.id_for_label(id_)
            if id_for_label:
                attrs['for'] = id_for_label
            if field.field.field.required:
                attrs['class'] = 'required'
            attrs = flatatt(attrs)
            contents = format_html('<label{}>{}</label>', attrs, contents)
        else:
            contents = conditional_escape(contents)
    return mark_safe(contents)


@register.filter
def add_class(field, class_name):
    css_classes = field.field.widget.attrs.get('class', '')
    if css_classes.find(class_name) == -1:
        css_classes += " %s" % class_name
    field.field.widget.attrs['class'] = css_classes
    return field


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
