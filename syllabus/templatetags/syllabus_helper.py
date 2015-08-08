from django import template

register = template.Library()


@register.simple_tag()
def multiply(a, b):
    return a * b


@register.filter
def to_minutes(value):
    return value.seconds/60
