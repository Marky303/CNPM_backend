from django.core.serializers import serialize
import json
def to_json(queryset):
    return json.loads(serialize('json', queryset))