from django.db import models
from skimage.util import unique
from uuslug import uuslug
from django.utils.text import slugify
from unittest.util import _MAX_LENGTH
from bokeh.themes import default


# Create your models here.

class HomeCategories(models.Model):
    name = models.CharField(max_length=30)
    reference_id = models.CharField(max_length=5)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return str(self.name)


class Course(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return str(self.id)
        

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Course, self).save(*args, **kwargs)

class Quiz(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     self.slug = uuslug(self.name, instance=self)
    #     super(Quiz, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super(Quiz, self).save(*args, **kwargs)

class Question(models.Model):
    text = models.CharField('Question', max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    answer_1 = models.CharField(max_length=1000)
    answer_2 = models.CharField(max_length=1000)
    answer_3 = models.CharField(max_length=1000)
    answer_4 = models.CharField(max_length=1000)
    correct_answer = models.CharField(max_length=1000)
    category = models.CharField('Category', max_length=50)

    def __str__(self):
        return self.correct_answer

class Answer(models.Model):
    text = models.CharField('Answer', max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class InterviewTopic(models.Model):
    text = models.CharField('InterviewTopic', max_length=250)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return str(self.id)

class iquestions(models.Model):
    question = models.CharField('iquestions', max_length=1000)
    answer = models.CharField('iquestions', max_length=10000)
    interviewtopic = models.ForeignKey(InterviewTopic, on_delete=models.CASCADE, related_name='qna')

    def __str__(self):
        return self.question

class TestCategories(models.Model):
    topic = models.CharField(max_length=100, default="sv")
    slug = models.SlugField(blank=True)

class SubcategoriesOfTests(models.Model):
    Subcategories = models.CharField(max_length=100)
    testcategories = models.ForeignKey(TestCategories, on_delete=models.CASCADE, related_name='cst')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return str(self.id)

class Tests(models.Model):
    question = models.CharField(max_length=500)
    answer_1 = models.CharField(max_length=1000, default='avd')
    answer_2 = models.CharField(max_length=1000, default='avdv')
    answer_3 = models.CharField(max_length=1000, default='avdsdc')
    answer_4 = models.CharField(max_length=1000, default='avdedfcfws')
    correct_answer = models.CharField(max_length=1000, default='avqfed')
    sub_category = models.ForeignKey(SubcategoriesOfTests, on_delete=models.CASCADE, related_name='cstx')
    
    def __str__(self):
        return self.correct_answer

class Downloads(models.Model):
    email_id = models.CharField(max_length=50, unique=True)
    exam_type = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.email_id