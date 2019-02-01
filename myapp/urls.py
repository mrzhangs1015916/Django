from django.conf.urls import url
import myapp.views
urlpatterns=[
    url(r'^test/getdata$',myapp.views.getData)
]