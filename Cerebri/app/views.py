"""
Definition of views.
"""

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.template.defaulttags import register
from app.models import webpage_dict, Exercise, Test, AnswerType, AnswerDictionary
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

def test_view(request, test_url):
    test = Test.objects.get(url=test_url)
    exercise_url = test.get_first_exercise()
    return redirect('%s/%s' % (test_url, exercise_url))

def exercise_view(request, test_url, exercise_url):
    
    exercise = Exercise.objects.get(url=exercise_url)
    test = Test.objects.get(url=test_url)

    title = exercise.title
    content = exercise.content
    answers = eval(exercise.answers)
    answer_type = AnswerType(exercise.answer_type)
    next_url = test.get_next_exercise(exercise_url)

    previous_url = test.get_previous_exercise(exercise_url)
    points = exercise.points

    if points == 1: 
        points_text = "1 punkt"
    elif points in [2,3,4]:
        points_text = "%d punkty" % points
    else:
        points_text = "%d punktów" % points

    total_points = test.get_total_points()

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





@staff_member_required
def exercise_edit_view(request, test_url, exercise_url):
    
    exercise = Exercise.objects.get(url=exercise_url)
    test = Test.objects.get(url=test_url)
    
    title = exercise.title
    points = exercise.points
    content = exercise.content
    answers = eval(exercise.answers)
    answer_type = AnswerType(exercise.answer_type)
    answer_types = [(e.value, e) for e in AnswerType]

    next_url = test.get_next_exercise(exercise_url)
    previous_url = test.get_previous_exercise(exercise_url)

    if points == 1: 
        points_text = "1 punkt"
    elif points in [2,3,4]:
        points_text = "%d punkty" % points
    else:
        points_text = "%d punktów" % points

    total_points = test.get_total_points()

    context = {
        'exercise_title': title,
        'exercise_content': content,
        'exercise_answers': answers,
        'next_url': next_url,
        'previous_url': previous_url,
        'points_text': points_text,
        'exercise_points': points,
        'exercise_id': exercise,
        'total_points': total_points,
        'answer_type': answer_type,
        'answer_types': answer_types,
        'answer_dict': AnswerDictionary
               }


    return render(request, 'app/edit.html', context)