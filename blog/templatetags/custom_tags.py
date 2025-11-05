from django import template

register = template.Library()

@register.filter(name='is_marketer')
def is_marketer(user):
    return user.groups.filter(name="af_marketer").exists()
