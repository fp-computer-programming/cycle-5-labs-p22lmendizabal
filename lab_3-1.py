# author: LM (AMDG) 10/25/21
from math import pow
from time import process_time, perf_counter
t0 = perf_counter()
(2 ** 2)
t1 = perf_counter()
speed = t1 - t0
print(speed)

t2 = perf_counter()
pow(2, 2)
t4 = perf_counter()
speed2 = t4 -t2
print(speed2)
print(speed2 - speed)