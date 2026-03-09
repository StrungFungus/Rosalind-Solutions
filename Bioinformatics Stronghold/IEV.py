# IEV

population = input("Insert data:").split()
genotypes = {0: 4, 
             1: 4, 
             2: 4, 
             3: 3, 
             4: 2, 
             5:0}

generation = 0

for index, value in enumerate(population):
    generation += genotypes[index] * int(value)

print(generation)
proper = generation / 2
print(proper)