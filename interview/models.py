from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class QuestionAnswer(models.Model):
    question = models.CharField(max_length=255)
    short_answer = models.CharField(max_length=255)
    answer = models.TextField(null=True)
    importance = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
