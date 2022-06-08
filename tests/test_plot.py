
import imghdr
import logging
import os
import shutil
import tempfile

import pytrip.utils.dvhplot
import pytrip.utils.rst_plot

logger = logging.getLogger(__name__)


def test_generate(rst_filename):
    fd, outfile = tempfile.mkstemp(suffix='.png')

    # convert CT cube to DICOM
    pytrip.utils.rst_plot.main([rst_filename, outfile])

    # check if destination file is not empty
    assert os.path.exists(outfile) is True
    assert os.path.getsize(outfile) > 1
    assert imghdr.what(outfile) == 'png'

    os.close(fd)  # Windows needs it
    os.remove(outfile)  # we need only temp filename, not the file


def test_relative_dos_plot(dos_filename, vdx_filename):
    working_dir = tempfile.mkdtemp()  # make temp working dir for output file
    output_file = os.path.join(working_dir, "foo.png")

    pytrip.utils.dvhplot.main(args=[dos_filename, vdx_filename, 'target', '-l', '-v', '-o', output_file])

    logger.info("Checking if " + output_file + " is PNG")
    assert imghdr.what(output_file) == 'png'

    logger.info("Removing " + working_dir)
    shutil.rmtree(working_dir)


def test_absolute_dos_plot(dos_filename, vdx_filename):
    working_dir = tempfile.mkdtemp()  # make temp working dir for output file
    output_file = os.path.join(working_dir, "foo.png")

    pytrip.utils.dvhplot.main(args=[dos_filename, vdx_filename, 'target', '-l', '-v', '-d 2.0', '-o', output_file])

    logger.info("Checking if " + output_file + " is PNG")
    assert imghdr.what(output_file) == 'png'

    logger.info("Removing " + working_dir)
    shutil.rmtree(working_dir)


def test_let_plot(let_filename, vdx_filename):
    working_dir = tempfile.mkdtemp()  # make temp working dir for output file
    output_file = os.path.join(working_dir, "foo.png")

    pytrip.utils.dvhplot.main(args=[let_filename, vdx_filename, 'target', '-l', '-v', '-o', output_file])

    logger.info("Checking if " + output_file + " is PNG")
    assert imghdr.what(output_file) == 'png'

    logger.info("Removing " + working_dir)
    shutil.rmtree(working_dir)
