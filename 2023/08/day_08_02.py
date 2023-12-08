#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_file = "test02.txt"
input_file = "input"

def isNotOver(locations):
    for elem in locations:
        if elem[2] != 'Z':
            return True
    return False

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


        print(instructions)
        print(m)

        locations = []
        for start in m:
            if start[2]=='A':
                locations.append(start)
        i = 0
        while isNotOver(locations):
            for c in instructions:
                j = 0
                i+=1
                while j< len(locations):
                    d = m[locations[j]]
                    if c == 'L':
                        d2 = d[0]
                        locations[j] = m[locations[j]][0]
                    if c == 'R':
                        d2 = d[1]
                        locations[j] = m[locations[j]][1]
                    j+=1

        print (i)




