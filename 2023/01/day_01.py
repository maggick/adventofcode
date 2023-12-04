#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

input_file = "input"
#input_file = "test01.txt"
input_file = "test02.txt"

if __name__ == '__main__':
    with open(input_file) as f:
        sum = 0
        for line in f.readlines():
            line_numbers = re.findall(r'\d', line)
            digit = line_numbers[0] + line_numbers[-1]
            sum += int(digit)
        print (sum)

