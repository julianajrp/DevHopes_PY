from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404
import ipdb
from .serializers import UserSerializer
from .models import User
from repos.models import Repo
from repos.serializers import RepoSerializer


class UserView(APIView):
    def get(self, request: Request) -> Response:
        # QuerySet
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        # Trazer também as receitas do usuario

        return Response(serializer.data)


class UserDetailView(APIView):
    def get(self, request: Request, user_name_data: str) -> Response:
        # try:
        #     user = User.objects.get(id=user_id)
        # except User.DoesNotExist:
        #     return Response({"detail": "Not Found."}, status.HTTP_404_NOT_FOUND)

        user = get_object_or_404(User, user_name=user_name_data)
        serializer = UserSerializer(user)

        return Response(serializer.data)


class UserReposRetrieveView(APIView):
    def get(self, request: Request, user_name_data: str) -> Response:
        user = get_object_or_404(User, user_name=user_name_data)
        repos = Repo.objects.filter(user=user)
        serializer = UserSerializer(user)

        return Response(serializer.data["repos"])
