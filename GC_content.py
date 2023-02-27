#Problem:

#The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, 
#the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

#DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling 
#is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some 
#labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the 
#label of the next string.

#In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", 
#where "xxxx" denotes a four-digit code between 0000 and 9999.

#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
#Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see 
#the note on absolute error below.

import random

#Random sequence generator
def DNA(length_nuc):
    return ''.join(random.choice('CTGA') for _ in range(length_nuc))

#Random fasta generator
def gen_fasta(seq_name, seq_id, length_nuc, length_fasta):
    fasta = '' #create empty variable
    for x in range(length_fasta): #for loop looping through length_fasta argument
        seq = '>'+str(seq_name)+str(seq_id)+'\n'+DNA(length_nuc) + '\n' #create each new sequence within the fasta
        fasta += seq #concatonate sequence into fasta
        seq_id += 1 #iterate the ID
    return fasta

fasta = gen_fasta('Rosalind_', 0, 210, 10)

print(fasta)

def gc_content(fasta):
    sequences = [] #list to store sequences and id
    current_sequence = ''
    current_id = ''

    for line in fasta.split('\n'): #iterate over the lines in the fasta string
        if line.startswith('>'): #if line is header line
            if current_sequence != '':  #if not first sequence, append to list
                sequences.append((current_id, current_sequence))
            current_id = line.strip()[1:]  #extract ID and remove ">" character
            current_sequence = ''  #reset sequence string
        else:
            current_sequence += line.strip()

    #append last sequence to list
    if current_sequence != '':
        sequences.append((current_id, current_sequence))
    
    gc_dict = {} #initialize an empty dictionary to store sequence IDs and their corresponding GC contents

    for seq_tuple in sequences: #loop through the list of sequence ID and sequence tuples

        seq_id = seq_tuple[0] #Extract the sequence ID and sequence string from the tuple
        seq_string = seq_tuple[1]
        gc_count = seq_string.count('G') + seq_string.count('C')#count the number of G and C nucleotides in the sequence
        gc_content = (gc_count / len(seq_string)) * 100 #calculate the GC content as a percentage of the total nucleotides in the sequence
        gc_dict[seq_id] = gc_content #add id and gc content to dictionary
    return gc_dict


print(gc_content(fasta))














