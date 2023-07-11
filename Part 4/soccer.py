import csv
from recordtype import recordtype

team = recordtype('Team', 'name win lose draw winningchance')
teamsList = []
total = 0
score = 0

with open('results.csv', 'r', encoding='utf-8') as csv_file:
    matchList = csv.DictReader(csv_file)

    for match in matchList:
        homeTeam = [team for team in teamsList if team.name == match['home_team']]
        awayTeam = [team for team in teamsList if team.name == match['away_team']]
        a = match['tournament'] == "FIFA World Cup"
        if not homeTeam:
            homeTeam = team(match['home_team'], 0, 0, 0, 1000)
            teamsList.append(homeTeam)
        else:
            homeTeam = homeTeam[0]

        if not awayTeam:
            awayTeam = team(match['away_team'], 0, 0, 0, 1000)
            teamsList.append(awayTeam)
        else:
            awayTeam = awayTeam[0]
        
        if a == False:
            if match['home_score'] > match['away_score']:
                homeTeam.winningchance += 1
                awayTeam.winningchance -= 1
                
            if match['home_score'] < match['away_score']:
                homeTeam.winningchance -= 1
                awayTeam.winningchance += 1
        
        if a == True:
  
            if homeTeam.winningchance > awayTeam.winningchance:
                if match['home_score'] > match['away_score']:
                    #print('1 - HomeWin', match)
                    total = total + 1
                    score = score + 1

                if match['home_score'] == match['away_score']:
                    #print('0.3 - homeWin', match)
                    total = total + 1
                    score = score + 0.3

                if match['home_score'] < match['away_score']:
                    #print("0 - homeWin", match)
                    total = total + 1

            if homeTeam.winningchance == awayTeam.winningchance:
                if match['home_score'] == match['away_score']:
                    #print("1 - draw", match)
                    total = total + 1
                    score = score + 1

                if match['home_score'] != match['away_score']:
                    #print("0.3 - draw", match)
                    total = total + 1
                    score = score + 0.3

            if homeTeam.winningchance < awayTeam.winningchance:
                if match['home_score'] < match['away_score']:
                    #print('1 - awayWin', match)
                    total = total + 1
                    score = score + 1

                if match['home_score'] == match['away_score']:
                    #print('0.3 - awayWin', match)
                    total = total + 1
                    score = score + 0.3

                if match['home_score'] > match['away_score']:
                    #print('0 - awayWin', match)
                    total = total + 1

score = score / total
print(score)
print (awayTeam.winningchance)
print (homeTeam.winningchance)
