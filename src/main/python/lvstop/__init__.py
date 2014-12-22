#!/usr/bin/env python

__author__ = "Grzegorz Halajko'"
__version__ = "0.1.0"
version_info = tuple([int(num) for num in __version__.split('.')])


__all__ = ["version_info", "__version__"]


import os
import sys

if os.name != 'posix':
    sys.exit('platform not supported')

    