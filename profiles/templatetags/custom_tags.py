from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag(name='edit_link')
def edit_link(obj):
    return reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
