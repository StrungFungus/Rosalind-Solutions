def read_file():
    ids = []
    seqs = []
    with open("rosalind_gc.txt", "r", encoding='utf-8') as f:
        sequence = ""
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                line = line[1:]
                if sequence:
                    seqs.append(sequence)
                    sequence = ""
                ids.append(line)
            else:
                sequence += line
        if sequence:
            seqs.append(sequence)
    return ids, seqs


def count_GC(seq):
    count = 0
    for i in seq:
        if i == "C" or i == "G":
            count += 1
    return count / len(seq) * 100 if len(seq) > 0 else 0


def biggest_GC(ids, seqs):
    max_gc = -1
    max_id = ""
    for i in range(len(seqs)):
        gc = count_GC(seqs[i])
        if gc > max_gc:
            max_gc = gc
            max_id = ids[i]
    print(f'{max_id}\n{max_gc:.6f}')


ids, seqs = read_file()
biggest_GC(ids, seqs)