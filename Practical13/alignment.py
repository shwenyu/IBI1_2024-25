import blosum as bl #use the blosum module for scoring !!!!! if don't have it, install it using pip install blosum
# This script reads protein sequences from FASTA files and aligns them using the BLOSUM62 scoring matrix.
import os
os.chdir('Practical13') # Change the working directory to 'Practical13'
# Import the BLOSUM matrix for scoring
matrix = bl.BLOSUM(62) # Define a function to read protein sequences from a FASTA file

def read_fasta(file_path):
    protein = ''
     # Open the FASTA file for reading
    with open(file_path, 'r') as file:
        for line in file:  # Iterate through each line in the file
            line = line.strip()  # Remove leading/trailing whitespace from the line
            if line.startswith('>'):  # Check if the line is a header line
                continue # Skip header lines
            else:  # If the line is a sequence line
                protein += line
    return protein  # Return the protein sequence

def align(seq1, seq2): # Function to align two sequences
    length = len(seq1) # Get the length of the sequences
    score = 0 # Initialize score to 0
    edit_distance = 0 # Initialize edit distance to 0
    for i in range(length): # Iterate through each position in the sequences
        val = matrix[seq1[i]][seq2[i]] # Get the score from the BLOSUM matrix
        if seq1[i] != seq2[i]: # If the characters are different
            edit_distance += 1 # Increment edit distance
        score += val # Add the score to the total score
    identity = (length - edit_distance) / length # Calculate identity
    return score, identity # Read the protein sequences from the FASTA files

# Read the protein sequences from the FASTA files
human = read_fasta('human.fasta')
mouse = read_fasta('mouse.fasta')
random = read_fasta('random.fasta')

score_human_mouse, identity_human_mouse = align(human, mouse)
score_human_random, identity_human_random = align(human, random)
score_mouse_random, identity_mouse_random = align(mouse, random)
# Print the alignment scores and identities
print(f"Mouse vs Human: Score = {score_human_mouse}, Identity = {identity_human_mouse*100:.2f}%")
print(f"Human vs Random: Score = {score_human_random}, Identity = {identity_human_random*100:.2f}%")
print(f"Mouse vs Random: Score = {score_mouse_random}, Identity = {identity_mouse_random*100:.2f}%")
