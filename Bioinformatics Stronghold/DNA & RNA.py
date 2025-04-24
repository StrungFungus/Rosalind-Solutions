import collections

Nucleotide = {
    "DNA": ['A', 'T', 'G', 'C'],
    "RNA": ['A', 'U', 'G', 'C']
}

seq = input("Enter sequence: ")
print(f"{seq}")

trans_seq = seq.replace("T", "U")
print(f"{trans_seq}")

def DNA_Counter():
    return dict(collections.Counter(trans_seq))
print(f"{collections.Counter(trans_seq)}")



