from django.urls import path, include
from .views import taskview, taskdetail, taskadd, taskdelete, taskupdate, taskcomplete, registration
urlpatterns = [
    path("",taskview.as_view(),name="tasks"),
    path("task/<int:pk>",taskdetail.as_view(),name = "task-detail"),
    path("task-delete/<int:pk>", taskdelete.as_view(), name="task-delete"),
    path("task-update/<int:pk>", taskupdate.as_view(), name="task-update"),
    path("task-complete/<int:pk>", taskcomplete.as_view(), name="task-complete"),
    path('login/', include("django.contrib.auth.urls")),
    path("add-task",taskadd.as_view(),name="task-add"),
    path("register/",registration.as_view(),name="register"),

]
