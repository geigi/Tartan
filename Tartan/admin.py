from django.contrib import admin
from django import forms
from Tartan.models import Photo, Album

from Tartan.forms import MultiImageField

# Album Administration

class AlbumAdminForm(forms.ModelForm):
    multi_photo_upload = MultiImageField(required = False, max_file_size=50*1024*1024)
    class Meta:
        model=Album
        fields='__all__'
    def save(self, commit=True):
        newInst = super(AlbumAdminForm, self).save(commit=True)
        for imgfile in self.cleaned_data['multi_photo_upload']:
            photo = Photo()
            photo.imgOrig=imgfile
            photo.album=newInst
            photo.save()
        return newInst

    #dummy to satisfy Django
    def save_m2m(self):
        return

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
