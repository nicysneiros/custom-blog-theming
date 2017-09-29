from .models import Profile

def profile_processors(request):
	context = {}
	try:
		context = {
			'profile': Profile.objects.get(user=request.user.pk) 
		}
	except Exception:
		pass

	return context