from users.models import users
from users.serializers import UsersSerializer
from rest_framework import generics

class UsersList(generics.ListCreateAPIView):
    queryset = users.objects.all()
    serializer_class = UsersSerializer

class usersDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = users.objects.all()
    serializer_class = UsersSerializer

