from django.shortcuts import render
from Storages.models import Gallery
from django.shortcuts import redirect


def gallery(request):
    gallery = Gallery.objects.order_by("-id")
    return render(request, 'rest/index.html', context={'gallery': gallery})

def like(request):
    try:
        id_gal=request.GET['like']
        Image_el = Gallery.objects.get(id = id_gal)
    except:
        raise Http404("not found")
    Image_el.raiting += 1
    Image_el.save()
    return redirect('http://127.0.0.1:8000/'.format(id_gal))

def dislike(request):
    try:
        id_gal=request.GET['dislike']
        Image_el = Gallery.objects.get(id = id_gal)
    except:
        raise Http404("not found")
    Image_el.raiting -= 1
    Image_el.save()
    return redirect('http://127.0.0.1:8000/'.format(id_gal))
