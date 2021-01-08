from django import template

register = template.Library()

@register.inclusion_tag('tags/menu.html')
def show_menu():
    pass
