from .views import blog,about
from django.urls import path

urlpatterns = [
    path('', blog, name='blog-home'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog-home'),
]

