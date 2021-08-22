from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime

# User Models...
class myCustomeUser(AbstractUser):
    username = models.CharField(max_length=50, unique="True", blank=False)
    password = models.CharField(max_length=200, blank=False)
    isStudent = models.BooleanField(default=False)
    isQuestionSetter = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(myCustomeUser, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True, unique="True")
    studentID = models.IntegerField(blank=True, unique="True")

    def __str__(self):
        return self.name


class QuestionSetter(models.Model):
    user = models.OneToOneField(myCustomeUser, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True, unique="True")
    rank = models.CharField(max_length=50, blank=True)
    isVarified = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Admin(models.Model):
    user = models.OneToOneField(myCustomeUser, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True, unique="True")
    isVarified = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name



# Exam Releted models...
class QuestionNumeric(models.Model):
    question = models.TextField()
    marks = models.IntegerField()
    correctAns = models.FloatField()

    def __str__(self):
        return self.question


class QuestionTureFalse(models.Model):
    question = models.TextField()
    marks = models.IntegerField()
    correctAns = models.BooleanField()

    def __str__(self):
        return self.question


class QuestionSet(models.Model):
    examName = models.CharField(max_length=200)
    questionNumeric = models.ManyToManyField(QuestionNumeric, blank=True, null=True, related_name='rvsToQues')
    questionTureFalse = models.ManyToManyField(QuestionTureFalse, blank=True, null=True, related_name='rvsToQues')
    questionSetter = models.ForeignKey(QuestionSetter, on_delete=models.CASCADE)
    startingTime = models.DateTimeField()
    durationInMinits = models.IntegerField()
    totalMarks = models.IntegerField(default=0)
    topic = models.CharField(max_length=200)
    description = models.TextField()
    isCompleted = models.BooleanField(default=False)
    submissionTimeLimit = models.BooleanField(default=False)
    multipleSubmission = models.BooleanField(default=False)

    def __str__(self):
        return self.examName


class StudentAnsNumeric(models.Model):
    question = models.ForeignKey(QuestionNumeric, blank=True, null=True, on_delete=models.CASCADE)
    givenAns = models.IntegerField(null=True, blank=True)
    obtainedMarks = models.IntegerField(default=0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name


class StudentAnsTureFalse(models.Model):
    question = models.ForeignKey(QuestionTureFalse, blank=True, null=True, on_delete=models.CASCADE)
    givenAns = models.BooleanField(null=True, blank=True)
    obtainedMarks = models.IntegerField(default=0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name


class StudentAnsSet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    questionSet = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)
    studentAnsNumeric = models.ManyToManyField(StudentAnsNumeric, related_name='rvsToAnsSet')
    studentAnsTureFalse = models.ManyToManyField(StudentAnsTureFalse, related_name='rvsToAnsSet')
    totalObtainedMarks = models.IntegerField(default=0)
    submissionTime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.student.name


class ExamParticipent(models.Model):
    student = models.ForeignKey(Student, blank=True, null=True, on_delete=models.CASCADE)
    studentAnsSet = models.ForeignKey(StudentAnsSet, blank=True, null=True, on_delete=models.CASCADE, related_name='rvsToAnsSet')
    questionSet = models.ForeignKey(QuestionSet, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name


class Notice(models.Model):
    user = models.ForeignKey(myCustomeUser, null=True, blank=True, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200, blank=True)
    details = models.TextField(blank=True)
    postingTime = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.topic


class Resource(models.Model):
    user = models.ForeignKey(myCustomeUser, null=True, blank=True, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200, blank=True)
    details = models.TextField(blank=True)
    postingTime = models.DateTimeField(default=datetime.now, blank=True)
    link = models.TextField(blank=True)

    def __str__(self):
        return self.topic
