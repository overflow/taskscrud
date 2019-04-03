from django.contrib.auth import views as auth_views
from django.urls import path

from tasks.models import Task
from tasks.views import TaskView


taskview = TaskView(model=Task)
urlpatterns =  [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
    ] + taskview.get_urls()
