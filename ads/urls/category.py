from django.urls import path

from ads.views import category

urlpatterns = [
    path('', category.CatListView.as_view()),
    path('<int:pk>/', category.CatDetailView.as_view()),
    path('create/', category.CatCreateView.as_view()),
    path('<int:pk>/update/', category.CatUpdateView.as_view()),
    path('<int:pk>/delete/', category.CatDeleteView.as_view()),
]