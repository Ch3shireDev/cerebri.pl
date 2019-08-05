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
                path('<test_url>', views.test_view),
                path('<test_url>/edit', views.test_edit_view),
                path('<test_url>/view', views.test_edit_show),
                path('<test_url>/save', views.test_edit_save),
                path('<test_url>/<exercise_url>', views.exercise_view),
                path('<test_url>/<exercise_url>/edit', views.exercise_edit_view),
                path('<test_url>/<exercise_url>/view', views.exercise_edit_render),
                path('<test_url>/<exercise_url>/save', views.exercise_edit_save),
                path('<test_url>/<exercise_url>/remove', views.exercise_edit_remove),
                
                path('<test_url>/<exercise_url>/add-before', views.exercise_add_before),
                path('<test_url>/<exercise_url>/add-after', views.exercise_add_after),
]