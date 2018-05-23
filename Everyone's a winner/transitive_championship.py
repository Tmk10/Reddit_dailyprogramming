WINNERS_LIST =["Villanova"]
SCORE_TABLE = []

#Loading data from file
with open("games.txt","r") as f:
    for line in f:
        SCORE_TABLE.append((line[12:36].strip(),int(line[36:40]), line[41:66].strip(),int(line[66:69])))

#Checking who wins the game

def who_wins(score_tuple):
    if score_tuple[1] < score_tuple[3]:
        return score_tuple[2]  
    else:
        return score_tuple[0]

#Looking for all transitive champions

def check_transitive_champion(team):
    for element in SCORE_TABLE:
        winner = who_wins(element)
        if team in element and winner!= team:
            if winner not in WINNERS_LIST:
                WINNERS_LIST.append(winner)
                check_transitive_champion(winner)
    return len(WINNERS_LIST)

            

print(check_transitive_champion("Villanova"))
            
    
