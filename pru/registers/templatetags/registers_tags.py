from django import template
from ..models import Register
register = template.Library()


@register.filter
def display_register_status(value):
    return Register.STATUS[value]
