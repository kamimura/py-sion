
# Created by kamimura on 2018/07/21.
# Copyright © 2018 kamimura. All rights reserved.

import setuptools

with open('README.md') as fh:
    long_description = fh.read()
setuptools.setup(
    name='sion',
    version='0.2.0',
    author='kamimura',
    author_email='kamimura@live.jp',
    license='MIT',
    description='loading and dumping a SION format file',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kamimura/py-sion',
    py_modules=['sion', 'SIONParser',
                'SIONLexer', 'SIONVisitor'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console"
    ),
    install_requires=['antlr4-python3-runtime'],
    package_dir={'': 'src'},
)
