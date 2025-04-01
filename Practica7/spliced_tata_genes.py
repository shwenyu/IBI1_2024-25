import re
splice_comb = input("What is your splice_combination (GTAG, GCAG,ATAC):")
file_path = "tata_genes.fa"
donor = splice_comb[0:2]
acceptor = splice_comb[2:4]
def read_fasta(file_path):
    genes = {}  # Dictionary to store gene parts
    current_gene = None  # Track the current gene being read
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line.startswith('>'):  # Header line
                if current_gene is not None:  # Save the previous gene
                    genes[current_gene] = ''.join(genes[current_gene])
                current_gene = line[1:]  # Extract gene name (remove '>')
                genes[current_gene] = []  # Initialize sequence list
            else:  # Sequence line
                if current_gene is not None:
                    genes[current_gene].append(line)

        # Save the last gene
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
    global donor, acceptor
    donor_matches = re.finditer(donor, seq)
    acceptor_matches = re.finditer(acceptor, seq)
    donor_positions = sorted([match.start() for match in donor_matches])
    acceptor_positions = sorted([match.start() for match in acceptor_matches])

    # Initialize lists to store valid pairs
    valid_donors = []
    valid_acceptors = []

    # Find non-overlapping donor/acceptor pairs
    i, j = 0, 0
    while i < len(donor_positions) and j < len(acceptor_positions):
        if donor_positions[i] < acceptor_positions[j]:
            # Ensure no overlap with the previous acceptor
            if not valid_acceptors or donor_positions[i] > valid_acceptors[-1]:
                valid_donors.append(donor_positions[i])
                valid_acceptors.append(acceptor_positions[j])
            i += 1
            j += 1
        else:
            j += 1

    # Construct the new sequence
    if valid_donors and valid_acceptors:
        new_seq = ""
        for d, a in zip(valid_donors, valid_acceptors):
            new_seq += seq[d + 2:a]  # Extract subsequence from donor+2 to acceptor
    else:
        new_seq = seq

    return new_seq

def count_tata(seq):
    find_tata = re.findall(r"TATA[A,T]A[A,T]", seq)
    count = len(find_tata)
    return(count)

genes = read_fasta(file_path)
spliced_genes = {}
output = open(f"{splice_comb}_spliced_genes.fa", "w")
for gene_name, sequence in genes.items():
    #print(sequence)
    new_sequence = splice(sequence)
    spliced_genes[gene_name] = new_sequence
    gene_name = ">" + gene_name + "\n"
    output.write(gene_name)
    new_sequence_o = new_sequence + "\n"
    output.write(new_sequence_o)
    count = count_tata(new_sequence)
    output.write(f"TATA box number: {count}\n")
output.close()