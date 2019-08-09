"""
Definition of urls for system.
"""

from django.urls import path
from django.contrib import admin
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [                  
                path('', views.home_view),
                path('admin', admin.site.urls),


              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
                  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
                #path('admin/', admin.site.urls),
                path('add_course', views.add_course),
                path('add_course2', views.add_course2),
                
                path('<course_url>', views.course_view),
                path('<course_url>/', views.course_view),

                path('<course_url>/edit_course', views.edit_course),
                path('<course_url>/add_exercise', views.add_exercise),
                path('<course_url>/add-exercises', views.add_exercises),

                path('<course_url>/edit', views.course_edit_view),
                path('<course_url>/view', views.course_edit_show),
                path('<course_url>/save', views.course_edit_save),
                path('<course_url>/delete', views.course_edit_delete),
                path('<course_url>/append', views.course_append),

                path('<course_url>/<exercise_url>', views.exercise_view),
                path('<course_url>/<exercise_url>/edit', views.exercise_edit_view),
                path('<course_url>/<exercise_url>/view', views.exercise_edit_render),
                path('<course_url>/<exercise_url>/save', views.exercise_edit_save),
                path('<course_url>/<exercise_url>/remove', views.exercise_edit_remove),
                
                path('<course_url>/<exercise_url>/add-before', views.exercise_add_before),
                path('<course_url>/<exercise_url>/add-after', views.exercise_add_after),
]