from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    NID = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


# new models
class questionNumeric(models.Model):
    question = models.TextField()
    marks = models.IntegerField()
    correctAns = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class questionTureFalse(models.Model):
    question = models.TextField()
    marks = models.IntegerField()
    correctAns = models.BooleanField()

    def __str__(self):
        return self.question


class questionSet(models.Model):
    examName = models.CharField(max_length=200)
    questionNumeric = models.ManyToManyField(questionNumeric)
    questionTureFalse = models.ManyToManyField(questionTureFalse)
    noNumeric = models.IntegerField(default=0)
    noTureFalse = models.IntegerField(default=0)
    questionSetter = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    startingTime = models.DateTimeField()
    durationInMinits = models.IntegerField()
    totalMarks = models.IntegerField(default=0)

    def __str__(self):
        return self.examName


class studentAnsNumeric(models.Model):
    question = models.ManyToManyField(questionNumeric)
    givenAns = models.IntegerField(null=True, blank=True)
    obtainedMarks = models.IntegerField(null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student


class studentAnsTureFalse(models.Model):
    question = models.ManyToManyField(questionTureFalse)
    givenAns = models.BooleanField(null=True, blank=True)
    obtainedMarks = models.IntegerField(null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student


class studentAnsSet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    questionSet = models.ForeignKey(questionSet, on_delete=models.CASCADE)
    studentAnsNumeric = models.ManyToManyField(studentAnsNumeric)
    studentAnsTureFalse = models.ManyToManyField(studentAnsTureFalse)
    totalObtainedMarks = models.IntegerField()
    submissionTime = models.DateTimeField()

    def __str__(self):
        return self.student


class examParticipent(models.Model):
    exam = models.ForeignKey(questionSet, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.student
