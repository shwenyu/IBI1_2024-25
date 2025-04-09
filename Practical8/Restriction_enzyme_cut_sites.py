def recognition(dna, enzyme):  # Define a function to find the position of the enzyme in the DNA sequence
    len_enz = len(enzyme)  # Get the length of the enzyme sequence
    len_DNA = len(dna)  # Get the length of the DNA sequence
    for i in range(len_DNA-len_enz+1):  # Loop through the DNA sequence to check for matches
        cut = dna[i:i+len_enz]  # Extract a substring of the same length as the enzyme
        if cut == enzyme:  # Check if the substring matches the enzyme sequence
            pos = i  # Store the starting position of the match
            return(pos)  # Return the position of the match
    return("Not found")  # Return "Not found" if no match is found

def check(seq):  # Define a function to validate the sequence
    for i in range(len(seq)):  # Loop through each character in the sequence
        if not seq[i] in ["A", "G", "C", "T"]:  # Check if the character is not a valid nucleotide
            return(False)  # Return False if an invalid character is found
    return(True)  # Return True if all characters are valid nucleotides

dna = input("DNA sequence:")  # Prompt the user to input a DNA sequence
enzyme = input("Enzyme sequence:")  # Prompt the user to input an enzyme sequence
if check(dna) and check(enzyme):  # Check if both the DNA and enzyme sequences are valid
    if isinstance(recognition(dna, enzyme), int):  # Check if the recognition function returns a valid position
        beg = recognition(dna, enzyme)  # Get the starting position of the enzyme in the DNA
        end = beg + len(enzyme) - 1  # Calculate the ending position of the enzyme in the DNA
        print(f"The position of enzyme is from {beg} to {end}")  # Print the position of the enzyme
    else:
        print(recognition(dna, enzyme))  # Print "Not found" if the enzyme is not in the DNA
else:
    print("Wrong sequence input!")  # Print an error message if the input sequences are invalid