from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

class Test(models.Model):
    name = models.CharField(max_length=100)
    max_score = models.IntegerField()

class TestResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
