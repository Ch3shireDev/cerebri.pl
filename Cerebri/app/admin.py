
from app.models import Exercise, Course
from django.contrib import admin

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class ProblemAdmin(admin.ModelAdmin):
    pass