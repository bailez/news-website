from django.contrib import admin
from django.urls import include, path

from articles import views

urlpatterns = [
    path('articles/', views.articles),
    path('articles/<int:year>/', views.year_archive),
    path('articles/reporter/<int:report>/', views.reporter),
    path('admin/', admin.site.urls),
]
