
import logging
import os
import tempfile

from pytrip.let import LETCube
from pytrip.vdx import create_sphere
from tests.conftest import exists_and_nonempty

logger = logging.getLogger(__name__)


def test_read(let_filename):
    let = LETCube()
    let.read(let_filename)

    v = create_sphere(let, name="sph", center=[10., 10., 10.], radius=8.)
    assert v is not None

    logger.info("Calculating DVH")
    result = let.calculate_lvh(v)
    assert result is not None
    lvh, min_l, max_l, _, area = result
    assert area > 2.
    assert len(lvh.shape) == 1
    assert lvh.shape[0] == 3000
    assert min_l == 0.
    assert max_l == 1.

    assert let.get_max() > 30.

    fd, outfile = tempfile.mkstemp()
    os.close(fd)  # Windows needs it
    os.remove(outfile)  # we need only temp filename, not the file
    let.write(outfile)
    hed_file = outfile + LETCube.header_file_extension
    dos_file = outfile + LETCube.data_file_extension
    assert exists_and_nonempty(hed_file) is True
    assert exists_and_nonempty(dos_file) is True
    os.remove(hed_file)
    os.remove(dos_file)
