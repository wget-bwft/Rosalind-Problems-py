#Problem:

#An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

#Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

#Given: A DNA string t having length at most 1000 nt.

#Return: The transcribed RNA string of t.

import random

#Random sequence generator
def DNA(length):
    return ''.join(random.choice('CTGA') for _ in range(length))

#Create sequence 
seq = DNA(999)

def DNA2RNA(seq):
    RNA = seq.replace('T','U') #python strings are immutable, .replace('old text', 'new text')
    print(RNA)

DNA2RNA(seq)