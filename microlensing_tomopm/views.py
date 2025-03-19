from django.views.generic import TemplateView
from custom_code.models import MicrolensingTarget


class PriorityManagementView(TemplateView):
    template_name = 'priority_management.html'

    def get_context_data(self, **kwargs):
        return {'targets': MicrolensingTarget.objects.all()}