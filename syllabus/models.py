from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey('Course')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Lecture(models.Model):
    module = models.ForeignKey('Module')
    title = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DurationField()
    concepts = models.ManyToManyField('Concept', through='LectureConcept')

    def __str__(self):
        return self.title


class Assignment(models.Model):
    module = models.ForeignKey('Module')
    title = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DurationField()
    concepts = models.ManyToManyField('Concept', through='AssignmentConcept')

    def __str__(self):
        return self.title


class Quiz(models.Model):
    module = models.ForeignKey('Module')
    title = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DurationField()
    concepts = models.ManyToManyField('Concept', through='QuizConcept')

    def __str__(self):
        return self.title


class Concept(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LectureConcept(models.Model):
    lecture = models.ForeignKey('Lecture')
    concept = models.ForeignKey('Concept')


class AssignmentConcept(models.Model):
    assignment = models.ForeignKey('Assignment')
    concept = models.ForeignKey('Concept')


class QuizConcept(models.Model):
    quiz = models.ForeignKey('Quiz')
    concept = models.ForeignKey('Concept')
