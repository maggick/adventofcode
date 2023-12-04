#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

input_file = "test01.txt"
#input_file = "test02.txt"
input_file = "input"

symbols = ['*']

if __name__ == '__main__':
    with open(input_file) as f:
        sum = 0
        schema=[]
        for line in f.readlines():
            schema.append(line)

        i = 0
        for line in schema:
            for match in re.finditer(r'\*', line):
                gear = []
                start = match.start()
                end = match.end()
 
                for match_g in re.finditer(r'\d+', schema[i]):
                    if match_g.start()==end or match_g.end()==start:
                        gear.append(match_g.group())

                try:
                    for match_g in re.finditer(r'\d+', schema[i-1]):
                        if  match_g.start()-1<= start <= match_g.end() :
                            gear.append(match_g.group())
                except IndexError:
                    pass

                try:
                    for match_g in re.finditer(r'\d+', schema[i+1]):
                        if  match_g.start()-1<= start <= match_g.end() :
                            gear.append(match_g.group())
                except IndexError:
                    pass

                if len(gear) == 2:
                    sum += int(gear[0])*int(gear[1])

                print ("{}: {},{}: {}".format(match.group(), match.start(), match.end(), gear))
            i+=1

    print (sum)

