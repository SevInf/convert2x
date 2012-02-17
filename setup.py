from distutils.core import setup


setup(
    name='convert2x',
    version='0.1',
    author='Sergej Tatarincev',
    author_email='st@bekitzur.com',
    scripts=['bin/convert2x'],
    description='Tool for downscaling @2x images',
    long_description=open('README').read(),
    license='LICENSE',

    install_requires=[
        'PIL >= 1.1.7'
    ]
)
