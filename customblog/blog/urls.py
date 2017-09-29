from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import PostListView

urlpatterns = [
	url(r'^$', login_required(PostListView.as_view()), name='post_list')
]