#!/usr/bin/env python

import re

def parse_player(data):
    return list(map(int, re.findall(r'\d+', data)))[1:]

def part1(data):
    player1, player2 = map(parse_player, data.split('\n\n'))
    while player1 and player2:
        p1 = player1.pop(0)
        p2 = player2.pop(0)
        if p1 > p2:
            player1.extend([p1, p2])
        else:
            player2.extend([p2, p1])
    return win_score(player1, player2)

def win_score(player1, player2):
    winner = player1 or player2
    return sum(a*(len(winner) - i) for i, a in enumerate(winner))

def play(player1, player2):
    played = set()
    while player1 and player2:
        pair = (player1, player2)
        if pair in played:
            return pair
        played.add(pair)
        p1, player1 = player1[0], player1[1:]
        p2, player2 = player2[0], player2[1:]
        if len(player1) >= p1 and len(player2) >= p2:
            s1, _ = play(player1[:p1], player2[:p2])
            p1win = bool(s1)
        else:
            p1win = p1 > p2
        if p1win:
            player1 += (p1, p2)
        else:
            player2 += (p2, p1)
    return player1, player2

def part2(data):
    player1, player2 = map(parse_player, data.split('\n\n'))
    player1, player2 = play(tuple(player1), tuple(player2))
    return win_score(player1, player2)

if __name__ == '__main__':
    data = open('input22.txt').read()
    print(part1(data))
    print(part2(data))
