P = int(input(""))
N = int(input(""))
R = int(input(""))
Day = 0
total = N
DayNum = N

while total <= P:
    DayNum = DayNum*R
    Day += 1
    total += DayNum
print(Day)
