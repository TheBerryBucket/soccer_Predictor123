import csv
from recordtype import recordtype

team = recordtype('Team', 'name win lose draw winningchance EloRating')
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
            homeTeam = team(match['home_team'], 0, 0, 0, 1000, 1000)
            teamsList.append(homeTeam)
        else:
            homeTeam = homeTeam[0]

        if not awayTeam:
            awayTeam = team(match['away_team'], 0, 0, 0, 1000, 1000)
            teamsList.append(awayTeam)
        else:
            awayTeam = awayTeam[0]

        rd = homeTeam.EloRating - awayTeam.EloRating

        if match['neutral'] == 'FALSE':
            rd += 100

        matchScore = 0
        ar = 0
        if -50 <= rd <= 50:


            if match['home_score'] != match['away_score']:
                if match['home_score'] > match['away_score']:
                    ar = 1
                else:
                    ar = 0
                
                    
                matchScore = 0.3

            if match['home_score'] == match['away_score']:
                #print( homeTeam, awayTeam , (homeTeam.EloRating) , (awayTeam.EloRating))
                ar = 0.5
                # print('1 - Draw', match)
                matchScore = 1



        if rd > 50:

            if match['home_score'] > match['away_score']:
                #print('1 - HomeWin', match)
                matchScore = 1
                #print( homeTeam, awayTeam , (homeTeam.EloRating) , (awayTeam.EloRating))
                ar = 1

            if match['home_score'] == match['away_score']:
                #print('0.3 - HomeWin', match)
                matchScore = 0.3
                #print( homeTeam, awayTeam , (homeTeam.EloRating) , (awayTeam.EloRating))
                ar = 0.5

            if match['home_score'] < match['away_score']:
                #print('0 - HomeWin', match)
                #print( homeTeam, awayTeam , (homeTeam.EloRating) , (awayTeam.EloRating))
                ar = 0



        if rd < -50: 

            if match['home_score'] < match['away_score']:
                #print('1 - AwayWin', match)
                matchScore = 1
                #print( homeTeam, awayTeam , (homeTeam.EloRating) , (awayTeam.EloRating))
                ar = 0
            if match['home_score'] == match['away_score']:
                #print('0.3 - AwayWin', match)
                matchScore = 0.3
                #print( homeTeam, awayTeam , (homeTeam.EloRating) , (awayTeam.EloRating))
                ar = 0.5
                    
            if match['home_score'] > match['away_score']:
                #print('0 - AwayWin', match)
                #print( homeTeam, awayTeam , (homeTeam.EloRating) , (awayTeam.EloRating))
                ar = 1

            

        er = 1 / (10**(-rd/400) + 1)



        homeTeam.EloRating = homeTeam.EloRating + 40 * (ar-er)
        awayTeam.EloRating = awayTeam.EloRating - 40 * (ar-er)
            
        if a == True:
            total += 1
            score += matchScore


                   
       

print (score)
print (total)
score = score / total
print(score)
