from sportsreference.nba.teams import Teams
from sportsreference.nba.schedule import Schedule
import time

east = ['MIL', 'TOR', 'PHI', 'IND', 'BOS', 'BKN', 'DET', 'MIA', 'ORL', 'CHA', 'WAS', 'ATL', 'CHI', 'CLE', 'NYK']

def team_record(abbr):
	wins = str([game.wins for game in Schedule(abbr) if game.wins][-1])
	losses = str([game.losses for game in Schedule(abbr) if game.losses][-1])
	return "-".join([wins,losses])

def true_inches(x):
	l = [int(s) for s in x.split('-')]
	return (l[0] * 12) + l[1]

def output(l):
	cnt = 1
	for i in l:
		s = str(cnt) + ". " + i[0] + " (" + i[1] +")"
		print(s)
		cnt += 1
start = time.time()
teams = Teams()
l = []
for team in teams:
	l += [(player.name, player.height) for player in team.roster.players]

sorts = sorted(l, key=lambda x: true_inches(x[1]))
print("10 Shortest Players in NBA:")
shortest = sorts[:10]
output(shortest)
print("\n\n")
print("10 Tallest Players in NBA:")
tallest = sorts[-10:]
output(tallest)
print("Time to run: " + str(time.time() - start))


