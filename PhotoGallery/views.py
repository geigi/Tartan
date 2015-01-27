from django.http import Http404, HttpResponse
from django.shortcuts import render

from PhotoGallery.models import Album, Photo


def overview(request):
    albumList = Album.objects.order_by('name')
    context = {'albumList': albumList}
    return render(request, 'PhotoGallery/overview.thtm', context)

    
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
    context = {'img':img}
    return render(request, 'PhotoGallery/detailed.thtm', context)
    