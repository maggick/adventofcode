#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

input_file = "test01.txt"
#input_file = "test02.txt"
input_file = "input"

symbols = ['!','"','#','$','%','&','’','(',')','*','+',',','-','/',':',';','<','=','>','?','@','[',']','^','_','`','{','|','}','~']

if __name__ == '__main__':
    with open(input_file) as f:
        sum = 0
        schema=[]
        for line in f.readlines():
            schema.append(line)

        i = 0
        for line in schema:
            for match in re.finditer(r'\d+', line):
                is_number = 0
                start = match.start()-1
                end = match.end()+1
                if match.start()-1<0:
                    start = 0
                if match.end()+1>len(line):
                    end = len(line)
                try:
                    for char in schema[i+1][start:end]:
                        if char in symbols:
                            is_number = 1
                except IndexError:
                    pass
                try:
                    for char in schema[i-1][start:end]:
                        if char in symbols:
                            is_number = 1
                except IndexError:
                    pass
                if line[match.start()-1] in symbols:
                    is_number = 1
                if line[match.end()] in symbols:
                    is_number = 1
                print ("{}: {},{}: {}".format(match.group(), match.start(), match.end(), is_number))
                if is_number:
                    sum+= int(match.group())
            i+=1

    print (sum)

