import blosum as bl
import os
os.chdir('Practical13')
# Import the BLOSUM matrix for scoring
matrix = bl.BLOSUM(62)

def read_fasta(file_path):
    protein = ''
     # Open the FASTA file for reading
    with open(file_path, 'r') as file:
        for line in file:  # Iterate through each line in the file
            line = line.strip()  # Remove leading/trailing whitespace from the line
            if line.startswith('>'):  # Check if the line is a header line
                continue
            else:  # If the line is a sequence line
                protein += line
    return protein  # Return the protein sequence

def align(seq1, seq2):
    length = len(seq1)
    score = 0
    edit_distance = 0
    for i in range(length):
        val = matrix[seq1[i]][seq2[i]]
        if seq1[i] != seq2[i]:
            edit_distance += 1
        score += val
    identity = (length - edit_distance) / length 
    return score, identity

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
