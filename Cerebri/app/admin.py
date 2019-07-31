
from app.models import Exercise, Test
from django.contrib import admin

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass

@admin.register(Test)
class ProblemAdmin(admin.ModelAdmin):
    pass