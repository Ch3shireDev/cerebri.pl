"""
Definition of views.
"""

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.template.defaulttags import register
from app.models import webpage_dict, Exercise, Test, AnswerType, AnswerDictionary
from django.http import HttpResponse
import random
import json

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def shuffle(arg):
    tmp = list(arg)[:]
    random.shuffle(tmp)
    return tmp

def home_view(request):
    tests = Test.objects.all()
    return render(request, 'app/index.html', context={'tests': tests})

def test_view(request, test_url):
    test = Test.objects.get(url=test_url)
    exercise_url = test.get_first_exercise()
    return redirect('%s/%s' % (test_url, exercise_url))

def exercise_render(request,title, content, answers,answer_type,test_url=None,exercise_url=None,next_url=None,previous_url=None,points=None,total_points=None):
   
    
    if points is not None:
        if points == 1: 
            points_text = "1 punkt"
        elif points in [2,3,4]:
            points_text = "%d punkty" % points
        else:
            points_text = "%d punktów" % points
    else:
        points_text=None

        
    context = {'exercise_title': title,
               'exercise_content': content,
               'exercise_answers': answers,
               'next_url': next_url,
               'previous_url': previous_url,
               'points_text': points_text,
               'exercise_points': points,
               'exercise_url': exercise_url,
               'total_points': total_points,
               'test_url': test_url,
               'exercise_url': exercise_url,
               }

    webpage = webpage_dict[str(answer_type)] #html source
    return render(request, webpage, context=context)

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
    total_points = test.get_total_points()

    return exercise_render(request,title,content,answers,answer_type,test_url, exercise_url,next_url,previous_url,points,total_points)





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
        'exercise_url': exercise_url,
        'test_url': test_url,
        'total_points': total_points,
        'answer_type': answer_type,
        'answer_types': answer_types,
        'answer_dict': AnswerDictionary
               }


    return render(request, 'app/edit_exercise.html', context)

@staff_member_required
def exercise_edit_render(request, test_url, exercise_url):
    if request.method != 'POST':
        return HttpResponse(status=500)

    title = request.POST['title']
    content = request.POST['content']
    answer_type = request.POST['answer_type']
    answers = request.POST['answers']
    answers = eval(answers)

    answer_type = AnswerType(int(answer_type))
    return exercise_render(request,title,content,answers,answer_type)

@staff_member_required
def exercise_edit_save(request,test_url,exercise_url):
    if request.method != 'POST':
        return HttpResponse(status=500)

    title = request.POST['title']
    content = request.POST['content']
    answer_type = request.POST['answer_type']
    answers = request.POST['answers']
    points = request.POST['points']

    try:
        points = int(points)
    except:
        points = 0

    exercise = Exercise.objects.get(url=exercise_url)

    exercise.title = title
    exercise.content = content
    exercise.answer_type = int(answer_type)
    exercise.answers = answers
    exercise.points = points

    return HttpResponse(status=200)

@staff_member_required
def test_edit_view(request, test_url):
    test = Test.objects.get(url=test_url)
    return render(request, 'app/edit_test.html', {'test':test, 'test_url':test_url })

@staff_member_required
def test_edit_show(request, test_url):
    return HttpResponse(status=200)

@staff_member_required
def test_edit_save(request,test_url):
    return HttpResponse(status=200)

@staff_member_required
def exercise_add_before(request, test_url, exercise_url):

    return HttpResponse(status=200)

@staff_member_required
def exercise_add_after(request,test_url, exercise_url):
    return HttpResponse(status=200)