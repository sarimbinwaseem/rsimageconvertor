> [!WARNING]
> Compression is not stable. Huge errors in implementation will destroy the output.

# RS Image Convertor
### Using rawpy, imageio and pyheif

#### Install directly from github:

```bash
pip install git+https://github.com/sarimbinwaseem/rsimageconvertor.git@main
```

### Convertor

#### Import and run

```python
from rsimageconvertor.convertor import Convertor
con = Convertor()
```

1. For one image<br>
```python 
con.convertOne("path/to/image.<heic, dng, etc>")
```

2. For entire folder<br>
```python
con.convertAll("path/to/folder")
```

A prompt will ask for PNG or JPEG file format<br>
Simply type png or jpg

## Size Compression
#### Compresses size on disk with minimum impact on resolution and quality.

```python
con.compressOne("path/to/image.<ext>", size = 2000, form  = "same")
```

path: path to image<br>
size: maximum size needed with miniumum resize of picture<br>
form: save as PNG or JPG or any other PIL supported format, if "same" is passed, final image will be in same format as original.
