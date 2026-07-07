from django.db import models

class FingguPipelineMetrics(models.Model):
    success_rate = models.FloatField()
    average_duration = models.IntegerField()
    failed_runs = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'finggu_pipeline_metrics'