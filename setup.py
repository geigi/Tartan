from setuptools import setup
import os

setup(
    name="django-tartan",
    version="0.8.0",
    
    author="Julian Geywitz, Michael Schubert",
    author_email="willBeAddedLater@example.com",
    
    packages=["Tartan"],
    include_package_data = True,
    
    #package_data = {'PhotoGallery':['templates/*']},
    #package_data={"PhotoGallery": list(map(lambda x: x[0].lstrip("PhotoGallery/")+"/*", filter (lambda x: x[2],os.walk("PhotoGallery/static")))) + ["templates/*", "templates/PhotoGallery/*"]},
    
    zip_safe=False,
    
    url="https://github.com/geigi/Tartan",
    description="Django based Photo Gallery",
    )