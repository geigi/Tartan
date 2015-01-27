from django.db import models

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
    
    name = models.CharField(max_length = 200, null = True)
    
    imgOrig = models.ImageField()
    imgPreview = models.ImageField(null=True, default=None, blank=True)
    imgThumb = models.ImageField(null=True, default=None, blank=True)
    
    album = models.ForeignKey(Album)
    
    def save(self):
        from PIL import Image, ImageOps
        from io import BytesIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        import os 
        
        
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