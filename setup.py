import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
  name = 'csvTovcf',
  packages = ['csv2vcard'],
  version = '0.1.0',
  description = 'A library for converting csv to .vcf file',
  long_description = README,
  long_description_content_type='text/markdown',
  author = 'Shivam Mani Tripathi',
  author_email = 'abc@privatemail.com',
  url = 'https://github.com/stripathi669/csv2vcard',
  download_url = 'https://github.com/stripathi669/csv2vcard/archive/0.1.0.tar.gz',
  keywords = ['csv', 'vcard', 'export', 'vcf'],
  python_requires = '>=3.6',
  classifiers = [
    'Development Status :: 3 - Alpha','License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    ],
)
