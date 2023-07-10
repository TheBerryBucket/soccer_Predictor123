import csv
from recordtype import recordtype

team = recordtype ('Team', 'name win lose tie')
teamsList = []



with open ('results.csv', 'r',encoding='utf-8') as csv_file:
    matchList = csv.DictReader(csv_file)

    for match in matchList:
        homeTeam = [team for team in teamsList if team.name == match['home_team']]
        awayTeam = [team for team in teamsList if team.name == match['away_team']]


        a = match['tournament'] == "FIFA World Cup"
        if a == True:
            
            if match['home_team'][0][0] == match['away_team'][0][0]:
                print ("Draw",(match))

            if match['home_team'][0][0] < match['away_team'][0][0]:
                print ("HomeWin",(match))

            if match['home_team'][0][0] > match['away_team'][0][0]:
                print ("AwayWin",(match))

    


#teamsList.remove ('win')
#teamsList.remove ('lose')
#teamsList.remove ('tie')

#def SortTeams(team):
  #return team.name


#teamsList.sort(key=SortTeams)
#print (teamsList)