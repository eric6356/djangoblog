from django import template

register = template.Library()

@register.simple_tag
def active_page(request, path):
    from django.core.urlresolvers import resolve, Resolver404
    if not request:
        return ""
    try:
        return "active" if request.path.startswith(path) else ""
    except Resolver404:
        return ""