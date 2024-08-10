from math import *
from utils import *

ms = {'sh_stress': 40, 'ten_stress': 90}
ci = {'sh_stress': 15}


# Input from the user
speed = int(input("Enter the expected rotational speed of the shaft [rpm]: "))
power = int(input("Enter the power, the shaft is expected to transmit [kW]: "))

# Calculation of Mt with Power formula
Mt = ((60 * (power * 1000)) / (2 * pi * speed)) * 1000 # to convert the unit to Nmm

ms_ss_a = ms.get('sh_stress')
ci_ss_a = ci.get('sh_stress')
ms_ts_a = ms.get('ten_stress')

# Calculation of Shaft Diameter "d"
d = ((Mt * 16) / (pi * ms_ss_a)) ** (1/3)
d = convert_to_std_d(d)
print(f"Diameter of the Shaft = {d}")

D = find_D(d, Mt, ci_ss_a)
print(f"Diameter of the Hub = {D}")

Tf = find_Tf(d, D, Mt, ci_ss_a)
print(f"Thickness of the Flange = {Tf}")

key_w = find_key(d)[0]
key_h = find_key(d)[1]

print(f"Key Thickness = {key_h}")
print(f"Key Width = {key_w}")

key_l = find_l(d, key_w, key_h, Mt, ms_ss_a, ms_ts_a)
print(f"Key Length = {key_l}")

n = find_bolt(d, Mt, Tf, ms_ss_a, ms_ts_a)[0]
D1 = find_bolt(d, Mt, Tf, ms_ss_a, ms_ts_a)[1]
d1 = find_bolt(d, Mt, Tf, ms_ss_a, ms_ts_a)[2]
d1 = convert_to_std_d(d1)

print(f"Number of Bolts = {n}")
print(f"Diameter of the Bolt Circle = {D1}")
print(f"Bolt Diameter = {d1}")

print(f"Outer Diameter = {4 * d}")
print(f"Length of the Hub = {1.5 * d}")
print(f"Thickness of the Protected Flange = {0.25 * d}")
