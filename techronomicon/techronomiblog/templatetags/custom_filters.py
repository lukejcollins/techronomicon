from django import template
from django.utils.dateformat import DateFormat

register = template.Library()

@register.filter(name='rfc3339')
def format_rfc3339(value):
    df = DateFormat(value)
    return df.format('Y-m-d\TH:i:sO')
