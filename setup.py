from distutils.core import setup
from setuptools import find_packages


setup(name='se83limo',
        version='0.17',
        author='Leonard Kuhn',
        author_email='leo.kuhn@fau.de',
        packages=find_packages(),
        install_requires=['numpy', 'Pillow', 'ipywidgets'])