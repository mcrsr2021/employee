from rest_framework import serializers
from users.models import users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['id','userid','username','email','salary','created','updated']
