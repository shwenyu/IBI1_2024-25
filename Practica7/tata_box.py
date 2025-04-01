import re  # Import the regular expression module for pattern matching

# file_path stores the path to the input FASTA file
file_path = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"

# Define a function to read a FASTA file and parse its contents
def read_fasta(file_path):
    genes = {}  # Initialize a dictionary to store gene sequences
    current_gene = None  # Variable to track the current gene being processed
    
    # Open the FASTA file for reading
    with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as file:
        for line in file:  # Iterate through each line in the file
            line = line.strip()  # Remove leading/trailing whitespace from the line
            if line.startswith('>'):  # Check if the line is a header line
                if current_gene is not None:  # If a gene was being processed, save its sequence
                    genes[current_gene] = ''.join(genes[current_gene])  # Join sequence parts
                position = re.findall(r"(>\S+)_", line)  # Extract gene name using regex
                if len(position) > 0:  # If a gene name is found
                    current_gene = position[0]  # Set the current gene name
                genes[current_gene] = []  # Initialize a list to store sequence parts
            else:  # If the line is a sequence line
                if current_gene is not None:  # Ensure a gene is being processed
                    genes[current_gene].append(line)  # Append the sequence part to the list

        # After the loop, save the last gene being processed
        if current_gene is not None:
            genes[current_gene] = ''.join(genes[current_gene])  # Join sequence parts

        return genes  # Return the dictionary of genes and their sequences

# Call the read_fasta function to parse the input file and store the result in find_genes
find_genes = read_fasta(file_path)

# Initialize a dictionary to store genes containing the TATA box pattern
find_tata_gene = {}

# Iterate through each gene and its sequence in the parsed data
for gene_name, sequence in find_genes.items():
    # Search for the TATA box pattern in the sequence
    find_tata = re.findall(r"TATA[A,T]A[A,T]", sequence)
    if len(find_genes) > 0:  # If the gene contains the TATA box pattern
        find_tata_gene[gene_name] = sequence  # Add the gene to the dictionary

# Open an output file to write the genes containing the TATA box pattern
output = open("tata_genes.fa", "w")

# Iterate through each gene and its sequence in the parsed data
for gene_name, sequence in find_genes.items():
    gene_name = gene_name + "\n"  # Add a newline character to the gene name
    output.write(gene_name)  # Write the gene name to the output file
    sequence = sequence + "\n"  # Add a newline character to the sequence
    output.write(sequence)  # Write the sequence to the output file

output.close()  # Close the output file