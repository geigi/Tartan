from django.contrib import admin
from PhotoGallery.models import Photo, Album


# Album Administration
class ImageInline(admin.TabularInline ):
    model = Photo
    exclude=('imgPreview', 'imgThumb', )
    readonly_fields = ('admin_image',)
    extra = 3

class AlbumAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    exclude=('imgPreview', 'imgThumb', )

admin.site.register(Album, AlbumAdmin)

# Image Administration

class ImageAdmin(admin.ModelAdmin):
    exclude=('imgPreview', 'imgThumb', )
    readonly_fields = ('admin_image',)
admin.site.register(Photo, ImageAdmin)