import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from user.models import User, Location
from avito import settings
from user.serializers import LocationSerializer, UserCreateSerializer, UserSerializer
from rest_framework import viewsets


# @method_decorator(csrf_exempt, name='dispatch')
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # model = User
    # def get(self, request, *args, **kwargs):
    #     super().get(request, *args, **kwargs)
    #
    #     paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
    #     page_number = request.GET.get("page")
    #     page_obj = paginator.get_page(page_number)
    #
    #     users = []
    #     for user in page_obj:
    #         users.append({
    #             "id": user.id,
    #             "username": user.username,
    #             "first_name": user.first_name,
    #             "last_name": user.last_name,
    #             "role": user.role,
    #             "age": user.age,
    #             "locations": list(user.location.all().values_list("name", flat=True)),
    #             'total_ads': user.ads.filter(is_published=True).count()
    #         })
    #
    #     response = {
    #         "items": users,
    #         "num_pages": paginator.num_pages,
    #         "total": paginator.count
    #     }
    #
    #     return JsonResponse(response, safe=False)


# @method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    # model = User
    # fields = ["username", "first_name", "last_name", "password", "role", "age", "location"]
    #
    # def post(self, request, *args, **kwargs):
    #     user_data = json.loads(request.body)
    #
    #     user = User.objects.create(
    #         username=user_data["username"],
    #         password=user_data["password"],
    #         first_name=user_data["first_name"],
    #         last_name=user_data["last_name"],
    #         role=user_data["role"],
    #         age=user_data["age"]
    #     )
    #     if 'locations' in user_data:
    #         for loc_name in user_data["locations"]:
    #             loc, _ = Location.objects.get_or_create(name=loc_name)
    #             user.location.add(loc)
    #
    #     return JsonResponse({
    #             "id": user.id,
    #             "username": user.username,
    #             "first_name": user.first_name,
    #             "last_name": user.last_name,
    #             "role": user.role,
    #             "age": user.age,
    #             "locations": list(user.location.all().values_list("name", flat=True)),
    #             'total_ads': user.ads.filter(is_published=True).count()
    #         })


# @method_decorator(csrf_exempt, name='dispatch')
class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # model = User
    #
    # def get(self, request, *args, **kwargs):
    #     user = self.get_object()
    #
    #     return JsonResponse({
    #         "id": user.pk,
    #         "username": user.username,
    #         "first_name": user.first_name,
    #         "last_name": user.last_name,
    #         "role": user.role,
    #         "age": user.age,
    #         "locations": list(user.location.all().values_list("name", flat=True)),
    #         "total_ads": user.ads.filter(is_published=True).count()
    #     }, safe=False)


#
# @method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # model = User
    # fields = ["username", "first_name", "last_name", "password", "role", "age", "location"]
    #
    # def patch(self, request, *args, **kwargs):
    #     super().post(request, *args, **kwargs)
    #     user_data = json.loads(request.body)
    #     if 'username' in user_data:
    #         self.object.username = user_data["username"]
    #     if 'first_name' in user_data:
    #         self.object.first_name = user_data["first_name"]
    #     if 'last_name' in user_data:
    #         self.object.last_name = user_data["last_name"]
    #     if 'password' in user_data:
    #         self.object.password = user_data["password"]
    #     if 'age' in user_data:
    #         self.object.age = user_data["age"]
    #     if 'locations' in user_data:
    #         for loc_name in user_data["locations"]:
    #             loc, _ = Location.objects.get_or_create(name=loc_name)
    #             self.object.location.add(loc)
    #     self.object.save()
    #
    #     return JsonResponse({
    #         "id": self.object.pk,
    #         "username": self.object.username,
    #         "first_name": self.object.first_name,
    #         "last_name": self.object.last_name,
    #         "role": self.object.role,
    #         "age": self.object.age,
    #         "locations": list(self.object.location.all().values_list("name", flat=True)),
    #         "total_ads": self.object.ads.filter(is_published=True).count()
    #     }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # model = User
    # success_url = '/'
    #
    # def delete(self, request, *args, **kwargs):
    #     super().delete(request, *args, **kwargs)
    #
    #     return JsonResponse({"status": "ok"}, status=200)


# views.py




class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


