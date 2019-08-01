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
                  path('<test_url>', views.test_view),
                  path('<test_url>/<exercise_url>', views.exercise_view),
                  path('<test_url>/<exercise_url>/edit', views.exercise_edit_view),
                  path('<test_url>/<exercise_url>/render', views.exercise_edit_render),
                  path('admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
                