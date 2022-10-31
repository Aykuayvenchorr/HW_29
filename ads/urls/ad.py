from django.urls import path

from ads.views import ad

urlpatterns = [
    path('<int:pk>/upload_image/', ad.AdImageView.as_view()),
]