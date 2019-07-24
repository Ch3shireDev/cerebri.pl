"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.template.defaulttags import register
from . import Exercises, webpage_dict
import random

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def shuffle(arg):
    tmp = list(arg)[:]
    random.shuffle(tmp)
    return tmp

def home_view(request):
    return render(request, 'app/index.html')


def test_view(request, exercise):
    if exercise not in Exercises:
        return redirect('/')

    data = Exercises[exercise]
    title = data.title
    content = data.content
    answers = data.answers
    answer_type = data.answer_type
    next_url = data.next
    previous_url = data.previous
    points = data.points

    if points == 1:
        points_text = "1 punkt"
    elif points in [2,3,4]:
        points_text = "%d punkty" % points
    else:
        points_text = "%d punktów" % points

    total_points = sum(Exercises[key].points for key in Exercises)

    context = {'exercise_title': title,
               'exercise_content': content,
               'exercise_answers': answers,
               'next_url': next_url,
               'previous_url': previous_url,
               'points_text': points_text,
               'exercise_points': points,
               'exercise_id': exercise,
               'total_points': total_points
               }

    webpage = webpage_dict[str(answer_type)] #html source
    return render(request, webpage, context=context)
