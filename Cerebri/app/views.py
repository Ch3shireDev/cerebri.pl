"""
Definition of views.
"""

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.template.defaulttags import register
from app.models import webpage_dict, Exercise, Test, AnswerType, AnswerDictionary
from django.http import HttpResponse, JsonResponse
import random
import re

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def shuffle(arg):
    if arg==None:
        return []
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

    answers = exercise.answers
    answers = re.sub(r'(?<!\\)\\(?<!\\)', '\\\\', answers)

    try:
        answers = eval(answers)
    except:
        answers = None
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
    try:
        answers = eval(exercise.answers)
    except:
        answers = ""
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
    try:
        answers = eval(answers)
    except:
        answers = ""
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

    print(content)

    try:
        points = int(points)
    except:
        points = 0

    exercise = Exercise.objects.get(url=exercise_url)

    exercise.title = title
    exercise.content = content
    exercise.answer_type = int(answer_type)

    answers = re.sub(r'(?<!\\)\\(?<!\\)', r'\\\\', answers)
    
    exercise.answers = answers
    exercise.points = points

    exercise.save()

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
    test = Test.objects.get(url=test_url)
    exercises = test.get_exercises()
    if exercise_url not in exercises:
        return HttpResponse(status=500)
    index = exercises.index(exercise_url)
    title = "Zadanie %d" % (index+2)
    exercise = Exercise.objects.create(title=title)
    exercise.save()
    exercises.insert(index+1, str(exercise.url))
    test.set_exercises(exercises)
    test.save()
    return redirect('/%s/%s/edit' % (test_url, exercise.url))

@staff_member_required
def exercise_edit_remove(request, test_url, exercise_url):
    url = ''
    try:
        test = Test.objects.get(url=test_url)
    except:
        return HttpResponse(status=500)

    tab = test.get_exercises()
    if exercise_url not in tab:
        return HttpResponse(status=500)

    try:
        exercise = Exercise.objects.get(url=exercise_url)
    except:
        tab.remove(exercise_url)
        test.set_exercises(tab)
        test.save()
        return HttpResponse(status=500)
    
    exercise.delete()

    index = tab.index(exercise_url)

    tab.remove(exercise_url)
    test.set_exercises(tab)
    test.save()

    if index >= len(tab):
        url = tab[-1]
    else:
        url = tab[index]
    return JsonResponse({'url': '/%s/%s' %(test_url, url)}, status=200)

import os
from tempfile import mkdtemp
from django.conf import settings
from django.core.files.storage import FileSystemStorage

@staff_member_required
def add_test(request):
    if request.method == 'POST':
        num = request.POST['filesNum']
        files = request.FILES
        n = 1
        folder = mkdtemp(dir=settings.MEDIA_ROOT)
        dirname = folder.replace('\\', '/')
        
        for key in files:

            myfile = request.FILES[key]
            fs = FileSystemStorage(location=dirname)
            filename = fs.save(myfile.name, myfile)
            file_url = fs.url(filename)
        request.session['filesdir'] = dirname

        title = request.POST['title']
        description = request.POST['description']
        
        test = Test.objects.create(title=title, description=description)
        test.save()
        return JsonResponse({'test_url': test.url}, status=200)
    else:
        return render(request, 'app/add_test.html')

@staff_member_required
def edit_test(request, test_url):

    if request.method == 'POST':

        return HttpResponse(status=200)

    from PIL import Image
    from pytesseract import pytesseract, image_to_string

    pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    
    exercises = []
    n = 1
    
    filesdir = request.session.get('filesdir')
    fname = filesdir.split('/')[-1]

    for file in os.listdir(filesdir):
        filename = filesdir+"/"+file
        text = image_to_string(Image.open(filename), lang="pol")
        url = '/media/%s/%s' % (fname, file)
        exercise = {'title': 'Zadanie %d' % n, 'content': text, 'url': url, 'number': n-1}
        exercises.append(exercise)
        n+=1
    return render(request, 'app/edit_test2.html', context={'exercises': exercises})

@staff_member_required
def add_exercise(request,test_url):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        url = request.POST['url']
        test = Test.objects.get(url=test_url)

        content = "<img src='%s' class='mx-auto d-block'/>\n\n%s" % (url, content)

        exercise = Exercise.objects.create(title=title, content=content)
        exercise.save()

        tab = test.get_exercises()
        tab += [exercise.url]
        test.set_exercises(tab)
        test.save()

        return HttpResponse(status=200)

    return HttpResponse(status=500)

@staff_member_required
def test_edit_delete(request, test_url):
    if request.method != 'POST':
        return HttpResponse(status=500)

    test = Test.objects.get(url=test_url)
    tab = test.get_exercises()

    test.delete()

    for exercise_url in tab:
        exercise = Exercise.objects.get(url=exercise_url)
        exercise.delete()

    return HttpResponse(status=200)

@staff_member_required
def test_append(request, test_url):
    test = Test.objects.get(url=test_url)
    tab = test.get_exercises()
    title = "Zadanie %d" % (len(tab)+1)
    exercise = Exercise.objects.create(title=title)
    exercise.save()
    tab.append(str(exercise.url))
    test.set_exercises(tab)
    test.save()
    return redirect('/%s/%s/edit' % (test_url, exercise.url))