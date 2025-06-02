def find_motif(Fstring, Sstring):
    Location = []
    for i in range(0, len(Fstring) - len(Sstring) + 1):
        if Fstring[i:i + len(Sstring)] == Sstring:
            Location.append(i+1)
    return Location

Fstring = input("Input the strand:")
Sstring = input("Input the sub-strand:")
results = find_motif(Fstring, Sstring)
print(results)