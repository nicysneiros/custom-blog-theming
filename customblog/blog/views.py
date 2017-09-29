from django.views.generic import ListView
from .models import Post

# Create your views here.
class PostListView(ListView):
	template_name = 'blog/post_list.html'

	def get_queryset(self):
		return Post.objects.filter(author=self.request.user)