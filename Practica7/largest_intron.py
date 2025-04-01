import re  # Import the regular expression module for potential pattern matching
seq = "ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA"  # Define the DNA sequence
gt_pos = []  # Initialize a list to store positions of "GT" start sites
ag_pos = []  # Initialize a list to store positions of "AG" end sites
for i in range(0, len(seq)-1):  # Loop through the sequence, stopping one character before the end
    if seq[i:i+2] == "GT":  # Check if the current two characters are "GT"
        gt_pos.append(i)  # Add the position of "GT" to the list
    if seq[i:i+2] == "AG":  # Check if the current two characters are "AG"
        ag_pos.append(i+1)  # Add the position of "AG" (end index) to the list
max_len = 0  # Initialize the maximum intron length to 0
max_intron = ''  # Initialize the longest intron sequence as an empty string
for i in range(min(len(gt_pos), len(ag_pos))):  # Loop through the smaller of the two position lists
    leng = ag_pos[i] - gt_pos[i] + 1  # Calculate the length of the intron
    intron = seq[gt_pos[i]:ag_pos[i]+1]  # Extract the intron sequence from the DNA
    if leng > max_len:  # Check if the current intron is longer than the previous maximum
        max_len = leng  # Update the maximum intron length
        max_intron = intron  # Update the longest intron sequence

# intron = re.findall(r"GT\S+?AG", seq)  # (Commented out) Alternative approach using regex to find introns
print(max_len, max_intron)  # Print the length and sequence of the longest intron