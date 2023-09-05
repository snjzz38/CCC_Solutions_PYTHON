Times = int(input(""))
Last = ''
Count = 0

for i in range(Times):
    txt = input("")
    for j in range(len(txt)):
        if txt[j] == Last:
            Count += 1
            if j == len(txt)-1:
                print(Count, " ", Last, " ", end='')
                print("")
                Last = ''
                Count = 0
        else:
            if Last != '':
                print(Count, " ", Last, " ", end='')
            letter = txt[j]
            Last = txt[j]
            Count = 1
            if j == len(txt)-1:
                print(Count, " ", Last, " ", end='')
                print("")
                Last = ''
                Count = 0

            

# 4
# +++===!!!!
# 777777......TTTTTTTTTTTT
# (AABBC)
# 3.1415555    