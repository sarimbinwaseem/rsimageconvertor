from setuptools import setup, find_packages
import os

version = '0.4.3'
author = "Sarim Bin Waseem"

with open("README.md", "r") as file:
    long_description = file.read()

with open(os.path.join("rsimageconvertor", "__init__.py"), "w", encoding = "UTF-8") as file:
    file.write(f'''__version__ = "{version}"
__author__ = "{author}"''')

setup(
    name = 'rsimageconvertor',
    version = version,
    description = 'Converts RAW and iPhone formats to JPG and PNG, compress size',
    long_description = long_description,
    long_description_content_type  =  "text/markdown",
    url = 'https://github.com/sarimbinwaseem/rsimageconvertor',
    package_dir={"": "rsimageconvertor"},
    author = author,
    author_email = '',
    license = 'MIT-License',
    packages = find_packages(where = "rsimageconvertor"),
    install_requires = ['rawpy',
                      'pyheif',
                      'imageio',
                      'Pillow'],

    classifiers = [
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
) 
