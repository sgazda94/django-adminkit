from django.urls import path, re_path
from .views import courses_view


urlpatterns = [

    # The home page
    path('courses/', courses_view, name='courses'),

    ]
