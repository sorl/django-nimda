import random
from django import template
from nimda.base import NimdaException
from django.core.urlresolvers import reverse
from operator import itemgetter


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
    # big fat disclaimer, this will only work with default site
    from django.contrib.admin.sites import site
    colors = ['aqua', 'green', 'red', 'white', 'black']
    random.seed('nimdalhc')
    random.shuffle(colors)
    app_labels = []
    models = []
    for m in site._registry.keys():
        if m._meta.app_label not in app_labels:
            app_labels.append(m._meta.app_label)
        cidx = app_labels.index(m._meta.app_label) % len(colors)
        models.append({
            'name': m._meta.verbose_name_plural,
            'app': m._meta.app_label,
            'count': m._default_manager.all().count(),
            'color': colors[cidx],
            'url': reverse('admin:%s_%s_changelist' % (m._meta.app_label, m._meta.model_name))
        })
    return {'models': sorted(models, key=itemgetter('app', 'name'))}
