"""

Test optimizing GP utility functions.

@author: David P. Fleming [University of Washington, Seattle], 2018
@email: dflemin3 (at) uw (dot) edu

"""

import numpy as np
import george
from approxposterior import utility as ut, gpUtils, likelihood as lh


def testInitGP():
    """
    Test default GP initialization.

    Parameters
    ----------

    Returns
    -------
    """

    # For reproducibility
    m0 = 50
    seed = 57
    np.random.seed(seed)

    # Randomly sample initial conditions from the prior
    theta = np.array(lh.rosenbrockSample(m0))

    # Evaluate forward model log likelihood + lnprior for each theta
    y = np.zeros(len(theta))
    for ii in range(len(theta)):
        y[ii] = lh.rosenbrockLnlike(theta[ii]) + lh.rosenbrockLnprior(theta[ii])

    # Set up a gp with a ExpSquaredKernel
    gp = gpUtils.defaultGP(theta, y)

    errMsg = "ERROR: Default initialization with incorrect parameters!"
    true = [-31.02658091, -0.34657359, -0.34657359]
    assert np.allclose(true, gp.get_parameter_vector()), errMsg

    return None
# end function

if __name__ == "__main__":
    testInitGP()
