from django.contrib import admin
from django.urls import include, path

from register import views as regviews
from articles import views

urlpatterns = [
    path('',views.home, name='home'),
    path('articles/', views.articles, name = 'articles'),
    path('articles/<int:year>/', views.year_archive),
    path('articles/reporter/<int:report>/', views.reporter),
    path('register/', regviews.register, name='register'),
    path('admin/', admin.site.urls),
    path('',include('django.contrib.auth.urls')),
]
