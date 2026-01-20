import numpy as np

class TrussAnalysis:
    def __init__(self, E, A, L, theta):
        self.E = E  # Young's Modulus
        self.A = A  # Cross-sectional Area
        self.L = L  # Length
        self.c = np.cos(np.radians(theta))
        self.s = np.sin(np.radians(theta))

    def local_stiffness(self):
        """Calculates the 4x4 local stiffness matrix for a truss element."""
        k = (self.E * self.A / self.L)
        cc, ss, cs = self.c**2, self.s**2, self.c*self.s
        return k * np.array([
            [ cc,  cs, -cc, -cs],
            [ cs,  ss, -cs, -ss],
            [-cc, -cs,  cc,  cs],
            [-cs, -ss,  cs,  ss]
        ])
