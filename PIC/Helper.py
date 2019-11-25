import numpy as np


def plasma_parameter(N_particles, N_grid, dx):
    return (N_particles / N_grid) * dx


def calculate_number_timesteps(T, dt):
    return int(T / dt) + 1



