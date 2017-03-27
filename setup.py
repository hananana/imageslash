# coding: UTF-8

from setuptools import setup, find_packages

setup(
    name='imageslash',
    version='1.0',
    packages=find_packages(),
    description='cut mapchip',
    author='hananana',
    license='MIT',
    install_requires=[
        'click',
        'olefile',
        'Pillow',
    ],
    entry_points='''
        [console_scripts]
        imageslash=src.imageslash:cmd
    ''',
)
