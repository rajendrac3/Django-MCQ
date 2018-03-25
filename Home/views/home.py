from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import Q

from ..models import Course, Quiz, Question, Answer
from ..forms import TakeQuizForm

def home(request):
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


def tests(request):
    aps = Question.objects.filter(quiz_id=1).values('category').distinct()
    items = Question.objects.filter(Q(quiz_id=2) | Q(quiz_id=3)).values('category').distinct()
    print("items", items)
    courses_list = {}
    courses_list = {"items": items, "aps": aps}
    return render(request, 'tests/page_1.html', courses_list)

def apt_category(request, pk):
    print("pk = ", pk)
    return render(request, 'tests/page_2.html')

def ccat_practise(request):
    return render(request, 'ccat_questions/ccat_practise.html')

def aptitude(request):
    return render(request, 'ccat_questions/home.html')