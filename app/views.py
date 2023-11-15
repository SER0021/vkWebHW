from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

QUESTIONS = [
        {
            'id': i,
            'title': f'Question {i}',
            'content': f'Long lorem ipsum {i}'
        } for i in range(10)
    ]
TAGS = [
    {
        'title': 'Python',
    },
    {
        'title': 'CSS',
    },
    {
        'title': 'Django',
    },
    {
        'title': 'VK',
    },
    {
        'title': 'Swift',
    }
]

def paginate(objects, page, per_page=3):
    paginator = Paginator(objects, per_page)
    try:
        paginated_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        paginated_objects = paginator.page(paginator.num_pages)
    return paginated_objects


def render_paginated(request, template_name, data):
    page = request.GET.get('page', 1)
    paginated_data = paginate(data, page)
    return render(request, template_name, {'questions': paginated_data})

def index(request):
    page = request.GET.get('page', 1)
    return render(request, 'index.html', {'questions': paginate(QUESTIONS, page)})

def hot(request):
    page = request.GET.get('page', 1)
    return render(request, 'hot.html', {'questions': paginate(QUESTIONS, page)})

def question(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, 'question.html', {'question': item})

def ask(request):
    return render(request, 'ask.html')

def tag(request, tag_title):
    item = next((tag for tag in TAGS if tag['title'] == tag_title), None)
    page = request.GET.get('page', 1)
    return render(request, 'tag.html', {'tag': item, 'questions': paginate(QUESTIONS, page)})

def setting(request):
    return render(request, 'setting.html')

def singup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

