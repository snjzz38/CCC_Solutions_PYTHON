def seq(list):
    delta = list[1]-list[0]
    Flag = True 
    for i in range(len(list)-1):
        if list[i+1]-list[i] != delta:
            Flag = False
            break 
    return Flag 

D = int(input(""))
Time = []

Loop = int(D/720)
Total = Loop*31
Rest = D%720


for i in range(1, Rest+1):
    Hours = int(i/60)
    Minutes = i%60
    Time.clear()
    if Hours < 10 and Hours > 0:
        Time.append(Hours)
    elif Hours == 0:
        Time.append(1)
        Time.append(2)
    else:
        Time.append(1)
        Time.append(Hours-10)
    if Minutes < 10:
        Time.append(0)
        Time.append(Minutes)
    else:
        Time.append(int(Minutes/10))
        Time.append(Minutes % 10)
    if seq(Time):
        Total += 1   
print(Total)


