Tartan is a modern and lightweight web photo gallery using Django.
The only Web Framework it uses is jQuery, no Bootstrap, etc. is used.

**Gallery Overview:**
![](/../screenshots/Screenshots/Overview_Dark.png)

**Album Overview:**
![](/../screenshots/Screenshots/Album_Dark.png)

**Carousel:**
![](/../screenshots/Screenshots/Carousel_Dark.png)

**Custom Color Scheme:**
![](/../screenshots/Screenshots/Overview_Light.png)

# Features
- Organize photos by albums
- Add descriptions to your photos
- Diashow mode
- Quick jump
- Download original file
- Bandwith optimized through small thumbnails
- Optimized for PC and Tablet use
- Works in browsers with disabled JavaScript

# Admin Features
- Upload multiple Photos at a time
- Create color schemes with a single CSS file

# Requirements
- Chrome 10 (Release: 08.03.2011)
- Firefox 3.6 (Release: 21.01.2010)
- Internet Explorer 10 (Release: 04.09.2012) 
- Opera 11.6 (Release: 06.12.2011)
- Safari 5.1 (Release: 21.07.2011) 

# Requirements for the Server
- Python, ideally Python 3
- Django
- Pillow

# Install
- Install Python, Django, Pillow
 
After `git clone`:
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`

# Server Installation

* [Installation on Linux](https://github.com/geigi/Tartan/wiki/Installation-on-Linux)

# Update
- `python manage.py makemigrations`
- `python manage.py migrate`

# Run debug server
- `python manage.py runserver`

# Naming
http://de.wikipedia.org/wiki/Farbfotografie#mediaviewer/File:Tartan_Ribbon.jpg

# Special Thanks
- jQuery: http://jquery.com
- JScrollPane: http://jscrollpane.kelvinluck.com
- Font Awesome: http://fortawesome.github.io/Font-Awesome/
- W3C: http://validator.w3.org
- Django: https://www.djangoproject.com
- Pillow: https://pillow.readthedocs.org
