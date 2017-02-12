# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE', encoding='utf-8') as f:
    license = f.read()

setup(
    name='PersianStemmer',
    version='1.0.0',
    description='Persian Stemmer for Python',
    long_description=readme,
    author='Hossein Taghi-Zadeh',
    author_email='h.t.azeri@gmail.com',
    url='https://github.com/MrHTZ/PersianStemmer-Python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

