from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class IELTS(models.Model):
    user = models.OneToOneField('custom_auth.User', on_delete=models.CASCADE, null=True, blank=True)

    listening = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    reading = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    writing = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    speaking = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(9)])


class Duolingo(models.Model):
    user = models.OneToOneField('custom_auth.User', on_delete=models.CASCADE)

    literacy = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(160)])
    conversation = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(160)])
    comprehension = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(160)])
    production = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(160)])

    def __str__(self):
        return str(self.user)


class TOEFL(models.Model):
    user = models.OneToOneField('custom_auth.User', on_delete=models.CASCADE)

    reading = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    listening = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    speaking = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    writing = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])


class CEFR(models.Model):
    user = models.OneToOneField('custom_auth.User', on_delete=models.CASCADE)

    listening = models.CharField(max_length=10)
    reading = models.CharField(max_length=10)
    writing = models.CharField(max_length=10)
    speaking = models.CharField(max_length=10)

