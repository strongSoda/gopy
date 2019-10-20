import os
import io
import re
from setuptools import find_packages, setup


def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


setup(name='gopy',
      version='0.6.3',
      description='Python Data Structures and Algorithms',
      long_description=long_description(),
      long_description_content_type="text/markdown",
      url='https://github.com/strongSoda/data-structures-and-algorithms',
      download_url = 'https://github.com/strongSoda/data-structures-and-algorithms/archive/v0.6.2.tar.gz',
      author='Imran Khan',
      author_email="strongsoda2@gmail.com",
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'snakeviz=2.0.1',
          'numpy'
          ],
              'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          ],
      zip_safe=False)