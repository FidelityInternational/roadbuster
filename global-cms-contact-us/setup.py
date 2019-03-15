# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from global_cms_contact_us import __version__


setup(
    name='global-cms-contact-us',
    version=__version__,
    description=open('README.rst').read(),
    author='FidelityDevelopment',
    author_email='FIL-DjangoCMS-Devs@fil.com',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)
