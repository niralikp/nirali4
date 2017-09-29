from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^create/',views.create),
    url(r'^read/',views.read),
    url(r'^delete/', views.delete),
    url(r'^update/', views.update)
]