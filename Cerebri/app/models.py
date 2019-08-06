"""
Definition of models.
"""

from django.db import models
from enum import Enum

class AnswerType(Enum):
    Closed = 0
    ManyValues = 1
    Proof = 2
    ListOfValues = 3
    Intervals = 4

AnswerDictionary = [
(AnswerType.Closed, '''{'answers':{'A': '2', 'B': '4', 'C': '6', 'D': '3',},'correct': 'A'}'''),
(AnswerType.Intervals, '''{'num_answers': [1, 2],'answers': [['-inf', 'left-inf', '4/3', 'right-open'],['4', 'left-open', 'inf', 'right-inf']]}'''),
(AnswerType.ListOfValues, '''[{"description": "Wartość $\\cos\\alpha$", "id": "cos-value", "value": "sqrt(5)/5"}]'''),
(AnswerType.ManyValues, '''{'num_answers': [0, 1, 2, 3, 4, 5],'answers': [5, 3, -3],}'''),
(AnswerType.Proof, '''{'steps': [{'id': '0', 'value': 'First step'},{'id': '1', 'value': 'Second step'},], 'correct_sequences': [['0','1']] }'''),
         ]

class Test(models.Model):
    url = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.TextField()
    exercises = models.TextField(default='[]')

    def __str__(self):
        return self.title

    def get_total_points(self):
        return 35

    def get_exercises(self):
        tab = eval(self.exercises)
        tab = [str(x) for x in tab]
        return tab

    def set_exercises(self, tab):
        tab = [str(x) for x in tab]
        self.exercises = str(tab)
        self.save()

    def get_next_exercise(self, url):
        tab = self.get_exercises()
        try:
            n = tab.index(url)
            if n+1<len(tab):
                return tab[n+1]
            return None
        except:
            return None

    def get_previous_exercise(self, url):
        tab = self.get_exercises()
        try:
            n = tab.index(url)
            if n-1>=0:
                return tab[n-1]
            return None
        except:
            return None

    def get_first_exercise(self):
        tab = self.get_exercises()
        if len(tab) == 0:
            return None
        url = tab[0]
        return url
    

class Exercise(models.Model):
    url = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    content = models.TextField()
    answers = models.TextField(default=AnswerDictionary[0][1])
    answer_type = models.PositiveSmallIntegerField(default=0)
    points = models.PositiveSmallIntegerField(default=1)

    def get_content(self):
        return self.content
    def get_answers(self):
        return eval(self.answers)

    def __str__(self):
        return "%s (%s)" % (self.title, self.url)

webpage_dict = {str(AnswerType.Closed): './app/exercises/closed.html',
                str(AnswerType.ManyValues): './app/exercises/many_values.html',
                str(AnswerType.Proof): './app/exercises/proof.html',
                str(AnswerType.ListOfValues): './app/exercises/list_of_values.html',
                str(AnswerType.Intervals): './app/exercises/intervals.html',
                }
