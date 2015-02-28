from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.utils.html import escape
from django.db.models import Q, Max
from PhotoGallery.models import Album, Photo

import json

ASCENDING = False;
DESCENDING = True;

####### USER VIEWS #######

# Home view (start page) -> list all albums
def overview(request):
    def sortparseAlbum(rawval):
        return {
            'name':('name',ASCENDING,'name',"name"),
            'namereverse':('name',DESCENDING, '-name', "namereverse"),
            'newestphotofirst': ('lastPhotoUpload',DESCENDING, '-lastPhotoUpload', "newestphotofirst"),
            'newestphotolast':  ('lastPhotoUpload',ASCENDING,  'lastPhotoUpload',  "newestphotolast"),
            'oldest':('created', DESCENDING, '-created', "oldest"),
            'newest':('created', ASCENDING, 'created', "newest"),
            }.get(rawval, ('pk', ASCENDING, 'pk', "pk"))      # default: order by primary key (pk)
    
    rawval = request.GET.get('ordering')
    ordering = sortparseAlbum(rawval)
    
    albumList = Album.objects.annotate(lastPhotoUpload=Max("photo__added")).order_by(ordering[2], "pk")
    context = {'albumList': albumList}
    return render(request, 'PhotoGallery/gallery.thtm', context)

# Album view -> list all images inside an album
def albumDetail(request, albumid):
    try:
        album = Album.objects.get(id=albumid)
    except Album.DoesNotExist:
        raise Http404
    
    rawval = request.GET.get('ordering')
    ordering = sortparse(rawval)
     
    imgList = album.photo_set.order_by(ordering[2], 'pk')
        
    context = {'album': album, 'imgList': imgList}
    if (ordering[0] != "pk"):
        context["ordering"] = ordering[3]
        

    return render(request, 'PhotoGallery/album.thtm', context)

# Detail view -> show a single image in large size
def imageDetail(request, imgid):
    try:
        img = Photo.objects.get(id=imgid)
    except Photo.DoesNotExist:
        raise Http404
    
    rawval = request.GET.get('ordering')
    ordering = sortparse(rawval)

    (prev, next) = nextPrevImg(request, img, ordering)
    
    thumbs = img.album.photo_set.order_by(ordering[2])

    try:
        dia = request.GET["dia"]
        dur = int(dia)
        if (dur <= 0):
            dur = False
    except (ValueError, KeyError):
        dur = False
    
    context = {'img':img, 'next':next, 'prev':prev, 'diaDuration': dur, 'thumbs' : thumbs}
    if (ordering[0] != "pk"):
        context["ordering"] = ordering[3]
    return render(request, 'PhotoGallery/carousel.thtm', context)


####### API VIEWS #######

# return image specific information
def imageJsonInfo (request, imgid):
    try:
        img = Photo.objects.get(id=imgid)
    except Photo.DoesNotExist:
        raise Http404
        
    rawval = request.GET.get('ordering')
    ordering = sortparse(rawval)
    
    (prev, next) = nextPrevImg(request, img, ordering)

    try:
        dia = request.GET["dia"]
        dur = int(dia)
        if (dur <= 0):
            dur = False
    except (ValueError, KeyError):
        dur = False
    
    jsonInfo = {}
    jsonInfo['id'] = img.id
    jsonInfo['name'] = escape(img.name)
    jsonInfo['description'] = escape(img.description)
    jsonInfo['currImgUrl'] = img.imgOrig.url

    jsonInfo['currSiteUrl'] = reverse('imageDetail', kwargs = {'imgid': img.id} ) + ("?ordering=%s" % ordering[3] if ordering[0] != "pk" else "")
    if (next):
        jsonInfo['nextInfoUrl'] = "%s?ordering=%s" % (reverse('imageJsonInfo', kwargs = {'imgid': next.id} ), ordering[3])
    else:
        jsonInfo['nextInfoUrl'] = False
    if (prev):
        jsonInfo['prevInfoUrl'] = "%s?ordering=%s" % (reverse('imageJsonInfo', kwargs = {'imgid': prev.id} ), ordering[3])
    else:
        jsonInfo['prevInfoUrl'] = False
    
    
    return HttpResponse(json.dumps(jsonInfo), content_type="application/json")

####### HELPER FUNCTONS #######

# get next and previous image object of an given image
def nextPrevImg(request, img, ordering):
    ## get next element
    #get elements with order values higher (or lower) than current
    nextNameExp = { ordering[0] + ("__gt" if (ordering[1] == ASCENDING) else "__lt") : getattr(img, ordering[0]) }
    nextNameQ = Q(**nextNameExp)
    # get values with same ordering key, but higher PK
    sameNameNextPkExpr = { ordering[0] : getattr(img, ordering[0]), "pk__gt" : img.pk }
    sameNameNextPkQ = Q(**sameNameNextPkExpr)
    q = img.album.photo_set.filter(nextNameQ | sameNameNextPkQ).order_by(ordering[2], "pk")[:1]
    if (q):
        next = q[0]
    else:
        next = False
    
    ## get previous element
    #get elements with order values lower (or higher) than current
    prevNameExpr = { ordering[0] + ("__lt" if (ordering[1] == ASCENDING) else "__gt") : getattr(img, ordering[0]) }
    prevNameQ = Q(**prevNameExpr)
    # get values with same ordering key, but lower PK
    sameNamePrevPkExpr = { ordering[0] : getattr(img, ordering[0]), "pk__lt": img.pk }
    sameNamePrevPkQ = Q(**sameNamePrevPkExpr)
    q = img.album.photo_set.filter(prevNameQ | sameNamePrevPkQ).order_by(ordering[2], "pk").reverse()[:1]
    if (q):
        prev = q[0]
    else:
        prev = False
    return (prev, next)

# return a tupel defining the ordering.
# always returns a tupel, never false -> no eror checking needed
def sortparse(rawval):
    return {
        'oldest':('added', DESCENDING, '-added', "oldest"),
        'newest':('added', ASCENDING, 'added', "newest"),
        'name':('name', ASCENDING, 'name', "name"),
        'namereverse':('name',DESCENDING, '-name', "namereverse"),
        }.get(rawval, ('pk', ASCENDING, 'pk', "pk"))      # default: order by primary key (pk)