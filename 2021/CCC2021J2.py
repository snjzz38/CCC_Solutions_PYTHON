People = int(input(""))
PeopleList = []
BidsList = []
maxBid = 0
maxIndex = 0

for i in range(People):
    Person = input("")
    PersonBid = int(input("")) 
    if PersonBid > maxBid:
        maxBid = PersonBid
        maxIndex = i
    PeopleList.append(Person)
    BidsList.append(PersonBid)

print(PeopleList[maxIndex])

