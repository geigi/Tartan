from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name


class Photo(models.Model):
    # constants
    
    # Preview Resolutions
    THUMBSIZE = (50,50)
    PREVIEWSIZE = (300,200)
    
    name = models.CharField(max_length = 200, null = True, blank = True)    
    description = models.TextField(blank = True)
    
    imgOrig = models.ImageField()
    imgPreview = models.ImageField(editable=True, default=None)
    imgThumb = models.ImageField(editable=True, default = None)
    
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
             
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png' 
            
            #Original photo
            imgPilPreview = Image.open(BytesIO(self.imgOrig.read()))

            if imgPilPreview.mode not in ('L', 'RGB'):
                imgPilPreview = imgPilPreview.convert('RGB') 
            
            imgPilThumb = ImageOps.fit(imgPilPreview, self.THUMBSIZE, Image.ANTIALIAS)
                
            imgPilPreview.thumbnail(self.PREVIEWSIZE, Image.ANTIALIAS)
            
            previewHandle = BytesIO()
            thumbHandle = BytesIO()
            imgPilPreview.save(previewHandle, PIL_TYPE)
            imgPilThumb.save(thumbHandle, PIL_TYPE)
            previewHandle.seek(0)  
            thumbHandle.seek(0)
            previewSuf = SimpleUploadedFile(os.path.split(self.imgOrig.name)[-1], previewHandle.read(), content_type="image/png") 
            thumbSuf = SimpleUploadedFile(os.path.split(self.imgOrig.name)[-1], thumbHandle.read(), content_type="image/png") 

            self.imgThumb.save('%s_thumb.%s'%(os.path.splitext(thumbSuf.name)[0],FILE_EXTENSION), thumbSuf, save=False)
            self.imgPreview.save('%s_preview.%s'%(os.path.splitext(previewSuf.name)[0],FILE_EXTENSION), previewSuf, save=False)

        
        super(Photo, self).save()


    def __str__(self):
        return self.name + " (in " + self.album.name +")"
        
    def admin_image(self):
        return '<img src="%s"/>' % self.imgPreview.url
    admin_image.short_description = 'Preview'
    admin_image.allow_tags = True