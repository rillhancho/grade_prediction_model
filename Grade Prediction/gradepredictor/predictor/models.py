from django.db import models


class Prediction(models.Model):
    socioeconomic_score = models.FloatField()
    sleep_hours = models.FloatField()
    study_hours = models.FloatField()
    attendance = models.FloatField()
    predicted_grade = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction: {self.predicted_grade} at {self.created_at}"


