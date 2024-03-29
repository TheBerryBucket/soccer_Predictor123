import csv
from recordtype import recordtype

team = recordtype('Team', 'name win lose draw winningchance EloRating')
teamsList = []
total = 0
score = 0

with open("c:/Users/Gareth/Documents/Github/soccer_Predictor123/Part 4/results.csv", 'r', encoding='utf-8') as csv_file:
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
        mov = int(match['home_score']) - int(match['away_score'])
        af = 1
        Af = 1
  
        if mov == 2:
            af = 1.5

        if mov == 3:
            af = 1.75

        if mov >= 4:
            af = 1.9

        if mov == -2:
            Af = 1.5

        if mov == -3:
            Af = 1.75

        if mov <= -4:
            Af = 1.9

    
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

            
        mi = 40
        er = 1 / (10**(-rd/400) + 1)
        mov = int(match['home_score']) - int(match['away_score'])
        af = 1
        Af = 1
  
        if mov == 2:
            af = 1.5

        if mov == 3:
            af = 1.75

        if mov <= 4:
            af = 1.9

        if mov == -2:
            Af = 1.5

        if mov == -3:
            Af = 1.75

        if mov >= -4:
            Af = 1.9

        if ['tournament'] == 'friendly':
            mi = 20
        if ['touranemnt'] == 'FIFA World Cup':
            mi = 60

        homeTeam.EloRating = homeTeam.EloRating - mi * (ar-er) * af
        awayTeam.EloRating = awayTeam.EloRating + mi * (ar-er) * Af
            
        if a == True:
            total += 1
            score += matchScore


                   
       

print (score)
print (total)
score = score / total
print(score)
