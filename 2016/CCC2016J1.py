List = []
Wins = 0

for i in range(6):
    Game = input("")
    List.append(Game)

for i in range(len(List)):
    if List[i] == "W":
        Wins += 1

if Wins == 1 or Wins == 2:
    print("3")
elif Wins == 3 or Wins == 4:
    print("2")
elif Wins == 5 or Wins == 6:
    print("1")
elif Wins == 0:
    print("-1")