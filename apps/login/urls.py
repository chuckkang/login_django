from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
# url(r'^$', views.index), # This line has changed!
url(r'^$', views.index),
url(r'^login$', views.login),
url(r'^register$', views.register),
url(r'^logout$', views.logout),
url(r'^success$', views.success)
]