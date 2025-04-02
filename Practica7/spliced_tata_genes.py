import re  # Import the regular expression module
splice_comb = input("What is your splice_combination (GTAG, GCAG,ATAC):")  # Get splice combination from user input
file_path = "tata_genes.fa"  # Define the file path for the input FASTA file
donor = splice_comb[0:2]  # Extract donor sequence from splice_combination
acceptor = splice_comb[2:4]  # Extract acceptor sequence from splice_combination

def read_fasta(file_path):
    # Function to read a FASTA file and return a dictionary of gene sequences
    genes = {}  # Initialize a dictionary to store gene sequences
    current_gene = None  # Variable to track the current gene being read
    
    with open(file_path, 'r') as file:  # Open the FASTA file for reading
        for line in file:  # Iterate through each line in the file
            line = line.strip()  # Remove leading/trailing whitespace
            if line.startswith('>'):  # Check if the line is a header
                if current_gene is not None:  # If a gene is being tracked, save its sequence
                    genes[current_gene] = ''.join(genes[current_gene])  # Join sequence parts
                current_gene = line[1:]  # Extract gene name (remove '>')
                genes[current_gene] = []  # Initialize sequence list for the gene
            else:  # If the line is a sequence
                if current_gene is not None:  # Ensure a gene is being tracked
                    genes[current_gene].append(line)  # Append sequence part to the gene

        # Save the last gene after finishing the file
        if current_gene is not None:
            genes[current_gene] = ''.join(genes[current_gene])

        return genes

'''def splice(seq):
    global donor, acceptor
    donor_matches = re.finditer(donor, seq)
    acceptor_matches = re.finditer(acceptor, seq)
    donor_positions = [match.start() for match in donor_matches]
    acceptor_positions = [match.start() for match in acceptor_matches]
    i, j = 0, 0
    if len(donor_positions) > 0 and len(acceptor_positions) > 0:
        spliced_d_pos = [-2, donor_positions[0]]
        spliced_a_pos = [acceptor_positions[0]]
    while j < len(acceptor_positions):
        while i < len(donor_positions):
            if acceptor_positions[j] > donor_positions[i]:
                i += 1
                continue
            spliced_d_pos.append(donor_positions[i])
            i += 1
            break
        j += 1
        while j < len(acceptor_positions):
            if acceptor_positions[j] < spliced_d_pos[-1]:
                j += 1
                continue
            spliced_a_pos.append(acceptor_positions[j])
            break
    #print(spliced_a_pos)
    if not spliced_a_pos is None and not spliced_d_pos is None:
        spliced_pos = spliced_d_pos.extend(spliced_a_pos)
    if not spliced_pos is None :
        spliced_pos = sorted(spliced_pos)   
        new_seq = ""
        for i in range(len(spliced_pos)-1):
            if i % 2 == 0:
                new_seq += seq[spliced_pos[i]+2:spliced_pos[i+1]]
    else:
        new_seq = seq
    return(new_seq)'''

def splice(seq):
    # Function to splice a sequence based on donor and acceptor sites
    global donor, acceptor  # Use global donor and acceptor variables
    donor_matches = re.finditer(donor, seq)  # Find all donor matches in the sequence
    acceptor_matches = re.finditer(acceptor, seq)  # Find all acceptor matches in the sequence
    donor_positions = sorted([match.start() for match in donor_matches])  # Get sorted donor positions
    acceptor_positions = sorted([match.start() for match in acceptor_matches])  # Get sorted acceptor positions

    # Initialize lists to store valid donor and acceptor positions
    valid_donors = []
    valid_acceptors = []

    # Find non-overlapping donor/acceptor pairs
    i, j = 0, 0  # Initialize indices for donor and acceptor positions
    while i < len(donor_positions) and j < len(acceptor_positions):  # Loop through positions
        if donor_positions[i] < acceptor_positions[j]:  # Check if donor is before acceptor
            if not valid_acceptors or donor_positions[i] > valid_acceptors[-1]:  # Ensure no overlap
                valid_donors.append(donor_positions[i])  # Add donor position to valid list
                valid_acceptors.append(acceptor_positions[j])  # Add acceptor position to valid list
            i += 1  # Move to the next donor position
            j += 1  # Move to the next acceptor position
        else:
            j += 1  # Move to the next acceptor position if donor is not valid

    if valid_acceptors and valid_donors:
        return True
    else:
        return False
    '''# Construct the new spliced sequence
    if valid_donors and valid_acceptors:  # Check if valid pairs exist
        new_seq = ""  # Initialize the new sequence
        last_position = 0  # Track the position to start keeping sequence parts
        for d, a in zip(valid_donors, valid_acceptors):  # Iterate through valid donor/acceptor pairs
            new_seq += seq[last_position:d]  # Add the part before the donor site
            last_position = a + len(acceptor)  # Update the position to start after the acceptor site
        new_seq += seq[last_position:]  # Add the remaining sequence after the last acceptor
    else:
        new_seq = seq  # If no valid pairs, return the original sequence

    return new_seq  # Return the spliced sequence'''


def count_tata(seq):
    # Function to count TATA box occurrences in a sequence
    find_tata = re.findall(r"TATA[A,T]A[A,T]", seq)  # Find all TATA box matches
    count = len(find_tata)  # Count the number of matches
    return(count)  # Return the count

genes = read_fasta(file_path)  # Read the input FASTA file into a dictionary
spliced_genes = {}  # Initialize a dictionary to store spliced genes
#output = open(f"{splice_comb}_spliced_genes.fa", "w")  # Open an output file for writing spliced genes
with open (f"{splice_comb}_spliced_genes.fa", "w") as output:
    for gene_name, sequence in genes.items(): # Iterate through each gene and its sequence
        if splice(sequence):
            spliced_genes[gene_name] = sequence
            count = count_tata(sequence)
            output.write(f">{gene_name}_TATAbox_number: {count}\n")
            output.write(f"{sequence}\n")
            #output.write(f"The TATA box number is: {count}\n")
    '''new_sequence = splice(sequence)  # Splice the sequence
    spliced_genes[gene_name] = new_sequence  # Store the spliced sequence in the dictionary
    gene_name = ">" + gene_name + "\n"  # Format the gene name for FASTA output
    output.write(gene_name)  # Write the gene name to the output file
    new_sequence_o = new_sequence + "\n"  # Format the spliced sequence for FASTA output
    output.write(new_sequence_o)  # Write the spliced sequence to the output file
    count = count_tata(new_sequence)  # Count TATA boxes in the spliced sequence
    output.write(f"TATA box number: {count}\n")  # Write the TATA box count to the output file'''
output.close()  # Close the output file
