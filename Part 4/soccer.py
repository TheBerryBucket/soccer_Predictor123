import csv
from recordtype import recordtype

team = recordtype ('Team', 'name win lose tie winningchance')
teamsList = []

i = 0

with open ('results.csv', 'r',encoding='utf-8') as csv_file:
    matchList = csv.DictReader(csv_file)

    for match in matchList:
        a = match['tournament'] == "FIFA World Cup"
        if a == False:
            a = 'Fix'
        if a == True:
            a = match
            i = i + 1
            print (i , a)

   # for match in matchList:
      #  a == True:
     #       i = i +


#teamsList.remove ('win')
#teamsList.remove ('lose')
#teamsList.remove ('tie')

#def SortTeams(team):
  #return team.winningchance #tournament


#teamsList.sort(key=SortTeams)

#print (teamsList)