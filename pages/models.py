from django.db import models


class MedicalCondition(models.Model):
    record_id = models.CharField(max_length=100)
    data = models.DateTimeField()
    diagnosis = models.CharField(max_length=300)
    
    
    def __str__(self):
        return self.record_id