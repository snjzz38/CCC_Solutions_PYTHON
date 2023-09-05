letters = "ABCDEFGHIJKLMNOPQRST"
numbers = "0123456789"
string = ""
inp = input("")
inp = list(inp)
update = list(inp)

for i in range(len(inp)):
    if inp[i] in letters:
        if inp[i-1] in numbers:
            update.insert(i, "*")
    print(update)
update.pop(0)


for i in inp:
    string += i

string = string.replace("+", " tighten ")
string = string.replace("-", " loosen ")
string = string.replace("*", "\n")

print(string)

# T+1S-1R+2Q-2P+3O-1