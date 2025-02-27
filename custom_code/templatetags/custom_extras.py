import json
from django import template
from tom_dataproducts.models import ReducedDatum

register = template.Library()

@register.inclusion_tag('custom_code/partials/classification_data.html')
def recent_classification(target, num_points=1):
    classification = ReducedDatum.objects.filter(data_type='classification').order_by('-timestamp')[:num_points]
    return {'recent_classification': [(datum.timestamp, json.loads(datum.value)['magnitude']) for datum in classification]}


