import random
from django import template
from nimda.base import NimdaException
from django.apps import apps

register = template.Library()


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
        raise NimdaException('Cannot find app list.')
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
                M = apps.get_model(app['app_label'], m['object_name'])
                models.append({
                    'name': m['name'],
                    'count': M._default_manager.all().count(),
                    'color': colors[cidx],
                    'url': m['admin_url']
                })
        return {'models': models}
