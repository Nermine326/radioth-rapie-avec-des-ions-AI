
import logging
import os
import tempfile

import pytest

import pytrip.utils.rst2sobp
from pytrip.raster import Rst

logger = logging.getLogger(__name__)


@pytest.mark.smoke
def test_read(rst_filename):
    """Check if we are able to read a simple .rst file"""
    r = Rst()
    r.read(rst_filename)
    assert r.submachines == '17'
    assert r.machines[0].points == 323
    assert r.machines[0].energy == 120.2
    assert r.machines[0].raster_points[0] == [27.0, -24.0, 2844850.0]


@pytest.mark.smoke
def test_generate(rst_filename):
    """Execute rst2sobp.py and make sure a non-empty file exists."""
    fd, outfile = tempfile.mkstemp()

    pytrip.utils.rst2sobp.main(args=[rst_filename, outfile])

    # check if destination file is not empty
    assert os.path.exists(outfile) is True
    assert os.path.getsize(outfile) > 1

    os.close(fd)  # Windows needs it
    os.remove(outfile)  # we need only temp filename, not the file
