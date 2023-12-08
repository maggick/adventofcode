#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque

input_file = "test01.txt"
#input_file = "test02.txt"
input_file = "input"

order = deque(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'])


def compute_score(hand):
    cards = {}
    for card in hand:
        if card in cards:
            cards[card]+=1
        else:
            cards[card]=1

    score = 0
    pair = 0
    full = 0
    for card in cards:
        if cards[card]>score:
            score = cards[card]
        if cards[card]==2:
            pair+=1
        if cards[card]==3:
            full+=1
        if cards[card]==4:
            score =5
        if cards[card]==5:
            score =6

    if pair==1 and full==1:
        score = 4
        #full
    elif pair==2:
        score = 2
        #two pair
    else:
        if score ==1:
            # high card
            score =0
        if score == 2:
            #pair
            score =1

    return(score)

def weaker(hand1, hand2,hand_score):
    if hand_score[hand1]>hand_score[hand2]:
        return False
    if hand_score[hand1]<hand_score[hand2]:
        return True

    if hand_score[hand1]==hand_score[hand2]:
        i=0
        while i<len(hand1):
            if order.index(hand1[i])>order.index(hand2[i]):
                return True
            if order.index(hand1[i])<order.index(hand2[i]):
                return False
            i+=1

    return False



if __name__ == '__main__':
    with open(input_file) as f:
        hand_bids ={}
        for line in f.readlines():
            hand_bids[(line.split(' ')[0].strip())]=line.split(' ')[1].strip()

        hand_score ={}
        hands_ranked = deque()
        for hand in hand_bids:
            hand_score[hand]=compute_score(hand)


            if len(hands_ranked)==0:
                hands_ranked.append(hand)
            elif not weaker(hand,hands_ranked[len(hands_ranked)-1],hand_score):
                hands_ranked.append(hand)
            else:
                for hand_ranked in hands_ranked:
                    if weaker(hand, hand_ranked,hand_score):
                        hands_ranked.insert(hands_ranked.index(hand_ranked),hand)
                        break

        i=0
        score = 0
        for hand_ranked in hands_ranked:
            i+=1
            score += i*int(hand_bids[hand_ranked])


        print(hands_ranked)
        print(score)

