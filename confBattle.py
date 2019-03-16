from sportsreference.nba.teams import Teams


east = ['MIL', 'TOR', 'PHI', 'IND', 'BOS', 'BKN', 'DET', 'MIA', 'ORL', 'CHA', 'WAS', 'ATL', 'CHI', 'CLE', 'NYK']

teams = Teams()
for team in teams:
    # Creates an instance of the roster class for each player on the team.
    if team.abbreviation in east:
    	print(team.record)