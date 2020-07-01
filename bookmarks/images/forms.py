from django import forms
from .models import Image

class ImageCreateForm(forms.ModelForm):
  class Meta:
    model = Image
    fields = ['title', 'url', 'description']
    widgets = {
      'urls': forms.HiddenInput
    }
  
  def clean_url(self):
    url = self.cleaned_data['url']
    valid_extensions = ['jpg','jpeg']
    extensions = url.rspilt('.', 1)[1].lower()
    if extensions not in valid_extensions:
      raise forms.ValidationError('The given URL doesnt match valid image extensions')
    return url