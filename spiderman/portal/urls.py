from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^manage/', views.manage, name='manageHome'),
]
