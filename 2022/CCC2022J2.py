Players = int(input(""))
StarPlayers = 0

for i in range(Players):
    PlayersScore = int(input(""))
    PlayersFouls = int(input(""))
    PlayersStars = PlayersScore*5-PlayersFouls*3
    if PlayersStars > 40:
        StarPlayers += 1

if StarPlayers == Players:
    print(StarPlayers,"+", sep='')
else: 
    print(StarPlayers)



