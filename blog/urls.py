from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.detil_blog, name="detil_blog"),
    path("<kategori>/", views.kategori_blog, name="kategori_blog"),
]
