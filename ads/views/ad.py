import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad, Category
from ads.serializers import AdSerializer, AdDetailSerializer
from avito import settings
from user.models import User


def root(request):
    return JsonResponse({
        "status": "ok"
    })


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.order_by('-price')
    default_serializer = AdSerializer
    serializer_classes = {
        'retrieve': AdDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        categories = request.GET.getlist('cat', [])
        if categories:
            self.queryset = self.queryset.filter(category_id__in=categories)
        text = request.GET.get('text')
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        location = request.GET.get('location')
        if location:
            self.queryset = self.queryset.filter(author__location__name__icontains=location)

        price_from = request.GET.get('price_from')
        price_to = request.GET.get('price_to')
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)

        return super().list(self, request, *args, **kwargs)


# @method_decorator(csrf_exempt, name='dispatch')
# class AdListView(ListView):
#     model = Ad
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#
#         self.object_list = self.object_list.order_by("-price")
#         categories = request.GET.getlist("cat", None)
#
#         categories_q = None
#         for calf.t_name in categories:
#             if not categories_q:
#                 categories_q = Q(category__name__contains=cat_name)
#             else:
#                 categories_q |= Q(category__name__contains=cat_name)
#         if categories_q:
#             self.object_list = self.object_list.filter(categories_q)
#
#         paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
#         page_number = request.GET.get("page")
#         page_obj = paginator.get_page(page_number)
#
#
#
#         ads = []
#         for ad in page_obj:
#             ads.append({
#                 "id": ad.id,
#                 "name": ad.name,
#                 "author": ad.author.username,
#                 "price": ad.price,
#                 "category": ad.category.name,
#                 "image": ad.image.url if ad.image else None
#             })
#
#         response = {
#             "items": ads,
#             "num_pages": paginator.num_pages,
#             "total": paginator.count
#         }
#
#         return JsonResponse(response, safe=False)
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class AdCreateView(CreateView):
#     model = Ad
#     fields = ["name", "price", "description", "is_published", "image"]
#
#     def post(self, request, *args, **kwargs):
#         ad_data = json.loads(request.body)
#         author = get_object_or_404(User, username=ad_data['author'])
#         category = get_object_or_404(Category, name=ad_data['category'])
#
#         ad = Ad.objects.create(
#             name=ad_data["name"],
#             author=author,
#             price=ad_data["price"],
#             description=ad_data["description"],
#             category=category,
#             is_published=ad_data["is_published"]
#             )
#
#         return JsonResponse({
#             "id": ad.pk,
#             "name": ad.name,
#             "author": ad.author.username,
#             "price": ad.price,
#             "description": ad.description,
#             "category": ad.category.name,
#             "is_published": ad.is_published,
#             "image": ad.image.url if ad.image else None
#         }, safe=False)
#
#
# class AdDetailView(DetailView):
#     model = Ad
#
#     def get(self, request, *args, **kwargs):
#         ad = self.get_object()
#
#         return JsonResponse({
#             "id": ad.id,
#             "name": ad.name,
#             "author": ad.author.username,
#             "price": ad.price,
#             "description": ad.description,
#             "category": ad.category.name,
#             "is_published": ad.is_published,
#             "image": ad.image.url if ad.image else None
#         })
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class AdUpdateView(UpdateView):
#     model = Ad
#     fields = ["name", "author", "price", "description", "category", "is_published", "image"]
#
#     def patch(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#         ad_data = json.loads(request.body)
#
#         if 'name' in ad_data:
#             self.object.name = ad_data["name"]
#         if 'price' in ad_data:
#             self.object.price = ad_data["price"]
#         if 'description' in ad_data:
#             self.object.description = ad_data["description"]
#         if 'is_published' in ad_data:
#             self.object.is_published = ad_data["is_published"]
#
#         self.object.save()
#
#         return JsonResponse({
#             "id": self.object.id,
#             "name": self.object.name,
#             "author": self.object.author.username,
#             "price": self.object.price,
#             "description": self.object.description,
#             "category": self.object.category.name,
#             "is_published": self.object.is_published
#         }, safe=False)
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class AdDeleteView(DeleteView):
#     model = Ad
#     success_url = '/'
#
#     def delete(self, request, *args, **kwargs):
#         super().delete(request, *args, **kwargs)
#
#         return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = ["name", "author", "price", "description", "category", "is_published", "image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES["image"]
        self.object.save()
        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author.username,
            "price": self.object.price,
            "description": self.object.description,
            "category": self.object.category.name,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None
        })
