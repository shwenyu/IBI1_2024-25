import re  # Import the regular expression module for pattern matching

# file_path stores the path to the input FASTA file
file_path = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"

# Define a function to read a FASTA file and parse its contents
def read_fasta(file_path):
    genes = {}  # Initialize a dictionary to store gene sequences
    current_gene = None  # Variable to track the current gene being processed
    
    # Open the FASTA file for reading
    with open(file_path, 'r') as file:
        for line in file:  # Iterate through each line in the file
            line = line.strip()  # Remove leading/trailing whitespace from the line
            if line.startswith('>'):  # Check if the line is a header line
                if current_gene is not None:  # If a gene was being processed, save its sequence
                    genes[current_gene] = ''.join(genes[current_gene])  # Join sequence parts
                position = re.findall(r">(\S+)_", line)  # Extract gene name using regex
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
    
file_path = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
# file_path stores the path to the input FASTA file
# Define a function to read a FASTA file and parse its contents

# Call the read_fasta function to parse the input file and store the result in find_genes
find_genes = read_fasta(file_path)
#print(find_genes)
# Initialize a dictionary to store genes containing the TATA box pattern
find_tata_gene = {}

# Iterate through each gene and its sequence in the parsed data
for gene_name, sequence in find_genes.items():
    # Search for the TATA box pattern in the sequence
    find_tata = re.search(r"TATA[AT]A[AT]", sequence)
    #print(find_tata)
    if find_tata:  # If the gene contains the TATA box pattern
        find_tata_gene[gene_name] = sequence  # Add the gene to the dictionary
#print(find_tata_gene)
# Write the genes containing the TATA box pattern to an output file
output_file = "tata_genes.fa"
with open(output_file, "w") as output:
    for gene_name, sequence in find_tata_gene.items():
        # Write the gene name and sequence in FASTA format
        output.write(f">{gene_name}\n")
        output.write(f"{sequence}\n")