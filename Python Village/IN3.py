String = input("Input your string of words here:")
Integers = input("Input your slice integers here:")
slice_locations = Integers.split()
a, b, c, d = map(int, slice_locations)
slice1 = String[a:b+1]
slice2 = String[c:d+1]
print(f"{slice1} {slice2}")