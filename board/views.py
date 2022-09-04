from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'board/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'board/question_detail.html', context)


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    subject = request.POST.get('subject')
    content = request.POST.get('content')
    create_date = timezone.now()

    question.answer_set.create(
        subject=subject, content=content, create_date=create_date)
    return redirect('board:detail', question_id=question.id)
