# Created by kamimura on 2018/07/21.
# Copyright © 2018 kamimura. All rights reserved.

import setuptools

with open('README.md') as fh:
    long_description = fh.read()
setuptools.setup(
    name='sion',
    version='0.0.1',
    author='kamimura',
    author_email='kamimura@live.jp',
    license='MIT',
    description='loading and dumping a SION format file',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://sitekamimura.blogspot.com/search/label/SION',
    py_modules=['sion', 'SIONLexer', 'SIONParser', 'SIONVisitor'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Classifier: Environment :: Console',
    )
)
