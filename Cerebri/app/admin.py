
from app.models import Exercise, ProblemSet
from django.contrib import admin

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass

@admin.register(ProblemSet)
class ProblemAdmin(admin.ModelAdmin):
    pass