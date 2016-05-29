from django import template
from django.utils.safestring import mark_safe
import plotly.tools as tls

register = template.Library()

@register.simple_tag()
def plotly_embed(url):
    # TODO: Re-implement get_embed to use the template system. get_embed should be safe, but using
    # mark_safe is always a vulnerability.

    return mark_safe(tls.get_embed(url))