def recognition(dna, enzyme):  # Define a function to find the position of the enzyme in the DNA sequence
    len_enz = len(enzyme)  # Get the length of the enzyme sequence
    len_DNA = len(dna)  # Get the length of the DNA sequence
    pos = []
    flag = False
    for i in range(len_DNA-len_enz+1):  # Loop through the DNA sequence to check for matches
        cut = dna[i:i+len_enz]  # Extract a substring of the same length as the enzyme
        if cut == enzyme:  # Check if the substring matches the enzyme sequence
            pos.append(i)  # Store the starting position of the match
            flag = True
    if flag == True:
        return(pos)  # Return the position of the match
    else:
        return("Not found")  # Return "Not found" if no match is found

def check(seq):  # Define a function to validate the sequence
    for i in range(len(seq)):  # Loop through each character in the sequence
        if not seq[i] in ["A", "G", "C", "T"]:  # Check if the character is not a valid nucleotide
            return(False)  # Return False if an invalid character is found
    return(True)  # Return True if all characters are valid nucleotides

dna = input("DNA sequence:")  # Prompt the user to input a DNA sequence
enzyme = input("Enzyme sequence:")  # Prompt the user to input an enzyme sequence
if check(dna) and check(enzyme):
    result = recognition(dna, enzyme)  # Check if both the DNA and enzyme sequences are valid
    if isinstance(result, list):  # Check if the recognition function returns a valid position
        print(f"The position(s) of enzyme: {result}")
    else:
        print(result)  # Print "Not found" if the enzyme is not in the DNA
else:
    print("Wrong sequence input!")  # Print an error message if the input sequences are invalid