#!/usr/bin/env python3
# -*- coding: utf-8 -*-


input_file = "test01.txt"
input_file = "input"

if __name__ == '__main__':
    with open(input_file) as f:
        seeds = []
        status = []
        current_load = 'seeds'
        previous_load = 'seeds'
        for line in f.readlines():
            if 'map' in line:
                previous_load = current_load
                current_load = line
                j = 0
                while j<len(status):
                    status[j] = previous_load
                    j+=1
            elif line.strip() == '':
                pass
            elif current_load == 'seeds':
                i = 1
                while i < len(line.split(' ')):
                    j = 0
                    while j < int(line.split(' ')[i+1].strip()):
                        status.append(current_load.strip())
                        seeds.append(j+int(line.split(' ')[i].strip()))
                        j+=1
                    i+=2
                #print(seeds)
            else:
                dest = int(line.split(' ')[0].strip())
                source = int(line.split(' ')[1].strip())
                rang = int(line.split(' ')[2].strip())

                i = 0
                while i<len(seeds):
                    if source <=seeds[i] < source+rang and status[i] == previous_load:
                        seeds[i] = seeds[i]-source+dest
                        status[i] = current_load
                    i+=1

        #print(seeds)
        lowest = seeds[0]
        for seed in seeds:
            if seed < lowest:
                lowest = seed
        print(lowest)



