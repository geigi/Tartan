from django.db import models
from django.utils import timezone
from django.db.models import Min
import datetime

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length = 200)
    
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime(2000,1,1))
    
    def __str__(self):
        return self.name

class Photo(models.Model):
    # constants
    
    # Compressed Image Resolutions
    THUMBSIZE = (65,65)
    PREVIEWSIZE = (300,200)
    CAROUSELSIZE = (2000,1200)
    
    name = models.CharField(max_length = 200, null = True, blank = True)    
    description = models.TextField(blank = True)
    
    imgOrig = models.ImageField()
    
    imgPreview = models.ImageField(editable=False)
    imgThumb = models.ImageField(editable=False)
    imgCarousel = models.ImageField(editable=False)
    
    album = models.ForeignKey(Album)
    
    added = models.DateTimeField(auto_now_add=True, default = timezone.now())
        
    def save(self):
        from PIL import Image, ImageOps
        from io import BytesIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        import os 
        
        def has_changed(instance, field):
            if not instance.pk:
                return False
            old_value = instance.__class__._default_manager.filter(pk=instance.pk).values(field).get()[field]
            return not getattr(instance, field) == old_value
            
        # Only create new thumbnails if Image file changed or this is a completly new database entry
        if ((self.pk is None) or has_changed(self, 'imgOrig')):
            DJANGO_TYPE = self.imgOrig.file.content_type
            
            # Possible Image Types
            IMGTYPE = {
                'PNG': {
                        "PIL_TYPE":"png",
                        "EXTENSION":"png",
                        "MIME":"image/png",
                    },
                'JPEG': {
                        "PIL_TYPE":"jpeg",
                        "EXTENSION":"jpg",
                        "MIME":"image/jpeg",
                    }
                }


            # which types to use for which image
            PREVIEW_TYPE = IMGTYPE["PNG"]
            THUMB_TYPE = IMGTYPE["PNG"]
            CAROUSEL_TYPE = IMGTYPE["JPEG"]
            
            # Open Original photo
            imgPilOrig = Image.open(BytesIO(self.imgOrig.read()))
            
            # convert original to RGB
            if imgPilOrig.mode not in ('L', 'RGB'):
                imgPilOrig = imgPilOrig.convert('RGB') 
            
            # Create a Copy of the original photo to be resized to every needed size
            imgPilPreview = imgPilOrig.copy()
            imgPilCarousel = imgPilOrig.copy()

            # create Thumbnails (Peview + Carousel) and Icons
            imgPilThumb = ImageOps.fit(imgPilPreview, self.THUMBSIZE, Image.ANTIALIAS)
            imgPilPreview.thumbnail(self.PREVIEWSIZE, Image.ANTIALIAS)
            imgPilCarousel.thumbnail(self.CAROUSELSIZE, Image.ANTIALIAS)
            
            # IO Stream
            previewHandle = BytesIO()
            thumbHandle = BytesIO()
            carouselHandle  = BytesIO()

            # save the Image in the expected file format
            imgPilPreview.save(previewHandle, PREVIEW_TYPE["PIL_TYPE"])
            imgPilThumb.save(thumbHandle, THUMB_TYPE["PIL_TYPE"])
            imgPilCarousel.save(carouselHandle, CAROUSEL_TYPE["PIL_TYPE"])

            previewHandle.seek(0)  
            thumbHandle.seek(0)
            carouselHandle.seek(0)
            
            #make Django know the newl created files
            previewSuf = SimpleUploadedFile(os.path.split(self.imgOrig.name)[-1], previewHandle.read(), content_type=PREVIEW_TYPE["MIME"]) 
            thumbSuf = SimpleUploadedFile(os.path.split(self.imgOrig.name)[-1], thumbHandle.read(), content_type=THUMB_TYPE["MIME"]) 
            carouselSuf = SimpleUploadedFile(os.path.split(self.imgOrig.name)[-1], carouselHandle.read(), content_type=CAROUSEL_TYPE["MIME"]) 

            # save them
            self.imgThumb.save('%s_thumb.%s'%(os.path.splitext(thumbSuf.name)[0],THUMB_TYPE["EXTENSION"]), thumbSuf, save=False)
            self.imgPreview.save('%s_preview.%s'%(os.path.splitext(previewSuf.name)[0],PREVIEW_TYPE["EXTENSION"]), previewSuf, save=False)
            self.imgCarousel.save('%s_carousel.%s'%(os.path.splitext(carouselSuf.name)[0],CAROUSEL_TYPE["EXTENSION"]), carouselSuf, save=False)

        
        super(Photo, self).save()


    def __str__(self):
        return self.name + " (in " + self.album.name +")"
        
    def admin_image(self):
        return '<img src="%s"/>' % self.imgPreview.url
    admin_image.short_description = 'Preview'
    admin_image.allow_tags = True