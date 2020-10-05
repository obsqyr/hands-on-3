import sys, unittest
from md import calcenergy
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units
from asap3 import Trajectory
from asap3 import EMT
from numpy import *

class MdTests(unittest.TestCase):
    def test_calcenergy(self):
        use_asap = True

        # Set up a crystal
        atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                                  symbol="Cu",
                                  size=(3, 3, 3),
                                  pbc=True)

        # Describe the interatomic interactions with the Effective Medium Theory
        atoms.calc = EMT()
        
        # Set the momenta corresponding to T=300K
        #MaxwellBoltzmannDistribution(atoms, 300 * units.kB)

        for i, a in enumerate(atoms):
            a.momentum = array([0, -2*i, 0])

        
        epot, ekin, t = calcenergy(atoms)

        self.assertTrue(abs(epot - (- 0.0006011545839377735)) < 0.000000000000001, "epot not correct")
        self.assertTrue(abs(ekin - 120.67373765985793) < 0.000000000000001, "ekin not correct")
        self.assertTrue(abs(t - 933574.033856577)< 0.000000000001, "t not correct") 

if __name__ == '__main__':
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())
