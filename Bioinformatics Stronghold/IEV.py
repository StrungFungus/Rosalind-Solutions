# IEV

population = input("Insert data:").split()
genotypes = {0: 4, 
             1: 4, 
             2: 4, 
             3: 3, 
             4: 2, 
             5:0} # hash map of how many in a genetic cross of the given would have a dominant feature

generation = 0

for index, value in enumerate(population):
    generation += genotypes[index] * int(value) # multiples the hash map value by the population value at the same index
print(generation)
proper = generation / 2
print(proper)