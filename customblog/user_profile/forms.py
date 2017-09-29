from django import forms
from django.forms.widgets import TextInput
from .models import Profile


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['header_color', 'header_text_color', 'bg_color', 'title_color', 'text_color']
		widgets = {
			'header_color': TextInput(attrs={'type': 'color'}),
			'header_text_color': TextInput(attrs={'type': 'color'}),
			'bg_color': TextInput(attrs={'type': 'color'}),
			'title_color': TextInput(attrs={'type': 'color'}),
			'text_color': TextInput(attrs={'type': 'color'}),
		}

class ProfileFormAdmin(forms.ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		widgets = {
			'header_color': TextInput(attrs={'type': 'color'}),
			'header_text_color': TextInput(attrs={'type': 'color'}),
			'bg_color': TextInput(attrs={'type': 'color'}),
			'title_color': TextInput(attrs={'type': 'color'}),
			'text_color': TextInput(attrs={'type': 'color'}),
		}
