from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='render_menu_item')
def render_menu_item(menu_item, level=0):
    if menu_item.children:
        if level == 0:
            template = """
            <li class="dropdown dropdown-hover">
                <a class="target-offset target-offset dropdown-toggle" href="{}" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" data-submenu="" tabindex="0">
                    <span class="label-text">{}</span>
                    <span class="label-dropdown-toggle fal fa-angle-down"></span>
                </a>
                <a class="dropdown-toggle-mobile" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"><span class="dropdown-toggle-mobile-icon fal fa-chevron-square-down fa-2x"></span></a>
                <ul class="dropdown-menu" role="menu">
                    {}
                </ul>
            </li>"""
        else:
            template = """
            <li class="dropdown dropdown-hover dropdown-submenu">
                <a class="target-offset" href="{}" tabindex="0">
                    <span class="label-text">{}</span>
                    <span class="label-dropdown-toggle fal fa-angle-right"></span>
                </a>
                <a class="dropdown-toggle-mobile" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"><span class="dropdown-toggle-mobile-icon fal fa-chevron-square-down fa-2x"></span></a>
                <ul class="dropdown-menu" role="menu">
                    {}
                </ul>
            </li>"""
        return mark_safe(template.format(menu_item.url, menu_item.text, "".join([render_menu_item(item, level+1) for item in menu_item.children])))
    else:
        template = """
                    <li class="">
                        <a class="target-offset" href="{}" tabindex="0">
                            <span class="label-text">{}</span>
                        </a>
                    </li>"""
        return mark_safe(template.format(menu_item.url, menu_item.text))