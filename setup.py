from setuptools import setup

setup(
    name='RS Image Convertor',
    version='0.3.1',
    description='Converts RAW and iPhone formats to JPG and PNG, compress size',
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
        'Operating System :: POSIX :: Linux :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
) 
