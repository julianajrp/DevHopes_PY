from rest_framework import serializers
from repos.serializers import RepoSerializer


class UserSerializer(serializers.Serializer):
    # write_only
    id = serializers.IntegerField(read_only=True)
    user_name = serializers.CharField(max_length=50)
    real_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    description = serializers.CharField()

    repos = RepoSerializer(many=True, read_only=True)
