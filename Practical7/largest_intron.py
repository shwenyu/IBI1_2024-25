import re  # Import the regular expression module for potential pattern matching
# Pseudocode: Import the 're' module to use regular expressions for pattern matching.

seq = "ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA"  # Define the DNA sequence
# Pseudocode: Define a string variable 'seq' to store the DNA sequence.

intron = re.findall(r"GT[ATCG]+AG", seq)
# Pseudocode: Use a regular expression to find all substrings in 'seq' that start with "GT", end with "AG", and have any combination of "A", "T", "C", or "G" in between.

large_intron = max(intron, key=len)
# Pseudocode: Find the longest intron in the list 'intron' by comparing their lengths.

large_len = len(large_intron)
# Pseudocode: Calculate the length of the longest intron and store it in 'large_len'.

print(large_intron, large_len)
# Pseudocode: Print the longest intron and its length.