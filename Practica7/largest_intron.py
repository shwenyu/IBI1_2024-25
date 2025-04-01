import re
seq = "ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA"
gt_pos = []
ag_pos = []
for i in range(0, len(seq)-1):
    if seq[i:i+2] == "GT":
        gt_pos.append(i)
    if seq[i:i+2] == "AG":
        ag_pos.append(i+1)
max_len = 0
max_intron = ''
for i in range(min(len(gt_pos), len(ag_pos))):
    leng = ag_pos[i] - gt_pos[i] + 1
    intron = seq[gt_pos[i]:ag_pos[i]+1]
    if leng > max_len:
        max_len = leng
        max_intron = intron

#intron = re.findall(r"GT\S+?AG", seq)
print(max_len, max_intron)