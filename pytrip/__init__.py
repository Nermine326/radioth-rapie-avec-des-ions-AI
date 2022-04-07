
"""
TODO: documentation here.
"""
# do not check this file for PEP8 compatibility
# flake8 complains about "E402 module level import not at top of file"
# flake8: noqa

import logging
from pytrip.cube import Cube
from pytrip.ctx import CtxCube
from pytrip.dos import DosCube
from pytrip.vdx import VdxCube, Voi
from pytrip.paths import DensityCube
from pytrip.raster import Rst
from pytrip.let import LETCube
from pytrip.dicomhelper import read_dicom_dir

# from https://docs.python.org/3/tutorial/modules.html
# if a package's __init__.py code defines a list named __all__,
# it is taken to be the list of module names that should be imported when from package import * is encountered.
__all__ = ['CtxCube', 'VdxCube', 'Voi', 'DosCube', 'DensityCube', 'LETCube', 'dicomhelper', 'res',
           'Rst']

# if an application using pytrip doesn't configure any logging level, then an error will occur
# to prevent it, we add null logging handler, as suggested by Python documentation:
# as described here: https://docs.python.org/3/howto/logging.html#library-config
logging.getLogger(__name__).addHandler(logging.NullHandler())
