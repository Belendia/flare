from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'test',views.SampleOne.as_view(), name='simple_url')
]
