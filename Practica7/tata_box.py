import re
#fa = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
file_path = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
def read_fasta(file_path):
    genes = {}  # Dictionary to store gene parts
    current_gene = None  # Track the current gene being read
    
    with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line.startswith('>'):  # Header line
                if current_gene is not None:  # Save the previous gene
                    genes[current_gene] = ''.join(genes[current_gene])
                position = re.findall(r"(>\S+)_",line)
                if len(position) > 0:
                    current_gene = position[0]  # Extract gene name (remove '>')
                genes[current_gene] = []  # Initialize sequence list
            else:  # Sequence line
                if current_gene is not None:
                    genes[current_gene].append(line)

        # Save the last gene
        if current_gene is not None:
            genes[current_gene] = ''.join(genes[current_gene])

        return genes
find_genes = read_fasta(file_path)
find_tata_gene = {}
for gene_name, sequence in find_genes.items():
    find_tata = re.findall(r"TATA[A,T]A[A,T]", sequence)
    if len(find_genes) > 0:
        find_tata_gene[gene_name] = sequence

output = open("tata_genes.fa", "w")
for gene_name, sequence in find_genes.items():
    gene_name = gene_name + "\n"
    output.write(gene_name)
    sequence = sequence + "\n"
    output.write(sequence)
output.close()