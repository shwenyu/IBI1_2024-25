import re  # Import the regular expression module for pattern matching
splice_comb = input("What is your splice_combination (GTAG, GCAG,ATAC):")  # Prompt user for splice combination input
file_path = "tata_genes.fa"  # Define the file path for the input FASTA file
donor = splice_comb[0:2]  # Extract the first two characters as the donor sequence
acceptor = splice_comb[2:4]  # Extract the last two characters as the acceptor sequence

def read_fasta(file_path):
    # Function to read a FASTA file and return a dictionary of gene sequences
    genes = {}  # Initialize an empty dictionary to store gene sequences
    current_gene = None  # Variable to track the current gene being processed
    
    with open(file_path, 'r') as file:  # Open the FASTA file for reading
        for line in file:  # Iterate through each line in the file
            line = line.strip()  # Remove leading and trailing whitespace from the line
            if line.startswith('>'):  # Check if the line is a header (starts with '>')
                if current_gene is not None:  # If a gene is being tracked, save its sequence
                    genes[current_gene] = ''.join(genes[current_gene])  # Join sequence parts into a single string
                current_gene = line[1:]  # Extract the gene name (remove '>')
                genes[current_gene] = []  # Initialize an empty list to store sequence parts for the gene
            else:  # If the line is a sequence
                if current_gene is not None:  # Ensure a gene is being tracked
                    genes[current_gene].append(line)  # Append the sequence part to the gene's list

        # Save the last gene after finishing the file
        if current_gene is not None:  # Check if there is a gene being tracked
            genes[current_gene] = ''.join(genes[current_gene])  # Join sequence parts into a single string

        return genes  # Return the dictionary of gene sequences

def splice(seq):
    # Function to splice a sequence based on donor and acceptor sites
    global donor, acceptor  # Use global donor and acceptor variables
    donor_matches = re.finditer(donor, seq)  # Find all donor matches in the sequence
    acceptor_matches = re.finditer(acceptor, seq)  # Find all acceptor matches in the sequence
    donor_positions = sorted([match.start() for match in donor_matches])  # Get sorted donor positions
    acceptor_positions = sorted([match.start() for match in acceptor_matches])  # Get sorted acceptor positions

    # Initialize lists to store valid donor and acceptor positions
    valid_donors = []  # List to store valid donor positions
    valid_acceptors = []  # List to store valid acceptor positions

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

    if valid_acceptors and valid_donors:  # Check if valid donor and acceptor positions exist
        return True  # Return True if splicing is possible
    else:
        return False  # Return False if splicing is not possible

def count_tata(seq):
    # Function to count TATA box occurrences in a sequence
    find_tata = re.findall(r"TATA[A,T]A[A,T]", seq)  # Find all TATA box matches using a regex pattern
    count = len(find_tata)  # Count the number of matches
    return(count)  # Return the count

genes = read_fasta(file_path)  # Read the input FASTA file into a dictionary of gene sequences
spliced_genes = {}  # Initialize an empty dictionary to store spliced genes

with open(f"{splice_comb}_spliced_genes.fa", "w") as output:  # Open an output file for writing spliced genes
    for gene_name, sequence in genes.items():  # Iterate through each gene and its sequence
        if splice(sequence):  # Check if the sequence can be spliced
            spliced_genes[gene_name] = sequence  # Add the sequence to the spliced genes dictionary
            count = count_tata(sequence)  # Count the number of TATA boxes in the sequence
            output.write(f">{gene_name}_TATAbox_number: {count}\n")  # Write the gene name and TATA box count to the file
            output.write(f"{sequence}\n")  # Write the sequence to the file

output.close()  # Close the output file
