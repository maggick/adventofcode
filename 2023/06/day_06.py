#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

input_file = "test01.txt"
#input_file = "test02.txt"
input_file = "input"

def compute_sol(t,d):
    sol1=(-t+math.sqrt(t**2-4*d))/-2
    sol2=(-t-math.sqrt(t**2-4*d))/-2
    if math.ceil(sol1)==math.floor(sol1):
        sol1 +=1
        sol2 -=1
    sol1=math.ceil(sol1)
    sol2=math.floor(sol2)
    return sol2-sol1+1

if __name__ == '__main__':
    times = []
    distances = []
    with open(input_file) as f:
        for time in f.readline().split(' '):
            try:
                times.append(int(time.strip()))
            except ValueError:
                pass
        for distance in f.readline().split(' '):
            try:
                distances.append(int(distance.strip()))
            except ValueError:
                pass

    if len(times) != len(distances):
        print("error loading times and distances")
        exit()

    i = 0
    result = 1
    while i<len(times):
        result = result *(compute_sol(times[i],distances[i]))
        i+=1
    print(result)

