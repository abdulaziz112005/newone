from django import template
from ..models import Category
register = template.Library()

@register.inclusion_tag('tags/menu.html')
def show_menu():
    categories = Category.objects.all()
    return {
        'categories': categories
    }
