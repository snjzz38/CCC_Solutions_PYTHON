d = {'a': 100, 'b': 20, 'c': 50, 'd': 100, 'e': 80}

print(max(d, key=d.get))
# a

print(min(d, key=d.get))
# b