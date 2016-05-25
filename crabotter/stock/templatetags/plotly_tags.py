from django import template
import plotly.tools as tls

register = template.Library()

@register.simple_tag
def plotly_embed(url):
    return tls.get_embed(url)