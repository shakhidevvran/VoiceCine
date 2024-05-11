from django.urls import path
from apps.chat.views import *


urlpatterns = [
    path('', GPTResponseApiView.as_view()),
]