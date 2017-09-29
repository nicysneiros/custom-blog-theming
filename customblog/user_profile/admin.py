from django.contrib import admin
from .models import Profile
from .forms import ProfileFormAdmin

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	form = ProfileFormAdmin

admin.site.register(Profile, ProfileAdmin)