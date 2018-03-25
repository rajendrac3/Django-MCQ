from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url

from .views import home

urlpatterns = [
    path('', home.home, name='home'),

    path('practise/', home.practise, name = 'practise'),
    path('practise/<slug:slug>/', home.choose_course, name='choose_course'),
    # path('practise/<int:course_pk>/<int:quiz_pk>', home.start_practise, name='start_practise'),
    path('practise/<slug:slug>/<int:section_pk>', home.question_display, name='question_display'),
    path('practise/answer_submit/<int:q_id>', home.answer_submit, name='answer_submit'),
    path('tests', home.tests, name='tests'),
    path('answer', home.selected_answer, name='selected_answer')
    # path('ccat_practise', home.ccat_practise, name = 'ccat_practise'),
    # path('aptitude', home.aptitude, name = 'aptitude'),

]