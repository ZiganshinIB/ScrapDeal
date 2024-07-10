from django import template
from django.db.models import Count
# from ..models import Protocol

register = template.Library()


@register.inclusion_tag('scrap/intags/sidebar.html')
def show_sidebar(active_item=None, ):
    return {'list_menu':
            [
                {'title': "Личный кабинет", 'url': '#',},
                {'title': 'Заявки', 'url': '#',},
            ],
            'active_item': active_item}

