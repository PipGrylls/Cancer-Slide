# Cancer-Slide
Building a pipeline to take .vsi files from Olympus microscopes and split them into constituent images for use in ML methods


## Setup

pip(3): requests, requests_toolkit, Pillow

conda (or pip): pandas

sudo apt-get install libgdiplus
sudo apt-get install libgif-dev autoconf libtool automake build-essential gettext libglib2.0-dev libcairo2-dev libtiff-dev libexif-dev

Download, https://free.pathomation.com/download/, 
and run pathomation it should launch a server and web-browser interface.
(If the URL is not http://localhost:54001/, then this will need to be changed in image_load.py)

In image_load.py set the slide directory to be "Root/path-to-files/" 