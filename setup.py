# Created by kamimura on 2018/07/21.
# Copyright © 2018 kamimura. All rights reserved.

import setuptools

with open('README.md') as fh:
    long_description = fh.read()
setuptools.setup(
    name='sion',
    version='0.1.0',
    author='kamimura',
    author_email='kamimura@live.jp',
    license='MIT',
    description='loading and dumping a SION format file',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kamimura/py-sion',
    packages=['src'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console"
    )
)
