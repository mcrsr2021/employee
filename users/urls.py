from django.urls import path
from users.views import UsersList,usersDetails

urlpatterns = [
    path('users/',UsersList.as_view()),
    path('users/<int:pk>/',usersDetails.as_view()),
]