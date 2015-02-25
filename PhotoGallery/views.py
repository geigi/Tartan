from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from PhotoGallery.models import Album, Photo

import json

ASCENDING = False;
DESCENDING = True;

####### USER VIEWS #######

# Home view (start page) -> list all albums
def overview(request):
    albumList = Album.objects.order_by('name')
    context = {'albumList': albumList}
    return render(request, 'PhotoGallery/gallery.thtm', context)

# Album view -> list all images inside an album
def albumDetail(request, albumid):
    try:
        album = Album.objects.get(id=albumid)
    except Album.DoesNotExist:
        raise Http404
    
    ordering = sortparse(request)
     
    imgList = album.photo_set.order_by(ordering[2], 'pk') #do not pass this to template, its not iterable!
        
    context = {'album': album, 'imgList': imgList}

    return render(request, 'PhotoGallery/album.thtm', context)

# Detail view -> show a single image in large size
def imageDetail(request, imgid):
    try:
        img = Photo.objects.get(id=imgid)
    except Photo.DoesNotExist:
        raise Http404
    
    # get next element
    q = img.album.photo_set.filter(id__gt=imgid).order_by('id')[:1]
    if (q):
        next = q[0]
    else:
        next = False
    
    # get previous element
    q = img.album.photo_set.filter(id__lt=imgid).order_by('id').reverse()[:1]
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


####### API VIEWS #######

# return image specific information
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
    jsonInfo['id'] = img.id
    jsonInfo['name'] = img.name
    jsonInfo['description'] = img.description
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

####### HELPER FUNCTONS #######

# return a tupel defining the ordering.
# always returns a tupel, never false -> no eror checking needed
def sortparse(request):
    rawval = request.GET.get('ordering')
    return {
        'oldest':('added', DESCENDING, '-added'),
        'newest':('added', ASCENDING, 'added'),
        'name':('name', DESCENDING, 'name'),
        'namereverse':('name',ASCENDING, '-name'),
        }.get(rawval, ('pk', ASCENDING, 'pk'))      # default: order by primary key (pk)