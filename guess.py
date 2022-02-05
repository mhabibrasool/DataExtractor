# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:02:38 2020

@author: HP
"""


from random import randint

secret_num = randint(1, 10)
num_guesses = 0
guess = 0

while guess != secret_num and num_guesses <= 4:
    guess = eval(input('Enter your guess (1-100) :'))
    num_guesses = num_guesses+1
    if guess < secret_num:
        print('HIGHER.',
              5-num_guesses, 'guesses left.\n')
    elif guess > secret_num:
        print('LOWER.',
              5-num_guesses, 'guesses left.\n')
    else:
        print('You got it.')
        
if num_guesses==5 and guess != secret_num:
    print('You lose. The correct number is', secret_num)
    