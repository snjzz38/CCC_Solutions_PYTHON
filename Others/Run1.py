table = {'Holy Grail': '1975', 
'Life of Brian': '1979',
'The Meaning of Life': '1983'}

print(table['Holy Grail'])

list(table.items())
print([key for (key, value) in table.items() if value == '1975'])
