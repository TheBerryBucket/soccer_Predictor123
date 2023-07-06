import csv
from recordtype import recordtype

team = recordtype ('Team', 'name win lose tie winningchance')
teamsList = []



with open ('results.csv', 'r',encoding='utf-8') as csv_file:
    matchList = csv.DictReader(csv_file)

    for match in matchList:
        homeTeam = [team for team in teamsList if team.name == match['home_team']]
        
        if not homeTeam:
            homeTeam = team (match['home_team'], 0 , 0 , 0, 0)
            teamsList.append (homeTeam)
        
        else:
            homeTeam = homeTeam[0]
            awayTeam = [team for team in teamsList if team.name == match['away_team']]
        
        if not awayTeam:
            awayTeam = team (match['away_team'], 0 , 0 , 0, 0)
            teamsList.append (awayTeam)
        
        else:
            awayTeam = awayTeam[0]

        if match['home_score'] == match['away_score']:
            homeTeam.tie = homeTeam.tie + 1
            awayTeam.tie = awayTeam.tie + 1

        if match['home_score'] > match['away_score']:
            homeTeam.win +=1
            awayTeam.lose = awayTeam.lose + 1

        if match['home_score'] < match['away_score']:
            homeTeam.lose = homeTeam.lose + 1
            awayTeam.win = awayTeam.win + 1
        #homeTeam.winningchance =  homeTeam.win + homeTeam.tie * 0.5
        #homeTeam.winningchance = team.winningchance / (homeTeam.win + homeTeam.tie + homeTeam.lose)
        #awayTeam.winningchance = awayTeam.win + awayTeam.tie * 0.5
        #awayTeam.winningchance = awayTeam.winningchance / (awayTeam.win + awayTeam.tie + awayTeam.lose)
#        team.remove ('win')
#        team.remove ('lose')
#        team.remove ('tie')



def SortTeams(team):
  return team.name


teamsList.sort(key=SortTeams)

print (teamsList)