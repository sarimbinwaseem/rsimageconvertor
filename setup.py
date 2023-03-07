from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='rsimageconvertor',
    version='0.3.3',
    description='Converts RAW and iPhone formats to JPG and PNG, compress size',
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url='https://github.com/sarimbinwaseem/rsimageconvertor',
    author='Sarim Bin Waseem',
    author_email='',
    license='MIT-License',
    packages=['rsimageconvertor'],
    install_requires=['rawpy',
                      'pyheif',
                      'imageio',
                      'Pillow'],

    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
) 
