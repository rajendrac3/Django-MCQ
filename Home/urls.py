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
    path('examinfo', home.examinfo, name='examinfo'),
    path('InterviewQnA', home.interviewQnA, name='interviewQnA'),
    path('downloads', home.downloads, name='downloads'),
    path('email_submitted', home.email_submitted, name='email_submitted'),
    path('ccat_info', home.ccat_info, name='ccat_info'),
    path('tests/<slug:slug>', home.tests_topic, name='tests_topic'),
    path('answer', home.selected_answer, name='selected_answer'),
    path('test_answer', home.selected_test_answer, name='selected_test_answer'),
    path('test_submitted', home.test_submitted, name='test_submitted'),
    path('InterviewQnA/<slug:slug>', home.choose_interview_topic, name='choose_interview_topic'),
    path('<slug:slug>', home.home_topics, name='home_topics')
]