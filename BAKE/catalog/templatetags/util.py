from django import template

register = template.Library()


@register.filter
def prettify_for_number(number):
    number = str(number)
    return '{} ({}) {}-{}-{}'.format(number[:2], number[2:5], number[5:8], number[8:10], number[10:])
