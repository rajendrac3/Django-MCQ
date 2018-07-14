from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import Q, Count
from django.db.models.query import QuerySet
import requests

from ..models import Course, Quiz, Question, InterviewTopic, iquestions, SubcategoriesOfTests, TestCategories, Tests, Downloads, Tests_Answers, HomeCategories
from ..forms import TakeQuizForm

sess_list = []
count_answers = 0

def home(request):
    ga = HomeCategories.objects.filter(reference_id='1')
    vr = HomeCategories.objects.filter(reference_id='2')
    all_items = {}
    all_items = {"ga_list":ga, "vr_list":vr}
    return render(request, 'newhome.html', all_items)

def home_topics(request, slug):
    print("in hometopics", slug)
    return render(request, "homequestions.html")

def examinfo(request):
    print("in examinfo")
    return render(request, 'home.html')

def practise(request):
    items = Course.objects.all()
    # print("items", items)
    # for generate_slug in items:
    #     print("in practise", generate_slug.save())
    courses_list = {}
    courses_list = {"courses_list": items}
    return render(request, 'ccat_questions/practise.html', courses_list)

def choose_course(request, slug):
    # quiz = get_object_or_404(Quiz, pk=pk)
    print("slug", slug)
    got_object = Course.objects.filter(slug=slug)
    for obj in got_object:
        print("got object", obj)
    sections = Quiz.objects.filter(course_id=obj)
    print("sections", sections)
    sections_list = {}
    sections_list = {"sections_list": sections}
    return render(request, 'ccat_questions/ccat_practise.html', sections_list)

def question_display(request, slug, section_pk):
    quiz = get_object_or_404(Quiz, pk=section_pk)
    print("section pk", section_pk)
    print("course pk")
    print("slug", slug)
    sections = Quiz.objects.all()
    courses = Course.objects.all()
    quiz_start = Question.objects.filter(quiz_id=section_pk)
    print("quiz_start", quiz_start)
    page = request.GET.get('page', 1)
    paginator = Paginator(quiz_start, 5)

    try:
        qz = paginator.page(page)
    except PageNotAnInteger:
        qz = paginator.page(1)
    except EmptyPage:
        qz = paginator.page(paginator.num_pages)

    questions_list = {}
    questions_list = {"questions_list": quiz_start }
    form = TakeQuizForm(question=quiz_start, spk=section_pk)
    return render(request, 'ccat_questions/questions.html',{
        'quiz': qz,
        'sections': sections,
        'courses': courses
        # 'form': form
    })

def answer_submit(request, q_id):
    valus = request.POST.get('q_id')
    print("from radio", q_id)
    return redirect('/')

def selected_answer(request):
    print("This is qid", request.POST['qid'])
    print("This is clicked answer", request.POST['selected_answer'])
    db = Question.objects.get(id=request.POST['qid'])
    print("db", db)
    if request.POST['selected_answer'] == str(db):
        st = {'status': 'yes'}
    else:
        st = {'status': 'no'}        
    return JsonResponse(st)

def selected_test_answer(request):
    
    db = Tests.objects.get(id=request.POST['qid'])
    print("id", request.POST['qid'])
    print("db", db)
    print("This answer is selected by user", type(request.POST['selected_answer']))
    global count_answers
    if str(db) == request.POST['selected_answer']:
        print("before print")
        count_answers = count_answers+1
        print("count", count_answers)
    
    # sess_list.append(request.POST['selected_answer'])
    # request.session['sel_ans'] = sess_list
    # print("user answer in session", request.session['sel_ans'])
    
    
    # print("del", request.session['sel_ans'])    
    # test_instance = Tests_Answers.objects.create(ques_id=request.POST['qid'], correct_answer=db, answer_by_user=request.POST['selected_answer'])
    # distinct_ids = Tests_Answers.objects.values_list('ques_id').distinct()
    # last_values = Tests_Answers.objects.filter()
    # print("last answers", distinct_ids)
    # print("last_values", last_values)

    if request.POST['selected_answer'] == str(db):
        st = {'status': 'yes'}
    else:
        st = {'status': 'no'}
    return JsonResponse(st)

def test_submitted(request):
    if request.method == 'POST':
        button_click = request.POST.get('')
        print("button_click", button_click)
    return HttpResponse("Test submitted")

def ccat_practise(request):
    return render(request, 'ccat_questions/ccat_practise.html')

def aptitude(request):
    return render(request, 'ccat_questions/home.html')

def interviewQnA(request):
    list_of_topics = InterviewTopic.objects.all()
    print("list_of_topics", list_of_topics)
    topic_list = {}
    topic_list = {"topic_list": list_of_topics}
    return render(request, 'InterviewQnA/home.html', topic_list)

def choose_interview_topic(request, slug):
    print("slug", slug)
    got_object = InterviewTopic.objects.filter(slug=slug)
    for obj in got_object:
        print("got object", obj)
    topics = iquestions.objects.filter(interviewtopic_id=obj)  
    print("topics", topics)      
    questions_list = {}
    page = request.GET.get('page', 1)
    paginator = Paginator(topics, 5)

    try:
        new_qz = paginator.page(page)
    except PageNotAnInteger:
        new_qz = paginator.page(1)
    except EmptyPage:
        new_qz = paginator.page(paginator.num_pages)

    return render(request, 'InterviewQnA/questions_page.html', {
        'questions_list': new_qz
        })

def tests(request):
    item1 = SubcategoriesOfTests.objects.filter(testcategories_id=1)
    item2 = SubcategoriesOfTests.objects.filter(testcategories_id=2)
    item1object = {}
    item1object = {'item1': item1, 'item2': item2}
    print("item1", item1)
    return render(request, 'tests/page_1.html', item1object)

def tests_topic(request, slug):
    filter_slug = SubcategoriesOfTests.objects.filter(slug=slug)
    print('filter_slug', filter_slug)
    for obj in filter_slug:
        print("got object", obj)
    filter_topics = Tests.objects.filter(sub_category_id=obj)
    print('filter_topics', filter_topics)
    test_questions = {}
    page = request.GET.get('page', 1)
    paginator = Paginator(filter_topics, 5)

    try:
        new_qz = paginator.page(page)
    except PageNotAnInteger:
        new_qz = paginator.page(1)
    except EmptyPage:
        new_qz = paginator.page(paginator.num_pages)

    return render(request, 'tests/page_2.html', {
        'questions_list': new_qz
        })

def downloads(request):
    return render(request, 'downloads/page1.html')

def email_submitted(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        exam_types = request.POST.get('exam_type')
        print("email", email)
        print("exam", exam_types)
        try:
            email_obj = Downloads.objects.create(email_id=email, exam_type=exam_types)
            print('email_obj', email_obj)
            return HttpResponse("email saved")
        except:
            return HttpResponse("You have already entered {}".format(email))

def ccat_info(request):
    return render(request, 'ccat_questions/ccat_info.html')