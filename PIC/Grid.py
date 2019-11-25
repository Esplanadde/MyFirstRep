import numpy as np
import BoundaryCondition
import scipy.fftpack
import Helper
import field_interpolation


class Grid:

    def __init__(self, T: float, L: float, NG: int, c: float = 1, bc=BoundaryCondition.BC()):

        self.c = c
        self.x, self.dx = np.linspace(0, L, NG, retstep=True, endpoint=False, dtype=np.float64)
        self.x_interpolation = np.arange(NG+2)*self.dx - self.dx

        self.dt = self.dx / c
        self.T = T
        self.NT = Helper.calculate_number_timesteps(T, self.dt)

        self.charge_density = np.zeros(NG + 1, dtype=np.float64)
        self.current_density_x = np.zeros((NG + 3), dtype=np.float64)
        self.current_density_yz = np.zeros((NG + 4, 2), dtype=np.float64)
        self.electric_field = np.zeros((NG + 2, 3), dtype=np.float64)
        self.magnetic_field = np.zeros((NG + 2, 3), dtype=np.float64)

        self.L = L
        self.NG = NG

        self.bc = bc
        self.k = 2 * np.pi * scipy.fftpack.fftfreq(self.NG, self.dx)
        self.k[0] = 0.0001

        self.list_species = []
        self.postprocessed = False
        self.postprocessed_fourier = False
        self.periodic = None


class PeriodicGrid(Grid):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.interpolator = field_interpolation.PeriodicInterpolateField
        self.periodic = True

