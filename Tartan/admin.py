from django.contrib import admin
from django import forms
from Tartan.models import Photo, Album

from multiupload.fields import MultiFileField

# Album Administration

class AlbumAdminForm(forms.ModelForm):
    multi_photo_upload = MultiFileField(required = False, max_file_size=50*1024*1024)    
    class Meta:
        model=Album
        fields='__all__'
    def save(self, commit=True):
        rv = super(AlbumAdminForm, self).save(commit=commit) 
        for imgfile in self.cleaned_data['multi_photo_upload']:
            print('got photo')
            photo = Photo()
            photo.imgOrig=imgfile
            photo.album=self.instance
            photo.save()
        return rv

class ImageInline(admin.TabularInline ):
    model = Photo
    exclude=('imgPreview', 'imgThumb', )
    readonly_fields = ('admin_image',)
    extra = 3

class AlbumAdmin(admin.ModelAdmin):
    form = AlbumAdminForm
    inlines = [ImageInline]
    exclude=('imgPreview', 'imgThumb', )

admin.site.register(Album, AlbumAdmin)

# Image Administration

class ImageAdmin(admin.ModelAdmin):
    exclude=('imgPreview', 'imgThumb', )
    readonly_fields = ('admin_image',)
admin.site.register(Photo, ImageAdmin)