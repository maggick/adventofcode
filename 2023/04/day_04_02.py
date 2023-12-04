#!/usr/bin/env python3
# -*- coding: utf-8 -*-

input_file = "test01.txt"
#input_file = "test02.txt"
input_file = "input"

if __name__ == '__main__':
    with open(input_file) as f:
        scratchcard = 0
        card_score = []
        how_much_card=[]
        # evaluate card score
        for line in f.readlines():
            how_much_card.append(1)
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
                        score += 1
            card_score.append(score)

        print (card_score)
        i = 0
        while i<len(card_score):
            n = 1
            while n<=how_much_card[i]:
                j = 0
                while j < card_score[i]:
                    how_much_card[i+j+1]+=1
                    j+=1
                n+=1
            i+=1


    print (how_much_card)
    score = 0
    for n in how_much_card:
        score +=n
    print (score)

