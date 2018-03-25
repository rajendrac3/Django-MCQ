from django.db import models
from skimage.util import unique
from uuslug import uuslug
from django.utils.text import slugify


# Create your models here.

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
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.correct_answer

class Answer(models.Model):
    text = models.CharField('Answer', max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text
