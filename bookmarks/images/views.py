from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Image
from .forms import ImageCreateForm


@login_required
def image_create(request):
  if request.method == 'POST':
    form = ImageCreateForm(data=request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      new_item = form.save(commit=False)
      new_item.user = request.user
      new_item.save()
      messages.success(request, 'Image added succcessfully')

      return redirect(new_item.get_absolute_url())
  else:
    form = ImageCreateForm(data=request.GET)
  context = {
    'section': 'images',
    'form': form
  }
  return render(request, 'images/image/create.html',context)

def image_detail(request, id, slug):
  image = get_object_or_404(Image, id=id, slug=slug)
  context = {
    'selection': 'images',
    'image': image
  }
  return render(request, 'images/image/detail.html', context)

@login_required
@require_POST
def image_like(request):
  image_id = request.POST.get('id')
  action = request.POST.get('action')
  if image_id and action:
    try :
      image = Image.objects.get(id=image_id)
      if action == 'like':
        image.users_like.add(request.user)
      else:
        image.users_like.remove(request.users)
      return JsonResponse({'status':'ok'})
    except:
      pass
  return JsonResponse({'status':'error'})