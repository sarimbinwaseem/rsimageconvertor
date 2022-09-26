# RS Image Convertor
### Using rawpy, imageio and pyheif

#### Install directly from github:

`pip install git+https://github.com/sarimbinwaseem/rsimageconvertor.git@main`

#### Import and run

``
from rsimageconvertor.convertor import Convertor
con = Convertor()
``

1. For one image<br>
`` con.convertOne("path/to/image.<heic, dng, etc>")``

2. For entire folder<br>
`` con.convertAll("path/to/folder")``

A prompt will ask for PNG or JPEG file format<br>
Simply type png or jpg
