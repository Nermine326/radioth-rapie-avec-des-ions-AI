

import numpy as np
import logging

logger = logging.getLogger(__name__)


def tcp_voi(sf, voi=None, ncells=1.0, fractions=1):
    """
    Returns TCP within VOI.
    If VOI is not give, TCP of entire cube is calculated.
    This is equation (7) in https://doi.org/10.1093/jrr/rru020
    assuming static oxygenation during all fractions.
    (Equation (8) would require a new oxy cube after every fractionation, not implemented.)

    :params numpy.array sf: numpy array, surviving fraction cube
    :params Voi voi: pytrip Voi() class object
    :params float ncells: number of cells in each voxel, or a cube of surviving fractions
    :params int fractions: number of fractions, default is 1
    """

    tcp = 0

    if voi is None:
        mask = None
    else:
        # mark ony those values as true, which are within the VOI
        voi_cube = voi.get_voi_cube()
        mask = (voi_cube.cube == 1000)

    # ncells may be either a scalar or a cube.
    if np.isscalar(ncells):
        tcp = np.exp(-sum(ncells * sf[mask]**fractions))
    else:
        # better make sure that the cells cube has the same size as the surviving fraction cube
        if ncells.shape == sf.shape:
            tcp = np.exp(-sum(ncells[mask] * sf[mask]**fractions))
        else:
            logger.error("ncells array shape does not match surviving fraction shape.")

    return tcp
