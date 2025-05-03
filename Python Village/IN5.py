with open('example.txt', mode='r', encoding='utf-8') as file:
    for i, line in enumerate(file):
        if i % 2 == 1:
            print(line.strip())