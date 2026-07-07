from django.views.generic import TemplateView

class FingguDashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['metrics'] = self.get_pipeline_metrics()
        return context

    def get_pipeline_metrics(self):
        # Simulate fetching pipeline metrics
        return {
            'success_rate': 95,
            'average_duration': 120,
            'failed_runs': 2
        }