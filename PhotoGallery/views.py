from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from PhotoGallery.models import Album, Photo

import json

def overview(request):
    albumList = Album.objects.order_by('name')
    context = {'albumList': albumList}
    return render(request, 'PhotoGallery/gallery.thtm', context)

    
def albumDetail(request, albumid):
    try:
        album = Album.objects.get(id=albumid)
    except Album.DoesNotExist:
        raise Http404
    
    def sortparse(rawval):
        return {
            'oldest':'-added',
            'newest':'added',
            'name':'name',
            'namereverse':'-name',
            }.get(rawval)
    
    orderParam = request.GET.get('ordering')
    ordering = sortparse(orderParam)
     
    imgSet = album.photo_set #do not pass this to template, its not iterable!
    
    if (ordering):
        imgList = imgSet.order_by(ordering, 'pk')
    else:
        imgList = imgSet.all
    
    context = {'album': album, 'imgList': imgList}

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

    try:
        dia = request.GET["dia"]
        dur = int(dia)
        if (dur <= 0):
            dur = False
    except (ValueError, KeyError):
        dur = False
    
    context = {'img':img, 'next':next, 'prev':prev, 'diaDuration': dur}
    return render(request, 'PhotoGallery/carousel.thtm', context)
    
def imageJsonInfo (request, imgid):
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

    try:
        dia = request.GET["dia"]
        dur = int(dia)
        if (dur <= 0):
            dur = False
    except (ValueError, KeyError):
        dur = False
    
    jsonInfo = {}
    jsonInfo['name'] = img.name
    jsonInfo['currImgUrl'] = img.imgOrig.url
    jsonInfo['currSiteUrl'] = reverse('imageDetail', kwargs = {'imgid': img.id} )
    if (next):
        jsonInfo['nextInfoUrl'] = reverse('imageJsonInfo', kwargs = {'imgid': next.id} )
    else:
        jsonInfo['nextInfoUrl'] = False
    if (prev):
        jsonInfo['prevInfoUrl'] = reverse('imageJsonInfo', kwargs = {'imgid': prev.id} )
    else:
        jsonInfo['prevInfoUrl'] = False
    
    
    return HttpResponse(json.dumps(jsonInfo), content_type="application/json")