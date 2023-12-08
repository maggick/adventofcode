#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque

input_file = "test01.txt"
input_file = "input"
input_file = "test02.txt"
input_file = "input"

order = deque(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'])


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
    print(cards)
    for card in cards:
        if card !='J':
            if cards[card]>score:
                score = cards[card]
            if cards[card]==2:
                pair+=1
            if cards[card]==3:
                full+=1
            if cards[card]==4:
                score =5
            if cards[card]==5:
                return 6

    J = 0
    try:
        J = cards['J']
        print("J: {}".format(J))
        print("score: {}".format(score))
    except KeyError:
        pass

    print(hand,J)

    # 5 J
    if J == 5:
        return 6

    if score == 3 and J == 1:
        return 5

    if score == 3 and J == 2:
        return 6

    # four of a kind + J → five of a kind
    if score == 5 and J ==1:
        return 6

    if pair==1 and full==1:
        #full
        return  4
    if pair==2 and J ==1:
        # two pairs + J → full
        return 4
    if pair==2:
        #two pairs
        return 2
    if score ==1 and J == 0:
    # high card
        return 0
    if score == 1 and J ==1:
        #pair
        return 1
    if score == 1 and J ==2:
        #three
        return 3
    if score == 1 and J ==3:
        #four
        return 5
    if score == 1 and J ==4:
        #five
        return 6

    if score == 2 and J == 0:
        #pair
        return 1
    if score == 2 and J ==1:
        #pair +J → three of a kind
        return 3
    if score == 2 and J ==2:
        #pair
        return 5
    if score == 2 and J ==3:
        #pair
        return 6

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
        print("score: {}".format(hand_score['JJJ8J']))
        print("compute")
        print(compute_score('JJJ8J'))

