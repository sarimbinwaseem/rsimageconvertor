from setuptools import setup

setup(
    name='RS Image Convertor',
    version='0.2.1',
    description='Converts DNG and HEIC to JPG',
    url='https://github.com/shuds13/pyexample',
    author='Sarim Bin Waseem',
    author_email='',
    license='BSD 2-clause',
    packages=['rsimageconvertor'],
    install_requires=['rawpy',
                      'pyheif',
                      'imageio',
                      'Pillow'],

    classifiers=[
        'Operating System :: POSIX :: Linux :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
) 
