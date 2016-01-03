#!/usr/bin/env python

from setuptools import setup

version = __import__('papersizes').__version__

setup(
    name='papersizes',
    packages=[
        'papersizes'
        ],

    version=version,
    description='Paper sizes and manipulations',
    author='Ian Millington',
    author_email='idmillington@googlemail.com',

    url='http://github.com/idmillington/papersizes',
    download_url='https://github.com/idmillington/papersizes/tarball/master',

    keywords=['pdf', 'papersizes', 'print', 'design'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics",
        ],

    zip_safe=False,

    # Testing and documentation requirements can be installed with:
    # pip install -r dev-requirements.txt
    install_requires=[]

    )
