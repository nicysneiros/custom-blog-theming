from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import ProfileDetailView

urlpatterns = [
	url(r'^login/$', auth_views.login, {'template_name': 'user_profile/login.html'}, name='user_login'),
	url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^profile/$', login_required(ProfileDetailView.as_view()), name='user_profile')
]