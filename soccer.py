import math
teams = []
with open('soccer.dat') as f:
	for line in f:
		L = line.split()
		if len(L) > 0 and L[0][0].isnumeric():
			teams.append(L)
num = 0
diff = math.inf
for (ind, team) in enumerate(teams):
	GoalsFor = int(team[6])
	GoalsAgainst = int(team[8])
	teamdiff = abs(GoalsFor - GoalsAgainst)
	if(teamdiff < diff):
		num = ind
		diff = teamdiff

print("Team with minimum difference is " + teams[num][1] + " with " + teams[num][6] + " For Goals and " + teams[num][8] + " Against Goals.")