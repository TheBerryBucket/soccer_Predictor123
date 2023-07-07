import csv
from recordtype import recordtype

team = recordtype ('Team', ' homeWin awayWin draw')
#teamsList = []

#homeTeam = [0][0]

with open ('results.csv', 'r',encoding='utf-8') as csv_file:
    matchList = csv.DictReader(csv_file)

    for match in matchList:

        #homeTeam = homeTeam[0]
        #awayTeam = awayTeam[0]

        if match['home_team'[0][0]] == match['away_team'[0][0]]:
            team.draw = team.draw
            print ()
        if match['home_team'[0][0]] < match['away_team'[0][0]]:
            team.homeWin = team.homeWin
            print ()
        if match['home_team'[0][0]] > match['away_team'[0][0]]:
            team.awayWin = team.awayWin
            print ()



#def SortTeams(team):
#  return team.name


#teamsList.sort(key=SortTeams)

#print (teamsList)