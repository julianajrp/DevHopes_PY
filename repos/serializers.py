from rest_framework import serializers


class RepoSerializer(serializers.Serializer):
    repo_title = serializers.CharField(max_length=50)
    repo_desc = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
