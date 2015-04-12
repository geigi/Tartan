from multiupload.fields import MultiFileField
from django.forms import ImageField


import sys

class MultiImageField(MultiFileField, ImageField):
    def to_python(self, data):
        ret = []
        for item in data:
            i = ImageField.to_python(self,item)
            if i:
                ret.append(i)
        return ret 
