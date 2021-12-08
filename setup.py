# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Samson Wang
# --------------------------------------------------------

from __future__ import print_function

import sys

import numpy as np
from Cython.Build import cythonize
from setuptools import Extension, setup

# Obtain the numpy include directory, only for numpy >= 1.0.0
numpy_include = np.get_include()

with open("README.md", "r") as fh:
    long_description = fh.read()


if sys.platform == "win32":
    extra_compile_args = ["/Qstd=c99"]
else:
    extra_compile_args = ["-std=c99"]

ext_modules = [
    Extension(
        name="cython_bbox",
        sources=["src/cython_bbox.pyx"],
        extra_compile_args=extra_compile_args,
        include_dirs=[numpy_include],
    )
]

compiler_directives = {"language_level": 3}
ext_modules = cythonize(ext_modules, compiler_directives=compiler_directives)

setup(
    name="cython_bbox",
    version="0.1.3",
    description="Standalone cython_bbox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Samson Wang",
    author_email="samson.c.wang@gmail.com",
    url="https://github.com/samson-wang/cython_bbox.git",
    keywords=["cython_bbox"],
    ext_modules=ext_modules,
    install_requires=["numpy>=1.0.0"],
)
