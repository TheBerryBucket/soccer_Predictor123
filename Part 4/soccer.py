import csv
from recordtype import recordtype

team = recordtype('Team', 'name win lose draw')
teamsList = []

with open('results.csv', 'r', encoding='utf-8') as csv_file:
    matchList = csv.DictReader(csv_file)

    for match in matchList:
        homeTeam = [team for team in teamsList if team.name == match['home_team']]
        awayTeam = [team for team in teamsList if team.name == match['away_team']]

        if not homeTeam:
            homeTeam = team (match['home_team'], 0 , 0 , 0)
            teamsList.append (homeTeam)
        
        else:
            homeTeam = homeTeam[0]

        if not awayTeam:
            awayTeam = team (match['away_team'], 0 , 0 , 0)
            teamsList.append (awayTeam)
        
        else:
            awayTeam = awayTeam[0]

        a = match['tournament'] == "FIFA World Cup"
        if a == True:
            
            if match['home_team'][0] == match['away_team'][0]:
                if match['home_score'] == match['away_score']:
                    print ('1 - draw' , match)

                if match['home_score'] != match['away_score']:
                    print ("0.3 - draw" , match)

            if match['home_team'][0] < match['away_team'][0]:
                if match['home_score'] > match['away_score']:
                    print ('1 - homeWin' , match)

                if match['home_score'] == match['away_score']:
                    print ('0.3 - homeWin' , match)

                if match['home_score'] < match['away_score']:
                    print("0 - homeWin" , match)

            if match['home_team'][0] > match['away_team'][0]:
                if match['home_score'] < match['away_score']:
                    print ('1 - awayWin' ,match)

                if match['home_score'] == match['away_score']:
                    print ('0.3 - awayWin' , match)

                if match['home_score'] > match['away_score']:
                    print ('0', 'awayWin', match)


