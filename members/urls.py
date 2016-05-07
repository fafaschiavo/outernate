from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new-member/$', views.new_member, name='new_member'),
    url(r'^include-new-member/$', views.include_new_member, name='include_new_member'),
]