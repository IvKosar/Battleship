#!/usr/bin/env python
# coding=utf-8
# course: Programming Fundamentals
# laboratory: 1
# date: 01/02/17
# username: petruk
# name: Marian Petruk
# description: Battleship game

from field.create_field import *
from field.field_tools import *
from ship.ship import *

# field = read_field('field.txt')
# print(field)


field = generate_valid_field()

print('----------')
print(field_to_str(field))
print('----------')
