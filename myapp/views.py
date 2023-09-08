import random
from datetime import datetime, timedelta

from django.shortcuts import render, HttpResponse
from .models import Questions


# Create your views here.
def home(request):
    categories = Questions.objects.values('category').distinct()
    return render(request, "home.html", {"categories": categories})


def start(request, category):
    categories = Questions.objects.values('category').distinct()
    return render(request, "start_quiz.html", {"category": category, "categories": categories})


def quiz(request, category=None):
    number = int(request.POST.get("number"))
    categories = Questions.objects.values('category').distinct()
    if category is not None:
        all_questions = Questions.objects.filter(category=category)
        chosen_questions = []
        while number != 0:
            rand_id = random.randint(0, len(all_questions) - 1)
            if all_questions[rand_id] not in chosen_questions:
                chosen_questions.append(all_questions[rand_id])
                number -= 1

        end_time = datetime.now() + timedelta(minutes=5)

        return render(request, "questions.html",
                      {"category": category, "questions": chosen_questions,
                       "categories": categories, "timer": end_time})


def check(request, category=None):
    categories = Questions.objects.values('category').distinct()
    if category is not None:
        questions = Questions.objects.all()
        score = 0
        question_number = 0
        answers = {}
        for question in questions:
            if request.POST.get(f'answer_{question.id}') is not None:
                answers[question] = request.POST.get(f'answer_{question.id}')
                if request.POST.get(f'answer_{question.id}').lower() == question.answer.lower():
                    score += 1
                question_number += 1
        return render(request, "answers.html", {"categories": categories, "category": category,
                                                "score": score, "answers": answers})
