import os
import io
import re
from setuptools import find_packages, setup


def long_description():
    with io.open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


setup(name='gopy',
      version='0.7.2',
      description='Python Data Structures and Algorithms',
      long_description=long_description(),
      long_description_content_type="text/markdown",
      url='https://github.com/strongSoda/gopy',
      download_url = 'https://github.com/strongSoda/gopy/archive/v0.7.0.tar.gz',
      author='Imran Khan',
      author_email="strongsoda2@gmail.com",
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'snakeviz>=2.0.1',
          'numpy>=1.17.0'
          ],
      classifiers=[
          'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
          'Intended Audience :: Developers',      # Define that your audience are developers
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',   # Again, pick a license
          'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          ],
      zip_safe=False)