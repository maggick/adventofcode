#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_file = "test01.txt"
input_file = "test02.txt"
input_file = "input"

def move(pos, d):
    #d → direction: 0→right, 1→ down, 2→ left, 3→up
    if map[pos] == "S" and d==0:
        d=0
    #We turn on this pipes
    #print(map[pos])
    match map[pos]:
        case "F":
            if d == 3: d=0
            elif d == 2: d=1
        case "L":
            if d== 1: d=0
            elif d==2:d=3
        case "7":
            if d==3: d=2
            elif d==0: d=1
        case "J":
            if d==1: d=2
            elif d==0: d=3
        case ".":
            print('bug')
            exit()

    match d:
        case 0:
            pos=(pos[0]+1,pos[1])
        case 1:
            pos=(pos[0],pos[1]+1)
        case 2:
            pos=(pos[0]-1,pos[1])
        case 3:
            pos=(pos[0],pos[1]-1)

    return pos,d


if __name__ == '__main__':
    #load map
    map = dict()
    start = (0,0)
    i=0
    with open(input_file) as f:
        for line in f.readlines():
            j=0
            for c in line.strip():
                map[j,i] = c
                if c == "S":
                    start = (j,i)
                j+=1
            i+=1


    #print(map)
    #print(start)

    #find paths
    pos = start
    d0 = 0
    max=0
    while d0<4:
        count = 0
        d=d0
        while True:
            pos,d=move(pos, d)
            #print (pos, d)
            if pos == start:
                break
            count+=1

        if count>max:
            max = count
        d0+=1

    #find longest path
    print (max/2)

