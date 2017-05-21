from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

from website.apps.core import views as core_views
from website.apps.stravauth.views import StravaAuth

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/password/$', core_views.password, name='password'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^stravalogin/', StravaAuth.as_view(url=reverse_lazy("home")), kwargs={"approval_prompt": "force"}, name="stravalogin"),
    # url(r'^stravalogout/$', 'django.contrib.auth.views.logout', kwargs={'next_page': '/'}, name="stravalogout"),
    url(r'^admin/', admin.site.urls),
]

# https://www.strava.com/oauth/authorize?client_id=6572&response_type=code&redirect_uri=home&approval_prompt=force&scope=write

# /stravalogin/?state=&code=b430495dcb87002a7c2cba7682e2db8f14079c19
