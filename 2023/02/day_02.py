#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import regex as re

input_file = "test01.txt"
#input_file = "test02.txt"
input_file = "input"

constrain = { 'red': 12, 'green':13, 'blue': 14}

if __name__ == '__main__':
    with open(input_file) as f:
        sum = 0
        gameId=0
        for line in f.readlines():
            gameId = int(line.split(':')[0].split(' ')[1])
            gameGrabs = line.split(':')[1].split(';')
            for grab in gameGrabs:
                for detail in grab.split(','):
                    number = int(detail.split(' ')[1])
                    color = detail.split(' ')[2].strip()
                    if number>constrain[color]:
                        gameId=0

            sum+= gameId

    print (sum)

