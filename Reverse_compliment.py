#Problem:

#In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

#The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

#Given: A DNA string s of length at most 1000 bp.

#Return: The reverse complement sc of s.

import random

#Random sequence generator
def DNA(length):
    return ''.join(random.choice('CTGA') for _ in range(length))

#Create sequence 
seq = DNA(999)

# to replace multiple values at once we need to create a dictionary to store more than one value
replace_dict1 = {'A':'1', 'T':'2', 'C':'3', 'G':'4'}
replace_dict2 = {'1':'T', '2':'A', '3':'G', '4':'C'}


def REVCOMP(seq, replace_dict1, replace_dict2):
    for i, j in replace_dict1.items(): #loop through items in dictionary1
        seq = seq.replace(i, j)

    for i, j in replace_dict2.items(): #loop through items in dictionary2
        seq = seq.replace(i, j)

    seq = seq[::-1] #reverse string
    print(seq)

REVCOMP(seq, replace_dict1, replace_dict2)