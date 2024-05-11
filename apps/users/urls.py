from django.urls import path, include
from .views import *
# from apps.password.views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('chat/', include('apps.chat.urls')),
    # path('send_email/', SendEmailView.as_view()),
    # path('reset_password/', PasswordResetConfirmView.as_view())
]
