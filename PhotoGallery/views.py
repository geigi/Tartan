from django.http import Http404, HttpResponse
from django.shortcuts import render

from PhotoGallery.models import Album, Photo


def overview(request):
    albumList = Album.objects.order_by('name')
    context = {'albumList': albumList}
    return render(request, 'PhotoGallery/gallery.thtm', context)

    
def albumDetail(request, albumid):
    try:
        album = Album.objects.get(id=albumid)
    except Album.DoesNotExist:
        raise Http404
    context = {'album': album}
    return render(request, 'PhotoGallery/album.thtm', context)

def imageDetail(request, imgid):
    try:
        img = Photo.objects.get(id=imgid)
    except Photo.DoesNotExist:
        raise Http404
        
    q = img.album.photo_set.filter(id__gt=imgid).order_by('id')[:1]
    if (q):
        next = q[0]
    else:
        next = False
    
    q = img.album.photo_set.filter(id__lt=imgid).order_by('-id')[:1]
    if (q):
        prev = q[0]
    else:
        prev = False

    context = {'img':img, 'next':next, 'prev':prev}
    return render(request, 'PhotoGallery/carousel.thtm', context)
    