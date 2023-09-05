People = int(input(""))
Dictionary = {}
maxBid = 0
maxIndex = 0

for i in range(People):
    Person = input("")
    PersonBid = int(input("")) 
    Dictionary[Person] = PersonBid

maxBid = max(list(Dictionary.values()))

key_list = list(Dictionary.keys())
val_list = list(Dictionary.values())
 
position = val_list.index(maxBid)
print(key_list[position])


