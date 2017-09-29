from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm
# Create your views here.

class ProfileDetailView(UpdateView):
    template_name = 'user_profile/profile.html'
    form_class = ProfileForm
    
    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user.pk)

