#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_file = "test01.txt"
#input_file = "test02.txt"
input_file = "input"


if __name__ == '__main__':
    with open(input_file) as f:
        sum = 0
        for line in f.readlines():
            score = 0
            my_numbers = []
            winning_numbers = []
            for elem in line.split('|')[1].strip().split(' '):
                if elem != '':
                    my_numbers.append(int(elem.strip()))
            for elem in line.split('|')[0].strip().split(':')[1].strip().split(' '):
                if elem != '':
                    winning_numbers.append(int(elem.strip()))

            for elem in my_numbers:
                if elem in winning_numbers:
                    if score == 0:
                        score = 1
                    else:
                        score = score * 2
            sum += score

    print (sum)

