# -*- coding: utf-8 -*-
import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

from random import randrange
from random import seed
from time import time

seed(int(time() * 1000))

GOAT = 0
CAR = 1


def problem(cnt):
    doors = [GOAT] * cnt
    answer = randrange(cnt)
    doors[answer] = CAR
    return (doors, answer)


def select(cnt):
    return randrange(cnt)


def last_other_door(doors, answer, selected):
    if answer == selected:
        for i in range(len(doors)):
            if i != selected:
                return i
    else:
        return answer
    raise Exception('invalid state')


def montyhall(cnt, change):
    doors, answer = problem(cnt)
    selected = select(cnt)
    other = last_other_door(doors, answer, selected)
    if change:
        selected = other
    return doors[selected] == CAR


def monte_carlo(sim_cnt, door_cnt, door_change):
    i = 0
    answer_cnt = 0
    while i < sim_cnt:
        if montyhall(door_cnt, door_change):
            answer_cnt = answer_cnt + 1
        i = i + 1
    return float(answer_cnt) / sim_cnt

#http://happinessoncode.com/2018/02/04/montyhall-problem/
