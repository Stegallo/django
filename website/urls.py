from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views


from website.apps.core import views as core_views

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
]
