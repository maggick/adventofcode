#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

input_file = "test02.txt"
input_file = "input"

if __name__ == '__main__':
    with open(input_file) as f:
        i=0
        instructions=""
        m = {}
        for line in f.readlines():
            if i==0:
                instructions = line.strip()
                i+=1
            elif i==1:
                i+=1
            else:
                m[line.split(' ')[0].strip()]=[line.split(' ')[2][1:-1].strip(),line.split(' ')[3][:-2].strip()]


        #print(instructions)
        #print(m)

        locations = []
        for start in m:
            if start[2]=='A':
                locations.append(start)

        results =[]
        for l in locations:
            i = 0
            while l[2] != "Z":
                for c in instructions:
                    i+=1
                    if c == 'L':
                        l = m[l][0]
                    if c == 'R':
                        l = m[l][1]
            results.append(i)

        print(math.lcm(*results))

