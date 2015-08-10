from django import template

register = template.Library()


@register.simple_tag()
def multiply(a, b):
    return a * b


@register.filter
def to_hours(timedelta):
    return timedelta.days*24 + timedelta.seconds / 3600
