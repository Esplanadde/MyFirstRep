import numpy as np
from numba import njit


@njit()
def PeriodicInterpolateField(x_particles, scalar_field, dx: float):
    logical_coordinates = (x_particles / dx).astype(np.int32)
    NG = scalar_field.shape[0] - 2
    right_fractions = (x_particles / dx - logical_coordinates).reshape((x_particles.size, 1))
    field = (1 - right_fractions) * scalar_field[logical_coordinates + 1] + \
            right_fractions * scalar_field[(logical_coordinates + 1) % NG + 1]
    return field
