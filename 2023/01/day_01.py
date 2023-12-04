#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import regex as re

input_file = "test01.txt"
input_file = "test02.txt"
input_file = "input"

numbers= {
        "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6",
        "seven":"7", "eight":"8", "nine":"9"
      }


if __name__ == '__main__':
    with open(input_file) as f:
        sum = 0
        for line in f.readlines():
            line_numbers = re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True)
            try:
                d1=numbers[line_numbers[0]]
            except KeyError:
                d1=line_numbers[0]
            try:
                d2=numbers[line_numbers[-1]]
            except KeyError:
                d2=line_numbers[-1]
            digit = d1+d2
            print(digit)
            sum += int(digit)
    print (sum)

