#!/usr/bin/env python3
# -*- coding: utf-8 -*-


input_file = "test01.txt"
input_file = "input"


if __name__ == '__main__':
    with open(input_file) as f:
        sum = 0
        for line in f.readlines():
            constrain = { 'red': 0, 'green':0, 'blue': 0}
            gameId = int(line.split(':')[0].split(' ')[1])
            gameGrabs = line.split(':')[1].split(';')
            for grab in gameGrabs:
                for detail in grab.split(','):
                    number = int(detail.split(' ')[1])
                    color = detail.split(' ')[2].strip()
                    if number>constrain[color]:
                        constrain[color]=number
            power = constrain['red']*constrain['green']*constrain['blue']
            sum+=power
        print(sum)


