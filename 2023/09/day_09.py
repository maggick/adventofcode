#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_file = "test01.1.txt"
input_file = "test01.txt"
input_file = "input"

def stop(seq):
    for elem in seq:
        if elem != 0:
            return False
    return True

if __name__ == '__main__':
    with open(input_file) as f:
        sum = 0
        sub = 0
        for line in f.readlines():
            seq=[]
            seqs=[]
            for elem in line.split(' '):
                seq.append(int(elem.strip()))

            seqs.append(seq)

            while not stop(seqs[-1]):
                i=0
                diff =[]
                while i<len(seq)-1:
                    diff.append(seq[i+1]-seq[i])
                    i+=1

                seq = diff
                seqs.append(diff)

            for seq in seqs:
                sum+=seq[-1]

            i = len(seqs)-1
            subsub = 0
            while i>0:
                subsub = seqs[i-1][0]-subsub
                i-=1

            sub += subsub
    print (sum)
    print (sub)

