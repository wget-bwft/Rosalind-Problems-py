#Problem:
#A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
#An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

#Given: A DNA string of length at most 1000 nt.

#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

import random

#Random sequence generator
def DNA(length):
    return ''.join(random.choice('CTGA') for _ in range(length))

#Create sequence 
seq = DNA(999)

#Nucleotide count function
def NCOUNT(seq): #define function with seq as argument
    a = seq.count('A') #count occurance of 'A' in the string seq
    t = seq.count('T') #count occurance of 'T' in the string seq
    c = seq.count('C') #count occurance of 'C' in the string seq
    g = seq.count('G') #count occurance of 'G' in the string seq
    print(a,c,t,g) #print the counts

NCOUNT(seq) #execute fucntion
