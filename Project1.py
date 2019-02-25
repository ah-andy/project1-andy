import math
import numpy as np
import time

L = 1
g = 9.81



def system_update(omega_i, angle_i, angle_t, time1, time2):
    dt = time2 - time1
    angle = angle_i + (omega_i * dt)
    accel_i = (-g / L * math.sin(omega_i) )
    omega = omega_i + (accel_i * dt)
    accel_t = ((-1 * g) / L ) * math.sin(angle)
    return angle, accel_t, omega

def print_system(time, omega_i, accel_i, angle_i):
    print("TIME:   ", time)
    print("POSITION:   ", angle_i)
    print("ACCELERATION:   ", accel_i)
    print("VELOCITY: ", omega_i, "\n")
    print((time, angle_i, accel_i, omega_i))

#initial conditions
angle_i = [math.pi]
omega_i = [5]
accel_i = [0]
time = np.linspace(0, 20, 50)
print_system(time[0], omega_i[0], accel_i[0], angle_i[0])

i = 1
while i < len(time):
    accel_t, angle, omega = system_update(omega_i[i-1], angle_i[i-1], accel_i[i-1], time[i-1], time[i])
    omega_i.append(omega)
    angle_i.append(angle)
    accel_i.append(accel_t)
    print_system(time[i], omega_i[i], accel_i[i], angle_i[i])
    i = i + 1