from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
# url(r'^$', views.index), # This line has changed!
url(r'^$', views.index),
url(r'^beltreviewer$', views.index),
url(r'^books$', views.show_books),
url(r'^books/add$', views.add_books),
url(r'^book/(?P<book_id>\d+)$', views.show_book),
url(r'^book/(?P<book_id>\d+)/addreview$', views.add_review),
url(r'^user/(?P<user_id>$', views.user),

]