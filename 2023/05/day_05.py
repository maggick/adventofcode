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
                for seed in line.split(' '):
                    status.append(current_load.strip())
                    if seed != 'seeds:':
                        seeds.append(int(seed.strip()))
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

        print(seeds)
        lowest = seeds[0]
        for seed in seeds:
            if seed < lowest:
                lowest = seed
        print(lowest)



