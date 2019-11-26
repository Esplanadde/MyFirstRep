import functools
import numba
import numpy as np
from scipy import fftpack as fft


def FourierLongitudinalSolver(rho, k, neutralize=True):
    rho_F = fft.fft(rho)
    if neutralize:
        rho_F[0] = 0
    field_F = rho_F / (1j * k)
    field = fft.ifft(field_F).real
    return field


@numba.njit()
def BunemanTransversalSolver(electric_field, magnetic_field, current_yz, dt, c):
    Fplus = 0.5 * (electric_field[:, 1] + c * magnetic_field[:, 2])
    Fminus = 0.5 * (electric_field[:, 1] - c * magnetic_field[:, 2])
    Gplus = 0.5 * (electric_field[:, 2] + c * magnetic_field[:, 1])
    Gminus = 0.5 * (electric_field[:, 2] - c * magnetic_field[:, 1])

    # propagate to front
    Fplus[1:] = Fplus[:-1] - 0.5 * dt * (current_yz[2:-1, 0])
    Gplus[1:] = Gplus[:-1] - 0.5 * dt * (current_yz[2:-1, 1])
    # propagate to back
    Fminus[:-1] = Fminus[1:] - 0.5 * dt * (current_yz[1:-2, 0])
    Gminus[:-1] = Gminus[1:] - 0.5 * dt * (current_yz[1:-2, 1])

    electric_field[:, 1] = Fplus + Fminus
    electric_field[:, 2] = Gplus + Gminus
    magnetic_field[:, 1] = (Gplus - Gminus) / c
    magnetic_field[:, 2] = (Fplus - Fminus) / c


@numba.njit()
def BunemanLongitudinalSolver(electric_field, current_x, dt):
    electric_field[:, 0] -= dt / current_x[:-1]


class Solver:
    def __init__(self, solve_algorithm, initialization_algorithm):
        self.solve = solve_algorithm
        self.init_solver = initialization_algorithm

