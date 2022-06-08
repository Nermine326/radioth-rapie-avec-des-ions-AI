
import logging

import numpy as np
import pytest

import pytrip as pt
from pytrip.models.proton import rbe_carabe, rbe_mcnamara, rbe_wedenberg
from pytrip.models.rcr import sf_rcr

logger = logging.getLogger(__name__)


@pytest.mark.smoke
@pytest.mark.parametrize('model_func', [rbe_carabe, rbe_mcnamara, rbe_wedenberg])
def test_few_values(model_func):
    rbe1 = model_func(10., 10., 5.)
    rbe2 = model_func(10., 17., 5.)
    assert rbe2 > rbe1
    assert rbe2 > 1.  # Carabe can actually return values below 1.0 for RBE
    assert 10. > rbe2  # Sanity check


def test_mcnamara_cube(dos_filename, let_filename, vdx_filename):
    """McNamara test on real cubes."""
    dose = pt.DosCube()
    dose.read(dos_filename)
    let = pt.LETCube()
    let.read(let_filename)
    v = pt.VdxCube(dose)
    logger.info("Adding VDX from path " + vdx_filename)
    v.read(vdx_filename)

    # increasing LET should increase RBE
    abx = 10.0  # alpha/beta ratio for x-rays [Gy]
    rbe1 = rbe_mcnamara(dose.cube, let.cube, abx)
    rbe2 = rbe_mcnamara(dose.cube, let.cube, 2.0)

    assert np.all(rbe2 >= rbe1)  # RBE goes up as abx goes down.


def test_rcr():
    """Test RCR model"""
    dose = 2.0  # Gy
    let = 50.0  # keV/um

    sf1 = sf_rcr(dose, let)
    # Survival should always be 0.0 <= sf <= 1.0
    assert 1.0 >= sf1
    assert sf1 >= 0.0

    # add hypoxia, should increase survival
    sf2 = sf_rcr(dose, let, 10.0)  # some oxygenation -> less survival
    assert 1.0 >= sf2
    assert sf2 >= 0.0

    sf1 = sf_rcr(dose, let, 0.0)  # no oxygenation -> much survival
    assert 1.0 >= sf2
    assert sf2 >= 0.0
    assert sf1 >= sf2

    # increase LET, should reduce survival
    sf2 = sf_rcr(dose, let + 10.0)
    assert 1.0 >= sf2
    assert sf2 >= 0.0
    assert sf1 >= sf2
