import collections

Nucleotide = {
    "DNA": ['A', 'T', 'G', 'C'],
    "RNA": ['A', 'U', 'G', 'C']
}

seq = input("Enter sequence: ")
print(f"{seq}")

rev = ''.join(reversed(seq))
print(rev)
complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
revcom = ''.join([complement[Nucleotide] for Nucleotide in rev])
print(f'revcome:{revcom}')
