from django.shortcuts import render
from django.core.paginator import Paginator


QUESTIONS = [
        {
            'id': i,
            'title': f'Question {i}',
            'content': f'Long lorem ipsum {i}'
        } for i in range(10)
    ]

def paginate(objects, page, per_page=3):
    paginator = Paginator(objects, per_page)
    return paginator.page(page)

def index(request):
    page = request.GET.get('page', 1)
    return render(request, 'index.html', {'questions': paginate(QUESTIONS, page)})


def question(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, 'question.html', {'question': item})
