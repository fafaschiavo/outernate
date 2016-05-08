from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new-member/$', views.new_member, name='new_member'),
    url(r'^include-new-member/$', views.include_new_member, name='include_new_member'),
    url(r'^upload-img/$', views.upload_img, name='upload_img'),
    url(r'^upload-img-success/(?P<img_hash>\w{10})/', views.upload_img_success, name='upload_img_success'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^verify-username/', views.verify_username, name='verify_username'),
]