from django.test import TestCase
from .models import FingguPipelineMetrics


class FingguPipelineMetricsTest(TestCase):
    def setUp(self):
        FingguPipelineMetrics.objects.create(success_rate=90.0, average_duration=150, failed_runs=1)

    def test_metrics_creation(self):
        metrics = FingguPipelineMetrics.objects.get(id=1)
        self.assertEqual(metrics.success_rate, 90.0)
        self.assertEqual(metrics.average_duration, 150)
        self.assertEqual(metrics.failed_runs, 1)