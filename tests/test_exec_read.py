
"""
"""
import logging
import os

import pytest

import pytrip.tripexecuter as pte

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope='module')
def exec_filename():
    return os.path.join('tests', 'res', 'TST003', 'EXEC', 'TST003101.exec')


def test_exec_parse(exec_filename):
    """TODO"""
    logger.info("Test parsing '{:s}'".format(exec_filename))

    plan = pte.Plan()
    plan.read_exec(exec_filename)
    assert len(plan.fields) == 3
