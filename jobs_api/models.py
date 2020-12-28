from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

# Create your models here.

class Jobs(models.Model):
    job = models.CharField(max_length=50)
    qualifications = models.CharField(max_length=50)
    experience = models.IntegerField()
    reporting_to = models.CharField(max_length=50)
    added_date = models.DateTimeField(max_length=32, auto_now_add=True) # this is when user add the record. then tracing activity

    #   By default Django model (Table) appended with "s". it self show Admin form  Plural Eg jobss therefore  set the job
    def __str__(self):
        return self.job

    class Meta:
        verbose_name_plural = "Jobs"

class Work_record(models.Model):
    #    "on_delete=models.CASCADE"If Candidate NAME Delete Work_record also delete Automatically
    positon = models.CharField(max_length=50)
    workplace = models.CharField(max_length=50)
    start = models.DateField(auto_now=False, auto_now_add=False, max_length=65)
    end = models.DateField(auto_now=False, auto_now_add=False, max_length=65)
    added_date = models.DateTimeField(max_length=32, auto_now_add=True)

    def __str__(self):
        return self.positon

    class Meta:
        verbose_name_plural = "Work_history"


class Candidates(models.Model):
    name = models.CharField(max_length=50)
    work_record = models.ManyToManyField(Work_record, related_name="position") #models.ForeignKey(Work_record, on_delete=models.CASCADE)
    apply_for = models.ManyToManyField(Jobs, related_name='Jobs')
    added_date = models.DateTimeField(max_length=32, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Candidates"

class questionnaire(models.Model):
    candidate = models.ForeignKey(Candidates,on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    answer = models.TextField(max_length=350)
    mark = models.IntegerField()
    added_date = models.DateTimeField(max_length=32, auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "questionnaire"